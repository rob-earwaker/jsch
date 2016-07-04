import uuid


class Reference(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def asdict(self):
        return {'$ref': '#/definitions/{0}'.format(self.name)}


class JSchema(object):
    FIELD_NAMES = {
        # meta
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'schema': '$schema',
        'default': 'default',
        # array
        'additional_items': 'additionalItems',
        'items': 'items',
        'max_items': 'maxItems',
        'min_items': 'minItems',
        'unique_items': 'uniqueItems',
        # integer, number
        'multiple_of': 'multipleOf',
        'maximum': 'maximum',
        'exclusive_maximum': 'exclusiveMaximum',
        'minimum': 'minimum',
        'exclusive_minimum': 'exclusiveMinimum',
        # object
        'max_properties': 'maxProperties',
        'min_properties': 'minProperties',
        'required': 'required',
        'additional_properties': 'additionalProperties',
        'properties': 'properties',
        'pattern_properties': 'patternProperties',
        'dependencies': 'dependencies',
        # string
        'max_length': 'maxLength',
        'min_length': 'minLength',
        'pattern': 'pattern',
        # all
        'definitions': 'definitions'
    }

    def __init__(self, type, **kwargs):
        self._ref = Reference(kwargs['ref']) if 'ref' in kwargs else None
        self._dict = {'type': type}
        for field in self.FIELD_NAMES:
            if field in kwargs:
                self._dict[self.FIELD_NAMES[field]] = kwargs[field]

    @property
    def ref(self):
        return self._ref

    def asdict(self):
        return self._dict


def uname():
    return uuid.uuid4().get_hex()


def Properties(**kwargs):
    return kwargs


def Dependencies(**kwargs):
    return kwargs


class JSchemaMeta(type):
    def __call__(cls, *args, **kwargs):
        jschema = super(JSchemaMeta, cls).__call__(*args, **kwargs)
        return type(uname(), (object,), {'jschema': jschema})


class Array(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        if 'additional_items' in kwargs:
            additional_items = kwargs['additional_items']
            if hasattr(additional_items, 'jschema'):
                schema = additional_items.jschema
                if schema.ref is not None:
                    kwargs['additional_items'] = schema.ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][schema.ref.name] = schema.asdict()
                else:
                    kwargs['additional_items'] = schema.asdict()
        if 'items' in kwargs:
            items = kwargs['items']
            if isinstance(items, list):
                kwargs['items'] = []
                for item in items:
                    schema = item.jschema
                    if schema.ref is not None:
                        kwargs['items'].append(schema.ref.asdict())
                        if 'definitions' not in kwargs:
                            kwargs['definitions'] = {}
                        kwargs['definitions'][schema.ref.name] = \
                            schema.asdict()
                    else:
                        kwargs['items'].append(schema.asdict())
            if hasattr(items, 'jschema'):
                schema = items.jschema
                if schema.ref is not None:
                    kwargs['items'] = schema.ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][schema.ref.name] = schema.asdict()
                else:
                    kwargs['items'] = schema.asdict()
        super(Array, self).__init__('array', **kwargs)


class Boolean(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Boolean, self).__init__('boolean', **kwargs)


class Integer(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Integer, self).__init__('integer', **kwargs)


class Null(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Null, self).__init__('null', **kwargs)


class Number(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Number, self).__init__('number', **kwargs)


class Object(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        if 'additional_properties' in kwargs:
            properties = kwargs['additional_properties']
            if hasattr(properties, 'jschema'):
                schema = properties.jschema
                if schema.ref is not None:
                    kwargs['additional_properties'] = schema.ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][schema.ref.name] = schema.asdict()
                else:
                    kwargs['additional_properties'] = schema.asdict()
        if 'properties' in kwargs:
            properties = kwargs['properties']
            for name in properties:
                schema = properties[name].jschema
                if schema.asdict().pop('required', False):
                    if 'required' not in kwargs:
                        kwargs['required'] = []
                    kwargs['required'].append(name)
                if schema.ref is not None:
                    kwargs['properties'][name] = schema.ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][schema.ref.name] = schema.asdict()
                else:
                    kwargs['properties'][name] = schema.asdict()
        if 'pattern_properties' in kwargs:
            properties = kwargs['pattern_properties']
            for name in properties:
                schema = properties[name].jschema
                if schema.ref is not None:
                    kwargs['pattern_properties'][name] = schema.ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][schema.ref.name] = schema.asdict()
                else:
                    kwargs['pattern_properties'][name] = schema.asdict()
        if 'dependencies' in kwargs:
            for name in kwargs['dependencies']:
                dependency = kwargs['dependencies'][name]
                if hasattr(dependency, 'jschema'):
                    schema = dependency.jschema
                    if schema.ref is not None:
                        kwargs['dependencies'][name] = schema.ref.asdict()
                        if 'definitions' not in kwargs:
                            kwargs['definitions'] = {}
                        kwargs['definitions'][schema.ref.name] = \
                            schema.asdict()
                    else:
                        kwargs['dependencies'][name] = schema.asdict()
        super(Object, self).__init__('object', **kwargs)


class String(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(String, self).__init__('string', **kwargs)

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
        self._required = False
        if 'required' in kwargs:
            if isinstance(kwargs['required'], bool):
                self._required = kwargs.pop('required')
        self._ref = Reference(kwargs['ref']) if 'ref' in kwargs else None
        self._dict = {'type': type}
        for field in self.FIELD_NAMES:
            if field in kwargs:
                self._dict[self.FIELD_NAMES[field]] = kwargs[field]

    @property
    def required(self):
        return self._required

    @property
    def ref(self):
        return self._ref

    @property
    def definitions(self):
        return self._dict.get('definitions', None)

    def asdict(self, root=True):
        dict = self._dict.copy()
        if not root:
            dict.pop('definitions', None)
        return dict


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
                    kwargs['definitions'][schema.ref.name] = \
                        schema.asdict(root=False)
                else:
                    kwargs['additional_items'] = schema.asdict(root=False)
                if schema.definitions is not None:
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    for name in schema.definitions:
                        kwargs['definitions'][name] = schema.definitions[name]
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
                            schema.asdict(root=False)
                    else:
                        kwargs['items'].append(schema.asdict(root=False))
            if hasattr(items, 'jschema'):
                schema = items.jschema
                if schema.ref is not None:
                    kwargs['items'] = schema.ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][schema.ref.name] = \
                        schema.asdict(root=False)
                else:
                    kwargs['items'] = schema.asdict(root=False)
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
                    kwargs['definitions'][schema.ref.name] = \
                        schema.asdict(root=False)
                else:
                    kwargs['additional_properties'] = schema.asdict(root=False)
        if 'properties' in kwargs:
            properties = kwargs['properties']
            for name in properties:
                schema = properties[name].jschema
                if schema.required:
                    if 'required' not in kwargs:
                        kwargs['required'] = []
                    kwargs['required'].append(name)
                if schema.ref is not None:
                    kwargs['properties'][name] = schema.ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][schema.ref.name] = \
                        schema.asdict(root=False)
                else:
                    kwargs['properties'][name] = schema.asdict(root=False)
        if 'pattern_properties' in kwargs:
            properties = kwargs['pattern_properties']
            for name in properties:
                schema = properties[name].jschema
                if schema.ref is not None:
                    kwargs['pattern_properties'][name] = schema.ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][schema.ref.name] = \
                        schema.asdict(root=False)
                else:
                    kwargs['pattern_properties'][name] = \
                        schema.asdict(root=False)
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
                            schema.asdict(root=False)
                    else:
                        kwargs['dependencies'][name] = \
                            schema.asdict(root=False)
        super(Object, self).__init__('object', **kwargs)


class String(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(String, self).__init__('string', **kwargs)

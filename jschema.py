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
        'title': 'title',
        'description': 'description',
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

    def asdict(self, root=True, id=None):
        dict = self._dict.copy()
        if not root:
            dict.pop('definitions', None)
        else:
            dict['$schema'] = 'http://json-schema.org/draft-04/schema#'
        if id:
            dict['id'] = id
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
        additional_items = kwargs.get('additional_items', None)
        if hasattr(additional_items, 'jschema'):
            schema = additional_items.jschema
            ref = schema.ref
            if ref is not None:
                kwargs['additional_items'] = ref.asdict()
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                kwargs['definitions'][ref.name] = schema.asdict(root=False)
            else:
                kwargs['additional_items'] = schema.asdict(root=False)
            if schema.definitions is not None:
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                for name in schema.definitions:
                    kwargs['definitions'][name] = schema.definitions[name]
        items = kwargs.get('items', None)
        if isinstance(items, list):
            kwargs['items'] = []
            for item in items:
                schema = item.jschema
                ref = schema.ref
                if ref is not None:
                    kwargs['items'].append(ref.asdict())
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][ref.name] = schema.asdict(root=False)
                else:
                    kwargs['items'].append(schema.asdict(root=False))
        if hasattr(items, 'jschema'):
            schema = items.jschema
            ref = schema.ref
            if ref is not None:
                kwargs['items'] = ref.asdict()
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                kwargs['definitions'][ref.name] = schema.asdict(root=False)
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
        additional_properties = kwargs.get('additional_properties', None)
        if hasattr(additional_properties, 'jschema'):
            schema = additional_properties.jschema
            ref = schema.ref
            if ref is not None:
                kwargs['additional_properties'] = ref.asdict()
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                kwargs['definitions'][ref.name] = schema.asdict(root=False)
            else:
                kwargs['additional_properties'] = schema.asdict(root=False)
        properties = kwargs.get('properties', {})
        for name in properties:
            schema = properties[name].jschema
            ref = schema.ref
            if schema.required:
                if 'required' not in kwargs:
                    kwargs['required'] = []
                kwargs['required'].append(name)
            if ref is not None:
                kwargs['properties'][name] = ref.asdict()
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                kwargs['definitions'][ref.name] = schema.asdict(root=False)
            else:
                kwargs['properties'][name] = schema.asdict(root=False)
        pattern_properties = kwargs.get('pattern_properties', {})
        for name in pattern_properties:
            schema = pattern_properties[name].jschema
            ref = schema.ref
            if ref is not None:
                kwargs['pattern_properties'][name] = ref.asdict()
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                kwargs['definitions'][ref.name] = schema.asdict(root=False)
            else:
                kwargs['pattern_properties'][name] = schema.asdict(root=False)
        for name, dependency in kwargs.get('dependencies', {}).iteritems():
            if hasattr(dependency, 'jschema'):
                schema = dependency.jschema
                ref = schema.ref
                if ref is not None:
                    kwargs['dependencies'][name] = ref.asdict()
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][ref.name] = schema.asdict(root=False)
                else:
                    kwargs['dependencies'][name] = schema.asdict(root=False)
        super(Object, self).__init__('object', **kwargs)


class String(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(String, self).__init__('string', **kwargs)

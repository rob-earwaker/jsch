import uuid


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
        self._optional = kwargs.pop('optional', False)
        schema = {'type': type}
        for field in self.FIELD_NAMES:
            if field in kwargs:
                schema[self.FIELD_NAMES[field]] = kwargs[field]
        if 'ref' in kwargs:
            self._dict = {
                'definitions': schema.pop('definitions', {}),
                '$ref': '#/definitions/{0}'.format(kwargs['ref'])
            }
            self._dict['definitions'][kwargs['ref']] = schema
        else:
            self._dict = schema

    @property
    def optional(self):
        return self._optional

    @property
    def definitions(self):
        return self._dict.get('definitions', {})

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
            kwargs['additional_items'] = schema.asdict(root=False)
            if schema.definitions:
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                for name in schema.definitions:
                    kwargs['definitions'][name] = schema.definitions[name]
        items = kwargs.get('items', None)
        if isinstance(items, list):
            kwargs['items'] = []
            for item in items:
                schema = item.jschema
                kwargs['items'].append(schema.asdict(root=False))
                if schema.definitions:
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    for name in schema.definitions:
                        kwargs['definitions'][name] = schema.definitions[name]
        if hasattr(items, 'jschema'):
            schema = items.jschema
            kwargs['items'] = schema.asdict(root=False)
            if schema.definitions:
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                for name in schema.definitions:
                    kwargs['definitions'][name] = schema.definitions[name]
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
            kwargs['additional_properties'] = schema.asdict(root=False)
            if schema.definitions:
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                for name in schema.definitions:
                    kwargs['definitions'][name] = schema.definitions[name]
        properties = kwargs.get('properties', {})
        for name in properties:
            schema = properties[name].jschema
            kwargs['properties'][name] = schema.asdict(root=False)
            if not schema.optional:
                if 'required' not in kwargs:
                    kwargs['required'] = []
                kwargs['required'].append(name)
            if schema.definitions:
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                for name in schema.definitions:
                    kwargs['definitions'][name] = schema.definitions[name]
        pattern_properties = kwargs.get('pattern_properties', {})
        for name in pattern_properties:
            schema = pattern_properties[name].jschema
            kwargs['pattern_properties'][name] = schema.asdict(root=False)
            if schema.definitions:
                if 'definitions' not in kwargs:
                    kwargs['definitions'] = {}
                for name in schema.definitions:
                    kwargs['definitions'][name] = schema.definitions[name]
        for name, dependency in kwargs.get('dependencies', {}).iteritems():
            if hasattr(dependency, 'jschema'):
                schema = dependency.jschema
                kwargs['dependencies'][name] = schema.asdict(root=False)
                if schema.definitions:
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    for name in schema.definitions:
                        kwargs['definitions'][name] = schema.definitions[name]
        super(Object, self).__init__('object', **kwargs)


class String(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(String, self).__init__('string', **kwargs)

import uuid


class JSchema(object):
    FIELD_NAMES = {
        # meta
        'type': 'type',
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
        'definitions': 'definitions',
        'all_of': 'allOf',
        'any_of': 'anyOf',
        'one_of': 'oneOf'
    }

    def __init__(self, **kwargs):
        self._optional = kwargs.pop('optional', False)
        schema = {}
        for field, field_name in self.FIELD_NAMES.iteritems():
            if field in kwargs:
                schema[field_name] = kwargs[field]
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
        definitions = {}
        additional_items = kwargs.get('additional_items', None)
        if hasattr(additional_items, 'jschema'):
            schema = additional_items.jschema
            kwargs['additional_items'] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        items = kwargs.get('items', None)
        if isinstance(items, list):
            kwargs['items'] = []
            for item in items:
                schema = item.jschema
                kwargs['items'].append(schema.asdict(root=False))
                for name in schema.definitions:
                    definitions[name] = schema.definitions[name]
        elif hasattr(items, 'jschema'):
            schema = items.jschema
            kwargs['items'] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        kwargs['type'] = 'array'
        super(Array, self).__init__(**kwargs)


class Boolean(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        kwargs['type'] = 'boolean'
        super(Boolean, self).__init__(**kwargs)


class Integer(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        kwargs['type'] = 'integer'
        super(Integer, self).__init__(**kwargs)


class Null(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        kwargs['type'] = 'null'
        super(Null, self).__init__(**kwargs)


class Number(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        kwargs['type'] = 'number'
        super(Number, self).__init__(**kwargs)


class Object(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        definitions = {}
        additional_properties = kwargs.get('additional_properties', None)
        if hasattr(additional_properties, 'jschema'):
            schema = additional_properties.jschema
            kwargs['additional_properties'] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        properties = kwargs.get('properties', {})
        for name in properties:
            schema = properties[name].jschema
            kwargs['properties'][name] = schema.asdict(root=False)
            if not schema.optional:
                if 'required' not in kwargs:
                    kwargs['required'] = []
                kwargs['required'].append(name)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        pattern_properties = kwargs.get('pattern_properties', {})
        for name in pattern_properties:
            schema = pattern_properties[name].jschema
            kwargs['pattern_properties'][name] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        dependencies = kwargs.get('dependencies', {})
        for name, dependency in dependencies.iteritems():
            if hasattr(dependency, 'jschema'):
                schema = dependency.jschema
                kwargs['dependencies'][name] = schema.asdict(root=False)
                for name in schema.definitions:
                    definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        kwargs['type'] = 'object'
        super(Object, self).__init__(**kwargs)


class String(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        kwargs['type'] = 'string'
        super(String, self).__init__(**kwargs)


class AllOf(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        types = kwargs.pop('types')
        kwargs['all_of'] = []
        definitions = {}
        for type in types:
            schema = type.jschema
            kwargs['all_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        super(AllOf, self).__init__(**kwargs)


class AnyOf(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        types = kwargs.pop('types')
        kwargs['any_of'] = []
        definitions = {}
        for type in types:
            schema = type.jschema
            kwargs['any_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        super(AnyOf, self).__init__(**kwargs)


class OneOf(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        types = kwargs.pop('types')
        kwargs['one_of'] = []
        definitions = {}
        for type in types:
            schema = type.jschema
            kwargs['one_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        super(OneOf, self).__init__(**kwargs)

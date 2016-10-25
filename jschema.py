import json
import uuid


MAX_ITEMS_KEY = 'max_items'
MIN_ITEMS_KEY = 'min_items'
MAXIMUM_KEY = 'maximum'
EXCLUSIVE_MAXIMUM_KEY = 'exclusive_maximum'
MINIMUM_KEY = 'minimum'
EXCLUSIVE_MINIMUM_KEY = 'exclusive_minimum'


class DefinitionError(Exception):
    pass


def validate_max_items(max_items):
    if max_items is None:
        return
    if not isinstance(max_items, int):
        raise DefinitionError("'{0}' must be an integer".format(MAX_ITEMS_KEY))
    if max_items < 0:
        raise DefinitionError("'{0}' must be gte zero".format(MAX_ITEMS_KEY))


def validate_min_items(min_items):
    if min_items is None:
        return
    if not isinstance(min_items, int):
        raise DefinitionError("'{0}' must be an integer".format(MIN_ITEMS_KEY))
    if min_items < 0:
        raise DefinitionError("'{0}' must be gte zero".format(MIN_ITEMS_KEY))


def validate_maximum(maximum, exclusive_maximum):
    if maximum is not None:
        if not isinstance(maximum, (int, float)):
            raise DefinitionError("'{0}' must be a number".format(MAXIMUM_KEY))
    if exclusive_maximum is not None:
        if not isinstance(exclusive_maximum, bool):
            raise DefinitionError(
                "'{0}' must be a boolean".format(EXCLUSIVE_MAXIMUM_KEY)
            )
        if maximum is None:
            raise DefinitionError(
                "'{0}' must be present if '{1}' is defined".format(
                    MAXIMUM_KEY, EXCLUSIVE_MAXIMUM_KEY
                )
            )


def validate_minimum(minimum, exclusive_minimum):
    if minimum is not None:
        if not isinstance(minimum, (int, float)):
            raise DefinitionError("'{0}' must be a number".format(MINIMUM_KEY))
    if exclusive_minimum is not None:
        if not isinstance(exclusive_minimum, bool):
            raise DefinitionError(
                "'{0}' must be a boolean".format(EXCLUSIVE_MINIMUM_KEY)
            )
        if minimum is None:
            raise DefinitionError(
                "'{0}' must be present if '{1}' is defined".format(
                    MINIMUM_KEY, EXCLUSIVE_MINIMUM_KEY
                )
            )


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
        MAX_ITEMS_KEY: 'maxItems',
        MIN_ITEMS_KEY: 'minItems',
        'unique_items': 'uniqueItems',
        # integer, number
        'multiple_of': 'multipleOf',
        MAXIMUM_KEY: 'maximum',
        EXCLUSIVE_MAXIMUM_KEY: 'exclusiveMaximum',
        MINIMUM_KEY: 'minimum',
        EXCLUSIVE_MINIMUM_KEY: 'exclusiveMinimum',
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
        max_items = kwargs.get(MAX_ITEMS_KEY, None)
        validate_max_items(max_items)

        min_items = kwargs.get(MIN_ITEMS_KEY, None)
        validate_min_items(min_items)

        maximum = kwargs.get(MAXIMUM_KEY, None)
        exclusive_maximum = kwargs.get(EXCLUSIVE_MAXIMUM_KEY, None)
        validate_maximum(maximum, exclusive_maximum)

        minimum = kwargs.get(MINIMUM_KEY, None)
        exclusive_minimum = kwargs.get(EXCLUSIVE_MINIMUM_KEY, None)
        validate_minimum(minimum, exclusive_minimum)

        self._optional = kwargs.pop('optional', False)
        schema = {}
        for field, field_name in self.FIELD_NAMES.items():
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
        if id:
            dict['id'] = id
        return dict

    def asjson(self, pretty=False):
        indent = 4 if pretty else None
        separators = (',', ': ') if pretty else (',', ':')
        return json.dumps(
            self.asdict(), sort_keys=True, indent=indent, separators=separators
        )


def uname():
    return uuid.uuid4().hex


def Properties(**kwargs):
    return kwargs


def Dependencies(**kwargs):
    return kwargs


class JSchemaMeta(type):
    def __call__(cls, *args, **kwargs):
        jschema = super(JSchemaMeta, cls).__call__(*args, **kwargs)
        return type(uname(), (object,), {'jschema': jschema})


class Array(JSchema, metaclass=JSchemaMeta):
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


class Boolean(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'boolean'
        super(Boolean, self).__init__(**kwargs)


class Integer(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'integer'
        super(Integer, self).__init__(**kwargs)


class Null(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'null'
        super(Null, self).__init__(**kwargs)


class Number(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'number'
        super(Number, self).__init__(**kwargs)


class Object(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        definitions = {}
        additional_properties = kwargs.get('additional_properties', None)
        if hasattr(additional_properties, 'jschema'):
            schema = additional_properties.jschema
            kwargs['additional_properties'] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        properties = kwargs.get('properties', {})
        for name in sorted(properties):
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
        for name, dependency in dependencies.items():
            if hasattr(dependency, 'jschema'):
                schema = dependency.jschema
                kwargs['dependencies'][name] = schema.asdict(root=False)
                for name in schema.definitions:
                    definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        kwargs['type'] = 'object'
        super(Object, self).__init__(**kwargs)


class String(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'string'
        super(String, self).__init__(**kwargs)


class Empty(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        definitions = {}
        all_of = kwargs.pop('all_of', [])
        for type in all_of:
            schema = type.jschema
            if 'all_of' not in kwargs:
                kwargs['all_of'] = []
            kwargs['all_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        any_of = kwargs.pop('any_of', [])
        for type in any_of:
            schema = type.jschema
            if 'any_of' not in kwargs:
                kwargs['any_of'] = []
            kwargs['any_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        one_of = kwargs.pop('one_of', [])
        for type in one_of:
            schema = type.jschema
            if 'one_of' not in kwargs:
                kwargs['one_of'] = []
            kwargs['one_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        super(Empty, self).__init__(**kwargs)

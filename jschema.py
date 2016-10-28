import json
import uuid


ADDITIONAL_ITEMS_KEY = 'additional_items'
ADDITIONAL_PROPERTIES_KEY = 'additional_properties'
ALL_OF_KEY = 'all_of'
ANY_OF_KEY = 'any_of'
DEFINITIONS_KEY = 'definitions'
DEPENDENCIES_KEY = 'dependencies'
ENUM_KEY = 'enum'
EXCLUSIVE_MAXIMUM_KEY = 'exclusive_maximum'
EXCLUSIVE_MINIMUM_KEY = 'exclusive_minimum'
ITEMS_KEY = 'items'
MAX_ITEMS_KEY = 'max_items'
MAX_LENGTH_KEY = 'max_length'
MAX_PROPERTIES_KEY = 'max_properties'
MAXIMUM_KEY = 'maximum'
MIN_ITEMS_KEY = 'min_items'
MIN_LENGTH_KEY = 'min_length'
MIN_PROPERTIES_KEY = 'min_properties'
MINIMUM_KEY = 'minimum'
MULTIPLE_OF_KEY = 'multiple_of'
NOT_KEY = 'not_'
ONE_OF_KEY = 'one_of'
PATTERN_KEY = 'pattern'
PATTERN_PROPERTIES_KEY = 'pattern_properties'
PROPERTIES_KEY = 'properties'
REQUIRED_KEY = 'required'
TYPE_KEY = 'type'
UNIQUE_ITEMS_KEY = 'unique_items'


def is_primitive_type_str(type_str):
    type_strs = [
        'array', 'boolean', 'integer', 'null', 'number', 'object', 'string'
    ]
    return type_str in type_strs


def is_primitive_type(type):
    types = (list, bool, int, float, dict, str)
    return type is None or isinstance(type, types)


def are_items_unique(items):
    for index, item in enumerate(items):
        for other_index, other_item in enumerate(items):
            if not other_index == index and other_item == item:
                return False
    return True


class SchemaValidationError(Exception):
    def __init__(self, key, message):
        super().__init__("'{0}' {1}".format(key, message))


def validate_is_bool_or_schema(key, value):
    if value is not None:
        if not isinstance(value, (bool, JSchema)):
            raise SchemaValidationError(key, "must be a bool or a schema")


def validate_is_schema_list(key, value):
    if value is not None:
        if not isinstance(value, list):
            raise SchemaValidationError(key, "must be a list")
        if not len(value) >= 1:
            raise SchemaValidationError(key, "list must not be empty")
        for item in value:
            if not isinstance(item, JSchema):
                raise SchemaValidationError(key, "list item must be a schema")


def validate_is_schema_dict(key, value):
    if value is not None:
        if not isinstance(value, dict):
            raise SchemaValidationError(key, "must be a dict")
        for k, v in value.items():
            if not isinstance(k, str):
                raise SchemaValidationError(key, "dict key must be a str")
            if not isinstance(v, JSchema):
                raise SchemaValidationError(key, "dict value must be a schema")


def validate_dependencies(dependencies):
    if dependencies is not None:
        if not isinstance(dependencies, dict):
            raise SchemaValidationError(DEPENDENCIES_KEY, "must be a dict")
        for key, value in dependencies.items():
            if not isinstance(key, str):
                raise SchemaValidationError(
                    DEPENDENCIES_KEY, "dict key must be a str"
                )
            if not isinstance(value, (JSchema, list)):
                raise SchemaValidationError(
                    DEPENDENCIES_KEY, "dict value must be a schema or a list"
                )
            if isinstance(value, list):
                if not len(value) >= 1:
                    raise SchemaValidationError(
                        DEPENDENCIES_KEY, "dict value list must not be empty"
                    )
                for item in value:
                    if not isinstance(item, str):
                        raise SchemaValidationError(
                            DEPENDENCIES_KEY,
                            "dict value list item must be a str"
                        )
                if not len(set(value)) == len(value):
                    raise SchemaValidationError(
                        DEPENDENCIES_KEY,
                        "dict value list item str must be unique"
                    )


def validate_enum(enum):
    if enum is not None:
        if not isinstance(enum, list):
            raise SchemaValidationError(ENUM_KEY, "must be a list")
        if not len(enum) >= 1:
            raise SchemaValidationError(ENUM_KEY, "list must not be empty")
        for item in enum:
            if not is_primitive_type(item):
                raise SchemaValidationError(
                    ENUM_KEY, "list item must be a primitive type"
                )
        if not are_items_unique(enum):
            raise SchemaValidationError(ENUM_KEY, "list item must be unique")


def validate_items(items):
    if items is not None:
        if not isinstance(items, (JSchema, list)):
            raise SchemaValidationError(
                ITEMS_KEY, "must be a schema or a list"
            )
        if isinstance(items, list):
            for item in items:
                if not isinstance(item, JSchema):
                    raise SchemaValidationError(
                        ITEMS_KEY, "list must contain only schemas"
                    )


def validate_is_positive_int_or_zero(key, value):
    if value is not None:
        if not isinstance(value, int):
            raise SchemaValidationError(key, "must be an int")
        if not value >= 0:
            raise SchemaValidationError(
                key, "must be greater than or equal to zero"
            )


def validate_maximum(maximum, exclusive_maximum):
    if maximum is not None:
        if not isinstance(maximum, (int, float)):
            raise SchemaValidationError(MAXIMUM_KEY, "must be an int or float")
    if exclusive_maximum is not None:
        if not isinstance(exclusive_maximum, bool):
            raise SchemaValidationError(
                EXCLUSIVE_MAXIMUM_KEY, "must be a bool"
            )
        if maximum is None:
            raise SchemaValidationError(
                MAXIMUM_KEY,
                "must be present if '{0}' is defined".format(
                    EXCLUSIVE_MAXIMUM_KEY
                )
            )


def validate_minimum(minimum, exclusive_minimum):
    if minimum is not None:
        if not isinstance(minimum, (int, float)):
            raise SchemaValidationError(MINIMUM_KEY, "must be an int or float")
    if exclusive_minimum is not None:
        if not isinstance(exclusive_minimum, bool):
            raise SchemaValidationError(
                EXCLUSIVE_MINIMUM_KEY, "must be a bool"
            )
        if minimum is None:
            raise SchemaValidationError(
                MINIMUM_KEY,
                "must be present if '{0}' is defined".format(
                    EXCLUSIVE_MINIMUM_KEY
                )
            )


def validate_multiple_of(multiple_of):
    if multiple_of is not None:
        if not isinstance(multiple_of, (int, float)):
            raise SchemaValidationError(
                MULTIPLE_OF_KEY, "must be an int or float"
            )
        if not multiple_of > 0:
            raise SchemaValidationError(
                MULTIPLE_OF_KEY, "must be greater than zero"
            )


def validate_not(not_):
    if not_ is not None:
        if not isinstance(not_, JSchema):
            raise SchemaValidationError(NOT_KEY, "must be a schema")


def validate_pattern(pattern):
    if pattern is not None:
        if not isinstance(pattern, str):
            raise SchemaValidationError(PATTERN_KEY, "must be a str")


def validate_required(required):
    if required is not None:
        if not isinstance(required, list):
            raise SchemaValidationError(REQUIRED_KEY, "must be a list")
        if not len(required) >= 1:
            raise SchemaValidationError(REQUIRED_KEY, "list must not be empty")
        for item in required:
            if not isinstance(item, str):
                raise SchemaValidationError(
                    REQUIRED_KEY, "list item must be a str"
                )
        if not len(set(required)) == len(required):
            raise SchemaValidationError(
                REQUIRED_KEY, "list item str must be unique"
            )


def validate_type(type):
    if type is not None:
        if not isinstance(type, (str, list)):
            raise SchemaValidationError(TYPE_KEY, "must be a str or a list")
        if isinstance(type, str):
            if not is_primitive_type_str(type):
                raise SchemaValidationError(
                    TYPE_KEY, "str must be a primitive type"
                )
        if isinstance(type, list):
            for item in type:
                if not isinstance(item, str):
                    raise SchemaValidationError(
                        TYPE_KEY, "list item must be a str"
                    )
                if not is_primitive_type_str(item):
                    raise SchemaValidationError(
                        TYPE_KEY, "list item str must be a primitive type"
                    )
            if not len(set(type)) == len(type):
                raise SchemaValidationError(
                    TYPE_KEY, "list item str must be unique"
                )


def validate_unique_items(unique_items):
    if unique_items is not None:
        if not isinstance(unique_items, bool):
            raise SchemaValidationError(UNIQUE_ITEMS_KEY, "must be a bool")


class JSchema(object):
    FIELD_NAMES = {
        # meta
        'schema': '$schema',
        'ref': '$ref',
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'default': 'default',
        # array
        ADDITIONAL_ITEMS_KEY: 'additionalItems',
        ITEMS_KEY: 'items',
        MAX_ITEMS_KEY: 'maxItems',
        MIN_ITEMS_KEY: 'minItems',
        UNIQUE_ITEMS_KEY: 'uniqueItems',
        # integer, number
        MULTIPLE_OF_KEY: 'multipleOf',
        MAXIMUM_KEY: 'maximum',
        EXCLUSIVE_MAXIMUM_KEY: 'exclusiveMaximum',
        MINIMUM_KEY: 'minimum',
        EXCLUSIVE_MINIMUM_KEY: 'exclusiveMinimum',
        # object
        MAX_PROPERTIES_KEY: 'maxProperties',
        MIN_PROPERTIES_KEY: 'minProperties',
        REQUIRED_KEY: 'required',
        ADDITIONAL_PROPERTIES_KEY: 'additionalProperties',
        PROPERTIES_KEY: 'properties',
        PATTERN_PROPERTIES_KEY: 'patternProperties',
        DEPENDENCIES_KEY: 'dependencies',
        # string
        MAX_LENGTH_KEY: 'maxLength',
        MIN_LENGTH_KEY: 'minLength',
        PATTERN_KEY: 'pattern',
        # all
        ENUM_KEY: 'enum',
        TYPE_KEY: 'type',
        ALL_OF_KEY: 'allOf',
        ANY_OF_KEY: 'anyOf',
        ONE_OF_KEY: 'oneOf',
        NOT_KEY: 'not',
        DEFINITIONS_KEY: 'definitions'
    }

    def __init__(self, **kwargs):
        additional_items = kwargs.get(ADDITIONAL_ITEMS_KEY, None)
        validate_is_bool_or_schema(ADDITIONAL_ITEMS_KEY, additional_items)

        additional_properties = kwargs.get(ADDITIONAL_PROPERTIES_KEY, None)
        validate_is_bool_or_schema(
            ADDITIONAL_PROPERTIES_KEY, additional_properties
        )

        all_of = kwargs.get(ALL_OF_KEY, None)
        validate_is_schema_list(ALL_OF_KEY, all_of)

        any_of = kwargs.get(ANY_OF_KEY, None)
        validate_is_schema_list(ANY_OF_KEY, any_of)

        definitions = kwargs.get(DEFINITIONS_KEY, None)
        validate_is_schema_dict(DEFINITIONS_KEY, definitions)

        dependencies = kwargs.get(DEPENDENCIES_KEY, None)
        validate_dependencies(dependencies)

        enum = kwargs.get(ENUM_KEY, None)
        validate_enum(enum)

        items = kwargs.get(ITEMS_KEY, None)
        validate_items(items)

        max_items = kwargs.get(MAX_ITEMS_KEY, None)
        validate_is_positive_int_or_zero(MAX_ITEMS_KEY, max_items)

        max_length = kwargs.get(MAX_LENGTH_KEY, None)
        validate_is_positive_int_or_zero(MAX_LENGTH_KEY, max_length)

        max_properties = kwargs.get(MAX_PROPERTIES_KEY, None)
        validate_is_positive_int_or_zero(MAX_PROPERTIES_KEY, max_properties)

        maximum = kwargs.get(MAXIMUM_KEY, None)
        exclusive_maximum = kwargs.get(EXCLUSIVE_MAXIMUM_KEY, None)
        validate_maximum(maximum, exclusive_maximum)

        min_items = kwargs.get(MIN_ITEMS_KEY, None)
        validate_is_positive_int_or_zero(MIN_ITEMS_KEY, min_items)

        min_length = kwargs.get(MIN_LENGTH_KEY, None)
        validate_is_positive_int_or_zero(MIN_LENGTH_KEY, min_length)

        min_properties = kwargs.get(MIN_PROPERTIES_KEY, None)
        validate_is_positive_int_or_zero(MIN_PROPERTIES_KEY, min_properties)

        minimum = kwargs.get(MINIMUM_KEY, None)
        exclusive_minimum = kwargs.get(EXCLUSIVE_MINIMUM_KEY, None)
        validate_minimum(minimum, exclusive_minimum)

        multiple_of = kwargs.get(MULTIPLE_OF_KEY, None)
        validate_multiple_of(multiple_of)

        not_ = kwargs.get(NOT_KEY, None)
        validate_not(not_)

        pattern = kwargs.get(PATTERN_KEY, None)
        validate_pattern(pattern)

        pattern_properties = kwargs.get(PATTERN_PROPERTIES_KEY, None)
        validate_is_schema_dict(PATTERN_PROPERTIES_KEY, pattern_properties)

        properties = kwargs.get(PROPERTIES_KEY, None)
        validate_is_schema_dict(PROPERTIES_KEY, properties)

        one_of = kwargs.get(ONE_OF_KEY, None)
        validate_is_schema_list(ONE_OF_KEY, one_of)

        required = kwargs.get(REQUIRED_KEY, None)
        validate_required(required)

        type = kwargs.get(TYPE_KEY, None)
        validate_type(type)

        unique_items = kwargs.get(UNIQUE_ITEMS_KEY, None)
        validate_unique_items(unique_items)

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

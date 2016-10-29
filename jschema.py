import json
import uuid


ADDITIONAL_ITEMS_KEY = 'additional_items'
ADDITIONAL_PROPERTIES_KEY = 'additional_properties'
ALL_OF_KEY = 'all_of'
ANY_OF_KEY = 'any_of'
DEFAULT_KEY = 'default'
DEFINITIONS_KEY = 'definitions'
DEPENDENCIES_KEY = 'dependencies'
DESCRIPTION_KEY = 'description'
ENUM_KEY = 'enum'
EXCLUSIVE_MAXIMUM_KEY = 'exclusive_maximum'
EXCLUSIVE_MINIMUM_KEY = 'exclusive_minimum'
ID_KEY = 'id'
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
REF_KEY = 'ref'
REQUIRED_KEY = 'required'
SCHEMA_KEY = 'schema'
TITLE_KEY = 'title'
TYPE_KEY = 'type'
UNIQUE_ITEMS_KEY = 'unique_items'


KEYWORDS = {
    ADDITIONAL_ITEMS_KEY: 'additionalItems',
    ADDITIONAL_PROPERTIES_KEY: 'additionalProperties',
    ALL_OF_KEY: 'allOf',
    ANY_OF_KEY: 'anyOf',
    DEFAULT_KEY: 'default',
    DEFINITIONS_KEY: 'definitions',
    DEPENDENCIES_KEY: 'dependencies',
    DESCRIPTION_KEY: 'description',
    ENUM_KEY: 'enum',
    EXCLUSIVE_MAXIMUM_KEY: 'exclusiveMaximum',
    EXCLUSIVE_MINIMUM_KEY: 'exclusiveMinimum',
    ID_KEY: 'id',
    ITEMS_KEY: 'items',
    MAX_ITEMS_KEY: 'maxItems',
    MAX_LENGTH_KEY: 'maxLength',
    MAX_PROPERTIES_KEY: 'maxProperties',
    MAXIMUM_KEY: 'maximum',
    MIN_ITEMS_KEY: 'minItems',
    MIN_LENGTH_KEY: 'minLength',
    MIN_PROPERTIES_KEY: 'minProperties',
    MINIMUM_KEY: 'minimum',
    MULTIPLE_OF_KEY: 'multipleOf',
    NOT_KEY: 'not',
    ONE_OF_KEY: 'oneOf',
    PATTERN_KEY: 'pattern',
    PATTERN_PROPERTIES_KEY: 'patternProperties',
    PROPERTIES_KEY: 'properties',
    REF_KEY: '$ref',
    REQUIRED_KEY: 'required',
    SCHEMA_KEY: '$schema',
    TITLE_KEY: 'title',
    TYPE_KEY: 'type',
    UNIQUE_ITEMS_KEY: 'uniqueItems'
}


SCHEMA_VALIDATION_FUNCTIONS = {
    ADDITIONAL_ITEMS_KEY:
        lambda kwargs:
            validate_is_bool_or_schema(ADDITIONAL_ITEMS_KEY, kwargs),
    ADDITIONAL_PROPERTIES_KEY:
        lambda kwargs:
            validate_is_bool_or_schema(ADDITIONAL_PROPERTIES_KEY, kwargs),
    ALL_OF_KEY: lambda kwargs: validate_is_schema_list(ALL_OF_KEY, kwargs),
    ANY_OF_KEY: lambda kwargs: validate_is_schema_list(ANY_OF_KEY, kwargs),
    DEFAULT_KEY: lambda kwargs: validate_default(kwargs),
    DEFINITIONS_KEY:
        lambda kwargs: validate_is_schema_dict(DEFINITIONS_KEY, kwargs),
    DEPENDENCIES_KEY: lambda kwargs: validate_dependencies(kwargs),
    DESCRIPTION_KEY: lambda kwargs: validate_is_str(DESCRIPTION_KEY, kwargs),
    ENUM_KEY: lambda kwargs: validate_enum(kwargs),
    EXCLUSIVE_MAXIMUM_KEY: lambda kwargs: validate_maximum(kwargs),
    EXCLUSIVE_MINIMUM_KEY: lambda kwargs: validate_minimum(kwargs),
    ID_KEY: lambda kwargs: validate_is_str(ID_KEY, kwargs),
    ITEMS_KEY: lambda kwargs: validate_items(kwargs),
    MAX_ITEMS_KEY:
        lambda kwargs: validate_is_positive_int_or_zero(MAX_ITEMS_KEY, kwargs),
    MAX_LENGTH_KEY:
        lambda kwargs:
            validate_is_positive_int_or_zero(MAX_LENGTH_KEY, kwargs),
    MAX_PROPERTIES_KEY:
        lambda kwargs:
            validate_is_positive_int_or_zero(MAX_PROPERTIES_KEY, kwargs),
    MAXIMUM_KEY: lambda kwargs: validate_maximum(kwargs),
    MIN_ITEMS_KEY:
        lambda kwargs: validate_is_positive_int_or_zero(MIN_ITEMS_KEY, kwargs),
    MIN_LENGTH_KEY:
        lambda kwargs:
            validate_is_positive_int_or_zero(MIN_LENGTH_KEY, kwargs),
    MIN_PROPERTIES_KEY:
        lambda kwargs:
            validate_is_positive_int_or_zero(MIN_PROPERTIES_KEY, kwargs),
    MINIMUM_KEY: lambda kwargs: validate_minimum(kwargs),
    MULTIPLE_OF_KEY: lambda kwargs: validate_multiple_of(kwargs),
    NOT_KEY: lambda kwargs: validate_not(kwargs),
    ONE_OF_KEY: lambda kwargs: validate_is_schema_list(ONE_OF_KEY, kwargs),
    PATTERN_KEY: lambda kwargs: validate_is_str(PATTERN_KEY, kwargs),
    PATTERN_PROPERTIES_KEY:
        lambda kwargs: validate_is_schema_dict(PATTERN_PROPERTIES_KEY, kwargs),
    PROPERTIES_KEY:
        lambda kwargs: validate_is_schema_dict(PROPERTIES_KEY, kwargs),
    REF_KEY: lambda kwargs: validate_is_str(REF_KEY, kwargs),
    REQUIRED_KEY: lambda kwargs: validate_required(kwargs),
    SCHEMA_KEY: lambda kwargs: None,
    TITLE_KEY: lambda kwargs: validate_is_str(TITLE_KEY, kwargs),
    TYPE_KEY: lambda kwargs: validate_type(kwargs),
    UNIQUE_ITEMS_KEY: lambda kwargs: validate_unique_items(kwargs)
}


def is_primitive_type_str(type_str):
    type_strs = [
        'array', 'boolean', 'integer', 'null', 'number', 'object', 'string'
    ]
    return type_str in type_strs


def is_primitive_type(type):
    types = (list, bool, int, float, dict, str)
    if type is not None and not isinstance(type, types):
        return False
    if isinstance(type, list):
        for item in type:
            if not is_primitive_type(item):
                return False
    if isinstance(type, dict):
        for key, value in type.items():
            if not is_primitive_type(key):
                return False
            if not is_primitive_type(value):
                return False
    return True


def are_items_unique(items):
    for index, item in enumerate(items):
        for other_index, other_item in enumerate(items):
            if not other_index == index and other_item == item:
                return False
    return True


class SchemaValidationError(Exception):
    def __init__(self, key, message):
        super().__init__("'{0}' {1}".format(key, message))


def validate_is_str(key, kwargs):
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, str):
            raise SchemaValidationError(key, "must be a str")


def validate_is_bool_or_schema(key, kwargs):
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, (bool, JSchema)):
            raise SchemaValidationError(key, "must be a bool or a schema")


def validate_is_schema_list(key, kwargs):
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, list):
            raise SchemaValidationError(key, "must be a list")
        if not len(value) >= 1:
            raise SchemaValidationError(key, "list must not be empty")
        for item in value:
            if not isinstance(item, JSchema):
                raise SchemaValidationError(key, "list item must be a schema")


def validate_is_schema_dict(key, kwargs):
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, dict):
            raise SchemaValidationError(key, "must be a dict")
        for k, v in value.items():
            if not isinstance(k, str):
                raise SchemaValidationError(key, "dict key must be a str")
            if not isinstance(v, JSchema):
                raise SchemaValidationError(key, "dict value must be a schema")


def validate_default(kwargs):
    key = DEFAULT_KEY
    value = kwargs.get(key, None)
    if not is_primitive_type(value):
        raise SchemaValidationError(key, "must be a primitive type")


def validate_dependencies(kwargs):
    key = DEPENDENCIES_KEY
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, dict):
            raise SchemaValidationError(key, "must be a dict")
        for k, v in value.items():
            if not isinstance(k, str):
                raise SchemaValidationError(key, "dict key must be a str")
            if not isinstance(v, (JSchema, list)):
                raise SchemaValidationError(
                    key, "dict value must be a schema or a list"
                )
            if isinstance(v, list):
                if not len(v) >= 1:
                    raise SchemaValidationError(
                        key, "dict value list must not be empty"
                    )
                for item in v:
                    if not isinstance(item, str):
                        raise SchemaValidationError(
                            key, "dict value list item must be a str"
                        )
                if not len(set(v)) == len(v):
                    raise SchemaValidationError(
                        key, "dict value list item str must be unique"
                    )


def validate_enum(kwargs):
    key = ENUM_KEY
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, list):
            raise SchemaValidationError(key, "must be a list")
        if not len(value) >= 1:
            raise SchemaValidationError(key, "list must not be empty")
        for item in value:
            if not is_primitive_type(item):
                raise SchemaValidationError(
                    key, "list item must be a primitive type"
                )
        if not are_items_unique(value):
            raise SchemaValidationError(key, "list item must be unique")


def validate_items(kwargs):
    key = ITEMS_KEY
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, (JSchema, list)):
            raise SchemaValidationError(key, "must be a schema or a list")
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, JSchema):
                    raise SchemaValidationError(
                        key, "list must contain only schemas"
                    )


def validate_is_positive_int_or_zero(key, kwargs):
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, int):
            raise SchemaValidationError(key, "must be an int")
        if not value >= 0:
            raise SchemaValidationError(
                key, "must be greater than or equal to zero"
            )


def validate_maximum(kwargs):
    maximum = kwargs.get(MAXIMUM_KEY, None)
    exclusive_maximum = kwargs.get(EXCLUSIVE_MAXIMUM_KEY, None)
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


def validate_minimum(kwargs):
    minimum = kwargs.get(MINIMUM_KEY, None)
    exclusive_minimum = kwargs.get(EXCLUSIVE_MINIMUM_KEY, None)
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


def validate_multiple_of(kwargs):
    key = MULTIPLE_OF_KEY
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, (int, float)):
            raise SchemaValidationError(key, "must be an int or float")
        if not value > 0:
            raise SchemaValidationError(key, "must be greater than zero")


def validate_not(kwargs):
    key = NOT_KEY
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, JSchema):
            raise SchemaValidationError(key, "must be a schema")


def validate_required(kwargs):
    key = REQUIRED_KEY
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, list):
            raise SchemaValidationError(key, "must be a list")
        if not len(value) >= 1:
            raise SchemaValidationError(key, "list must not be empty")
        for item in value:
            if not isinstance(item, str):
                raise SchemaValidationError(key, "list item must be a str")
        if not len(set(value)) == len(value):
            raise SchemaValidationError(key, "list item str must be unique")


def validate_type(kwargs):
    key = TYPE_KEY
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, (str, list)):
            raise SchemaValidationError(key, "must be a str or a list")
        if isinstance(value, str):
            if not is_primitive_type_str(value):
                raise SchemaValidationError(
                    key, "str must be a primitive type"
                )
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, str):
                    raise SchemaValidationError(key, "list item must be a str")
                if not is_primitive_type_str(item):
                    raise SchemaValidationError(
                        key, "list item str must be a primitive type"
                    )
            if not len(set(value)) == len(value):
                raise SchemaValidationError(
                    key, "list item str must be unique"
                )


def validate_unique_items(kwargs):
    key = UNIQUE_ITEMS_KEY
    value = kwargs.get(key, None)
    if value is not None:
        if not isinstance(value, bool):
            raise SchemaValidationError(key, "must be a bool")


class JSchema(object):
    def __init__(self, **kwargs):
        self._dict = {}
        for key, keyword in KEYWORDS.items():
            validate_keyword = SCHEMA_VALIDATION_FUNCTIONS[key]
            validate_keyword(kwargs)
            if key in kwargs:
                self._dict[keyword] = kwargs[key]

    def asdict(self, root=False, schema=None):
        dict = self._dict.copy()
        if root:
            validate_is_str(SCHEMA_KEY, {'schema': schema})
            dict[KEYWORDS['schema']] = (
                'http://json-schema.org/draft-04/schema#' if schema is None
                else schema
            )
        return dict

    def asjson(self, pretty=False, root=False, schema=None):
        dict = self.asdict(root, schema)
        indent = 4 if pretty else None
        separators = (',', ': ') if pretty else (',', ':')
        return json.dumps(
            dict, sort_keys=True, indent=indent, separators=separators
        )


def uname():
    return uuid.uuid4().hex


class JSchemaMeta(type):
    def __call__(cls, *args, **kwargs):
        jschema = super(JSchemaMeta, cls).__call__(*args, **kwargs)
        return type(uname(), (object,), {'jschema': jschema})

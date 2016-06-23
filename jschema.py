import json
import re


class Schema(dict):
    def __init__(self, *args, **kwargs):
        super(Schema, self).__init__(*args, **kwargs)

    def asjson(self, pretty=False):
        indent = 4 if pretty else None
        separators = (',', ': ') if pretty else None
        return json.dumps(
            self, sort_keys=True, indent=indent, separators=separators
        )


class SchemaProp(property):
    def __init__(self, type, prop_names={}, **kwargs):
        self.name = None
        self.jschema = Schema({'type': type})
        for def_name, schema_name in prop_names.iteritems():
            value = kwargs.pop(def_name, None)
            setattr(self, def_name, value)
            if value is not None:
                self.jschema[schema_name] = value
        super(SchemaProp, self).__init__(fget=self.getprop, fset=self.setprop)

    def getprop(self, obj):
        return getattr(obj, self.name, None)

    def setprop(self, obj, value):
        self.validate(value)
        setattr(obj, self.name, value)

    def validate(self, value):
        raise NotImplementedError()

    def raise_validation_error(self, type, value, *args):
        raise JsonSchemaValidationError(
            type, value, *[(key, getattr(self, key)) for key in args]
        )


class Object(SchemaProp):
    TYPE = 'object'
    SCHEMA_PROPS = {
        'max_properties': 'maxProperties',
        'min_properties': 'minProperties'
    }

    def __init__(self, cls):
        schema_props = [
            (key, value) for key, value in cls.__dict__.iteritems()
            if key in self.SCHEMA_PROPS
        ]
        super(Object, self).__init__(
            self.TYPE, self.SCHEMA_PROPS, **dict(schema_props)
        )
        self.validate_max_properties_definition()
        self.validate_min_properties_definition()
        props = [
            (key, val) for key, val in cls.__dict__.iteritems()
            if isinstance(val, SchemaProp)
        ]
        if props:
            self.jschema['properties'] = {}
        for name, prop in props:
            self.jschema['properties'][name] = prop.jschema

    def validate_max_properties_definition(self):
        if self.max_properties is not None:
            if not isinstance(self.max_properties, int):
                raise JsonSchemaDefinitionError(
                    'max_properties must be int', self.max_properties
                )
            if not self.max_properties >= 0:
                raise JsonSchemaDefinitionError(
                    'max_properties must be >= 0', self.max_properties
                )

    def validate_min_properties_definition(self):
        if self.min_properties is not None:
            if not isinstance(self.min_properties, int):
                raise JsonSchemaDefinitionError(
                    'min_properties must be int', self.min_properties
                )
            if not self.min_properties >= 0:
                raise JsonSchemaDefinitionError(
                    'min_properties must be >= 0', self.min_properties
                )

    def validate(self, value):
        pass


class String(SchemaProp):
    TYPE = 'string'
    SCHEMA_PROPS = {
        'max_length': 'maxLength',
        'min_length': 'minLength',
        'pattern': 'pattern'
    }

    def __init__(self, **kwargs):
        super(String, self).__init__(self.TYPE, self.SCHEMA_PROPS, **kwargs)
        self.validate_max_length_definition()
        self.validate_min_length_definition()

    def validate_max_length_definition(self):
        if self.max_length is not None:
            if not isinstance(self.max_length, int):
                raise JsonSchemaDefinitionError(
                    'max_length must be int', self.max_length
                )
            if not self.max_length >= 0:
                raise JsonSchemaDefinitionError(
                    'max_length must be >= 0', self.max_length
                )

    def validate_min_length_definition(self):
        if self.min_length is not None:
            if not isinstance(self.min_length, int):
                raise JsonSchemaDefinitionError(
                    'min_length must be int', self.min_length
                )
            if not self.min_length >= 0:
                raise JsonSchemaDefinitionError(
                    'min_length must be >= 0', self.min_length
                )

    def validate(self, value):
        if not isinstance(value, str):
            self.raise_validation_error(self.TYPE, value)
        if self.max_length is not None and len(value) > self.max_length:
            self.raise_validation_error(self.TYPE, value, 'max_length')
        if self.min_length is not None and len(value) < self.min_length:
            self.raise_validation_error(self.TYPE, value, 'min_length')
        if self.pattern is not None and re.match(self.pattern, value) is None:
            self.raise_validation_error(self.TYPE, value, 'pattern')


class Integer(SchemaProp):
    TYPE = 'integer'
    SCHEMA_PROPS = {
        'exclusive_maximum': 'exclusiveMaximum',
        'exclusive_minimum': 'exclusiveMinimum',
        'maximum': 'maximum',
        'minimum': 'minimum',
        'multiple_of': 'multipleOf'
    }

    def __init__(self, **kwargs):
        super(Integer, self).__init__(self.TYPE, self.SCHEMA_PROPS, **kwargs)

    def validate(self, value):
        if not isinstance(value, int):
            self.raise_validation_error(self.TYPE, value)
        if self.multiple_of is not None and not value % self.multiple_of == 0:
            self.raise_validation_error(self.TYPE, value, 'multiple_of')
        if self.maximum is not None:
            if self.exclusive_maximum and value >= self.maximum:
                self.raise_validation_error(
                    self.TYPE, value, 'maximum', 'exclusive_maximum'
                )
            if value > self.maximum:
                self.raise_validation_error(self.TYPE, value, 'maximum')
        if self.minimum is not None:
            if self.exclusive_minimum and value <= self.minimum:
                self.raise_validation_error(
                    self.TYPE, value, 'minimum', 'exclusive_minimum'
                )
            if value < self.minimum:
                self.raise_validation_error(self.TYPE, value, 'minimum')


class JsonSchemaValidationError(Exception):
    def __init__(self, type, value, *args):
        super(JsonSchemaValidationError, self).__init__(
            'invalid {0}{1}: {2}'.format(
                type,
                '' if not args else ' [{0}]'.format(
                    ', '.join(
                        ['{0}={1}'.format(key, repr(val)) for key, val in args]
                    )
                ),
                repr(value)
            )
        )


class JsonSchemaDefinitionError(Exception):
    def __init__(self, reason, value):
        super(JsonSchemaDefinitionError, self).__init__(
            'invalid definition [{0}]: {1}'.format(reason, repr(value))
        )


class ClassMeta(type):
    def __init__(cls, name, bases, dict):
        for key, value in dict.iteritems():
            if isinstance(value, SchemaProp):
                value.name = '_' + key
        cls.jschema = Object(cls).jschema
        super(ClassMeta, cls).__init__(name, bases, dict)


class Class(object):
    __metaclass__ = ClassMeta

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

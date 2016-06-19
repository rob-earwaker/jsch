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


class SchemaAttr(property):
    def __init__(self, type, **kwargs):
        self.name = None
        self.jschema = Schema({'type': type})
        super(SchemaAttr, self).__init__(fget=self.getprop, fset=self.setprop)

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


class Object(SchemaAttr):
    TYPE = 'object'

    def __init__(self, cls):
        kwargs = {}
        self.max_properties = getattr(cls, 'max_properties', None)
        super(Object, self).__init__(self.TYPE, **kwargs)
        if self.max_properties is not None:
            self.jschema['maxProperties'] = self.max_properties
        attrs = [
            (key, value) for key, value in cls.__dict__.iteritems()
            if isinstance(value, SchemaAttr)
        ]
        if attrs:
            self.jschema['properties'] = {}
        for key, value in attrs:
            self.jschema['properties'][key] = value.jschema


class String(SchemaAttr):
    TYPE = 'string'

    def __init__(self, **kwargs):
        self.max_length = kwargs.pop('max_length', None)
        self.min_length = kwargs.pop('min_length', None)
        self.pattern = kwargs.pop('pattern', None)
        super(String, self).__init__(self.TYPE, **kwargs)
        if self.max_length is not None:
            self.jschema['maxLength'] = self.max_length
        if self.min_length is not None:
            self.jschema['minLength'] = self.min_length
        if self.pattern is not None:
            self.jschema['pattern'] = self.pattern

    def validate(self, value):
        if not isinstance(value, str):
            self.raise_validation_error(self.TYPE, value)
        if self.max_length is not None and len(value) > self.max_length:
            self.raise_validation_error(self.TYPE, value, 'max_length')
        if self.min_length is not None and len(value) < self.min_length:
            self.raise_validation_error(self.TYPE, value, 'min_length')
        if self.pattern is not None and re.match(self.pattern, value) is None:
            self.raise_validation_error(self.TYPE, value, 'pattern')


class Integer(SchemaAttr):
    TYPE = 'integer'

    def __init__(self, **kwargs):
        self.exclusive_maximum = kwargs.pop('exclusive_maximum', None)
        self.maximum = kwargs.pop('maximum', None)
        self.multiple_of = kwargs.pop('multiple_of', None)
        super(Integer, self).__init__(self.TYPE, **kwargs)
        if self.exclusive_maximum is not None:
            self.jschema['exclusiveMaximum'] = self.exclusive_maximum
        if self.maximum is not None:
            self.jschema['maximum'] = self.maximum
        if self.multiple_of is not None:
            self.jschema['multipleOf'] = self.multiple_of

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


class ClassMeta(type):
    def __init__(cls, name, bases, dict):
        for key, value in dict.iteritems():
            if isinstance(value, SchemaAttr):
                value.name = '_' + key
        cls.jschema = Object(cls).jschema
        super(ClassMeta, cls).__init__(name, bases, dict)


class Class(object):
    __metaclass__ = ClassMeta

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

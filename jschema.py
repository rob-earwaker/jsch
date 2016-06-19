"""
>>> import jschema

>>> class Greeting(jschema.Class):
...     max_properties = 1
...     name = jschema.String(
...         max_length=10,
...         min_length=1,
...         pattern='^W'
...     )

>>> print Greeting.jschema.asjson(pretty=True)
{
    "maxProperties": 1,
    "properties": {
        "name": {
            "maxLength": 10,
            "minLength": 1,
            "pattern": "^W",
            "type": "string"
        }
    },
    "type": "object"
}

"""
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


class Object(SchemaAttr):
    def __init__(self, cls):
        kwargs = {}
        self.max_properties = getattr(cls, 'max_properties', None)
        super(Object, self).__init__('object', **kwargs)
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
    def __init__(self, **kwargs):
        self.max_length = kwargs.pop('max_length', None)
        self.min_length = kwargs.pop('min_length', None)
        self.pattern = kwargs.pop('pattern', None)
        super(String, self).__init__('string', **kwargs)
        if self.max_length is not None:
            self.jschema['maxLength'] = self.max_length
        if self.min_length is not None:
            self.jschema['minLength'] = self.min_length
        if self.pattern is not None:
            self.jschema['pattern'] = self.pattern

    def validate(self, value):
        if not isinstance(value, str):
            raise JsonSchemaValidationError(
                'invalid string: {0}'.format(repr(value))
            )
        if self.max_length is not None and len(value) > self.max_length:
            raise JsonSchemaValidationError(
                'invalid string [max_length={0}]: {1}'.format(
                    repr(self.max_length), repr(value)
                )
            )
        if self.min_length is not None and len(value) < self.min_length:
            raise JsonSchemaValidationError(
                'invalid string [min_length={0}]: {1}'.format(
                    repr(self.min_length), repr(value)
                )
            )
        if self.pattern is not None and re.match(self.pattern, value) is None:
            raise JsonSchemaValidationError(
                'invalid string [pattern={0}]: {1}'.format(
                    repr(self.pattern), repr(value)
                )
            )


class Integer(SchemaAttr):
    def __init__(self, **kwargs):
        self.multiple_of = kwargs.pop('multiple_of', None)
        super(Integer, self).__init__('integer', **kwargs)
        if self.multiple_of is not None:
            self.jschema['multipleOf'] = self.multiple_of

    def validate(self, value):
        if not isinstance(value, int):
            raise JsonSchemaValidationError(
                'invalid integer: {0}'.format(repr(value))
            )
        if self.multiple_of is not None and not value % self.multiple_of == 0:
            raise JsonSchemaValidationError(
                'invalid integer [multiple_of=7]: {0}'.format(repr(value))
            )


class JsonSchemaValidationError(Exception):
    pass


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

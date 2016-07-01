import uuid


def uname():
    return uuid.uuid4().get_hex()


class JSchema(object):
    def __init__(self, type, **kwargs):
        self._dict = {'type': type}
        id = kwargs.get('id', None)
        if id is not None:
            self._dict['id'] = id
        title = kwargs.get('title', None)
        if title is not None:
            self._dict['title'] = title
        description = kwargs.get('description', None)
        if description is not None:
            self._dict['description'] = description
        schema = kwargs.get('schema', None)
        if schema is not None:
            self._dict['$schema'] = schema
        default = kwargs.get('default', None)
        if default is not None:
            self._dict['default'] = default

    @classmethod
    def array(cls, **kwargs):
        return cls('array', **kwargs)

    @classmethod
    def boolean(cls, **kwargs):
        return cls('boolean', **kwargs)

    @classmethod
    def integer(cls, **kwargs):
        return cls('integer', **kwargs)

    @classmethod
    def null(cls, **kwargs):
        return cls('null', **kwargs)

    @classmethod
    def number(cls, **kwargs):
        return cls('number', **kwargs)

    @classmethod
    def object(cls, **kwargs):
        return cls('object', **kwargs)

    @classmethod
    def string(cls, **kwargs):
        return cls('string', **kwargs)

    def asdict(self):
        return self._dict


def Array(**kwargs):
    return type(uname(), (object,), {'jschema': JSchema.array(**kwargs)})


def Boolean(**kwargs):
    return type(uname(), (object,), {'jschema': JSchema.boolean(**kwargs)})


def Integer(**kwargs):
    return type(uname(), (object,), {'jschema': JSchema.integer(**kwargs)})


def Null(**kwargs):
    return type(uname(), (object,), {'jschema': JSchema.null(**kwargs)})


def Number(**kwargs):
    return type(uname(), (object,), {'jschema': JSchema.number(**kwargs)})


def Object(**kwargs):
    return type(uname(), (object,), {'jschema': JSchema.object(**kwargs)})


def String(**kwargs):
    return type(uname(), (object,), {'jschema': JSchema.string(**kwargs)})

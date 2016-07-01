import uuid


def uname():
    return uuid.uuid4().get_hex()


class JSchema(object):
    def __init__(self, **kwargs):
        self._dict = {'type': kwargs['type']}
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

    def asdict(self):
        return self._dict


def Array(id=None, title=None, description=None, schema=None, default=None):
    jschema = JSchema(
        type='array',
        id=id,
        title=title,
        description=description,
        schema=schema,
        default=default
    )
    return type(uname(), (object,), {'jschema': jschema})


def Boolean(id=None, title=None, description=None, schema=None, default=None):
    jschema = JSchema(
        type='boolean',
        id=id,
        title=title,
        description=description,
        schema=schema,
        default=default
    )
    return type(uname(), (object,), {'jschema': jschema})


def Integer(id=None):
    jschema = JSchema(
        type='integer', id=id, title=None, description=None, schema=None
    )
    return type(uname(), (object,), {'jschema': jschema})


def Null(id=None):
    jschema = JSchema(
        type='null', id=id, title=None, description=None, schema=None
    )
    return type(uname(), (object,), {'jschema': jschema})


def Number(id=None):
    jschema = JSchema(
        type='number', id=id, title=None, description=None, schema=None
    )
    return type(uname(), (object,), {'jschema': jschema})


def Object(id=None):
    jschema = JSchema(
        type='object', id=id, title=None, description=None, schema=None
    )
    return type(uname(), (object,), {'jschema': jschema})


def String(id=None):
    jschema = JSchema(
        type='string', id=id, title=None, description=None, schema=None
    )
    return type(uname(), (object,), {'jschema': jschema})

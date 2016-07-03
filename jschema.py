import uuid


def uname():
    return uuid.uuid4().get_hex()


class JSchema(object):
    FIELD_NAMES = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'schema': '$schema',
        'default': 'default',
        'additional_items': 'additionalItems',
        'items': 'items',
        'max_items': 'maxItems',
        'min_items': 'minItems',
        'unique_items': 'uniqueItems'
    }

    def __init__(self, type, **kwargs):
        self._dict = {'type': type}
        if 'additional_items' in kwargs:
            additional_items = kwargs['additional_items']
            if hasattr(additional_items, 'jschema'):
                kwargs['additional_items'] = additional_items.jschema.asdict()
        if 'items' in kwargs:
            items = kwargs['items']
            if isinstance(items, list):
                kwargs['items'] = [item.jschema.asdict() for item in items]
            if hasattr(items, 'jschema'):
                kwargs['items'] = items.jschema.asdict()
        for field in self.FIELD_NAMES:
            if field in kwargs:
                self._dict[self.FIELD_NAMES[field]] = kwargs[field]

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

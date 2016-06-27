class JSchema(object):
    PROPS = {
        'default': 'default',
        'description': 'description',
        'id': 'id',
        'properties': 'properties',
        'schema': '$schema',
        'type': 'type',
        'title': 'title'
    }

    def __init__(self, **kwargs):
        for prop in self.PROPS:
            setattr(self, prop, kwargs.get(prop, None))

    def __call__(self):
        schema = {}
        for prop in self.PROPS:
            if getattr(self, prop, None) is not None:
                schema[self.PROPS[prop]] = getattr(self, prop)
        return schema


class ObjectMeta(type):
    def __init__(cls, name, bases, dict):
        props = {}
        for prop in dict:
            if hasattr(dict[prop], 'jschema'):
                props[prop] = dict[prop].jschema()
        cls.jschema = JSchema(**{'properties': props})
        super(ObjectMeta, cls).__init__(name, bases, dict)


class Object(object):
    __metaclass__ = ObjectMeta


class Boolean(Object):
    def __init__(self, **kwargs):
        kwargs['type'] = 'boolean'
        self.jschema = JSchema(**kwargs)

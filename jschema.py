import uuid


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
        'unique_items': 'uniqueItems',
        'multiple_of': 'multipleOf',
        'maximum': 'maximum',
        'exclusive_maximum': 'exclusiveMaximum',
        'minimum': 'minimum',
        'exclusive_minimum': 'exclusiveMinimum',
        'max_properties': 'maxProperties',
        'min_properties': 'minProperties',
        'required': 'required',
        'additional_properties': 'additionalProperties',
        'properties': 'properties',
        'pattern_properties': 'patternProperties',
        'dependencies': 'dependencies',
        'max_length': 'maxLength',
        'min_length': 'minLength',
        'pattern': 'pattern',
        'definitions': 'definitions'
    }

    def __init__(self, type, **kwargs):
        if 'additional_items' in kwargs:
            additional_items = kwargs['additional_items']
            if hasattr(additional_items, 'jschema'):
                kwargs['additional_items'] = additional_items.jschema.asdict()
        if 'items' in kwargs:
            items = kwargs['items']
            if isinstance(items, list):
                kwargs['items'] = [item.jschema.asdict() for item in items]
            if hasattr(items, 'jschema'):
                ref = items.jschema.ref
                if ref is not None:
                    kwargs['items'] = {
                        '$ref': '#/definitions/{0}'.format(ref)
                    }
                    if 'definitions' not in kwargs:
                        kwargs['definitions'] = {}
                    kwargs['definitions'][ref] = items.jschema.asdict()
                else:
                    kwargs['items'] = items.jschema.asdict()
        if 'additional_properties' in kwargs:
            additional_properties = kwargs['additional_properties']
            if hasattr(additional_properties, 'jschema'):
                kwargs['additional_properties'] = \
                    additional_properties.jschema.asdict()
        if 'properties' in kwargs:
            properties = kwargs['properties']
            for property_name in properties:
                property_schema = properties[property_name].jschema.asdict()
                kwargs['properties'][property_name] = property_schema
                if property_schema.pop('required', False):
                    if 'required' not in kwargs:
                        kwargs['required'] = []
                    kwargs['required'].append(property_name)
        if 'pattern_properties' in kwargs:
            pattern_properties = kwargs['pattern_properties']
            for property_name in pattern_properties:
                kwargs['pattern_properties'][property_name] = \
                    pattern_properties[property_name].jschema.asdict()
        if 'dependencies' in kwargs:
            for name in kwargs['dependencies']:
                dependency = kwargs['dependencies'][name]
                if hasattr(dependency, 'jschema'):
                    kwargs['dependencies'][name] = dependency.jschema.asdict()
        self._ref = kwargs.pop('ref', None)
        self._dict = {'type': type}
        for field in self.FIELD_NAMES:
            if field in kwargs:
                self._dict[self.FIELD_NAMES[field]] = kwargs[field]

    @property
    def ref(self):
        return self._ref

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


def uname():
    return uuid.uuid4().get_hex()


class JSchemaDefinitionError(Exception):
    pass


def Properties(**kwargs):
    return kwargs


def Dependencies(**kwargs):
    return kwargs


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

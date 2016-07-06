import unittest

import jschema


class TestArray(unittest.TestCase):
    """
    enum                    # all
    not                     # all

    """
    def test_type_field(self):
        Siblings = jschema.Array()
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Array().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'id': 'http://py.jschema/schemas/',
            'type': 'array'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Siblings = jschema.Array(title='Siblings')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'title': 'Siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_description_field(self):
        Siblings = jschema.Array(description='List of siblings')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'description': 'List of siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_default_field(self):
        Siblings = jschema.Array(default=[])
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'default': [],
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_additional_items_field_as_boolean(self):
        Siblings = jschema.Array(additional_items=True)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'additionalItems': True,
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_additional_items_field_as_object(self):
        Siblings = jschema.Array(additional_items=jschema.Object())
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'additionalItems': {'type': 'object'},
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_additional_items_field_as_object_with_ref(self):
        Siblings = jschema.Array(
            additional_items=jschema.Object(ref='sibling')
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'sibling': {'type': 'object'}},
            'additionalItems': {'$ref': '#/definitions/sibling'},
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_additional_items_field_as_object_with_refs(self):
        Siblings = jschema.Array(
            additional_items=jschema.Object(ref='otherSibling'),
            items=jschema.Object(ref='sibling')
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'sibling': {'type': 'object'},
                'otherSibling': {'type': 'object'}
            },
            'items': {'$ref': '#/definitions/sibling'},
            'additionalItems': {'$ref': '#/definitions/otherSibling'},
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_additional_items_field_as_object_with_nested_ref(self):
        Siblings = jschema.Array(
            additional_items=jschema.Object(
                ref='sibling',
                properties=jschema.Properties(hat=jschema.Object(ref='hat'))
            )
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'sibling': {
                    'properties': {'hat': {'$ref': '#/definitions/hat'}},
                    'required': ['hat'],
                    'type': 'object'
                },
                'hat': {'type': 'object'}
            },
            'additionalItems': {'$ref': '#/definitions/sibling'},
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_array(self):
        Siblings = jschema.Array(items=[jschema.Object(), jschema.Null()])
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'items': [{'type': 'object'}, {'type': 'null'}],
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_array_with_ref(self):
        Siblings = jschema.Array(
            items=[jschema.Object(ref='sibling'), jschema.Null()]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'sibling': {'type': 'object'}},
            'items': [{'$ref': '#/definitions/sibling'}, {'type': 'null'}],
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_array_with_refs(self):
        Siblings = jschema.Array(
            items=[
                jschema.Object(ref='sibling'),
                jschema.Null(ref='unknownSibling')
            ]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'sibling': {'type': 'object'},
                'unknownSibling': {'type': 'null'}
            },
            'items': [
                {'$ref': '#/definitions/sibling'},
                {'$ref': '#/definitions/unknownSibling'}
            ],
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_array_with_nested_ref(self):
        Siblings = jschema.Array(
            items=[
                jschema.Object(
                    ref='sibling',
                    properties=jschema.Properties(
                        hat=jschema.Object(ref='hat')
                    )
                ),
                jschema.Null()
            ]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'sibling': {
                    'properties': {'hat': {'$ref': '#/definitions/hat'}},
                    'required': ['hat'],
                    'type': 'object'
                },
                'hat': {'type': 'object'}
            },
            'items': [{'$ref': '#/definitions/sibling'}, {'type': 'null'}],
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_object(self):
        Siblings = jschema.Array(items=jschema.Object())
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'items': {'type': 'object'},
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_object_with_ref(self):
        Siblings = jschema.Array(items=jschema.Object(ref='sibling'))
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'sibling': {'type': 'object'}},
            'items': {'$ref': '#/definitions/sibling'},
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_object_with_refs(self):
        Siblings = jschema.Array(
            items=jschema.Object(ref='sibling'),
            additional_items=jschema.Object(ref='otherSibling')
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'sibling': {'type': 'object'},
                'otherSibling': {'type': 'object'}
            },
            'items': {'$ref': '#/definitions/sibling'},
            'additionalItems': {'$ref': '#/definitions/otherSibling'},
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_object_with_nested_ref(self):
        Siblings = jschema.Array(
            items=jschema.Object(
                ref='sibling',
                properties=jschema.Properties(hat=jschema.Object(ref='hat'))
            )
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'sibling': {
                    'properties': {'hat': {'$ref': '#/definitions/hat'}},
                    'required': ['hat'],
                    'type': 'object'
                },
                'hat': {'type': 'object'}
            },
            'items': {'$ref': '#/definitions/sibling'},
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_max_items_field(self):
        Siblings = jschema.Array(max_items=4)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'maxItems': 4,
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_min_items_field(self):
        Siblings = jschema.Array(min_items=1)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'minItems': 1,
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_unique_items_field(self):
        Siblings = jschema.Array(unique_items=True)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'uniqueItems': True,
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())


class TestBoolean(unittest.TestCase):
    """
    enum                    # all
    not                     # all

    """
    def test_type_field(self):
        OnlyChild = jschema.Boolean()
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Boolean().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'id': 'http://py.jschema/schemas/',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        OnlyChild = jschema.Boolean(title='Only child')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'title': 'Only child',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_description_field(self):
        OnlyChild = jschema.Boolean(description='Indicates if only child')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'description': 'Indicates if only child',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_default_field(self):
        OnlyChild = jschema.Boolean(default=True)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'default': True,
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())


class TestInteger(unittest.TestCase):
    """
    enum                    # all
    not                     # all

    """
    def test_type_field(self):
        Age = jschema.Integer()
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Integer().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'id': 'http://py.jschema/schemas/',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Age = jschema.Integer(title='Age')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'title': 'Age',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_description_field(self):
        Age = jschema.Integer(description='Age in years')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'description': 'Age in years',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_default_field(self):
        Age = jschema.Integer(default=0)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'default': 0,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_multiple_of_field(self):
        Age = jschema.Integer(multiple_of=1)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'multipleOf': 1,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_maximum_field(self):
        Age = jschema.Integer(maximum=100)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'maximum': 100,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_exclusive_maximum_field(self):
        Age = jschema.Integer(maximum=100, exclusive_maximum=True)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'maximum': 100,
            'exclusiveMaximum': True,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_minimum_field(self):
        Age = jschema.Integer(minimum=1)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'minimum': 1,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_exclusive_minimum_field(self):
        Age = jschema.Integer(minimum=1, exclusive_minimum=False)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'minimum': 1,
            'exclusiveMinimum': False,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())


class TestNull(unittest.TestCase):
    """
    enum                    # all
    not                     # all

    """
    def test_type_field(self):
        Brain = jschema.Null()
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Null().jschema.asdict(id='http://py.jschema/schemas/')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'id': 'http://py.jschema/schemas/',
            'type': 'null'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Brain = jschema.Null(title='Brain')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'title': 'Brain',
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_description_field(self):
        Brain = jschema.Null(description='Represents the brain')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'description': 'Represents the brain',
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_default_field(self):
        Brain = jschema.Null(default=None)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'default': None,
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())


class TestNumber(unittest.TestCase):
    """
    enum                    # all
    not                     # all

    """
    def test_type_field(self):
        Height = jschema.Number()
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Number().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'id': 'http://py.jschema/schemas/',
            'type': 'number'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Height = jschema.Number(title='Height')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'title': 'Height',
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_description_field(self):
        Height = jschema.Number(description='Height in cm')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'description': 'Height in cm',
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_default_field(self):
        Height = jschema.Number(default=176.2)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'default': 176.2,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_multiple_of_field(self):
        Height = jschema.Number(multiple_of=5.)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'multipleOf': 5.,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_maximum_field(self):
        Height = jschema.Number(maximum=200.)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'maximum': 200.,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_exclusive_maximum_field(self):
        Height = jschema.Number(maximum=200., exclusive_maximum=True)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'maximum': 200.,
            'exclusiveMaximum': True,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_minimum_field(self):
        Height = jschema.Number(minimum=10.)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'minimum': 10.,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_exclusive_minimum_field(self):
        Height = jschema.Number(minimum=10., exclusive_minimum=False)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'minimum': 10.,
            'exclusiveMinimum': False,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())


class TestObject(unittest.TestCase):
    """
    enum                    # all
    not                     # all

    """
    def test_type_field(self):
        Hat = jschema.Object()
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Object().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'id': 'http://py.jschema/schemas/',
            'type': 'object'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Hat = jschema.Object(title='Hat')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'title': 'Hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_description_field(self):
        Hat = jschema.Object(description='A type of hat')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'description': 'A type of hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_max_properties_field(self):
        Hat = jschema.Object(max_properties=2)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'maxProperties': 2,
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_min_properties_field(self):
        Hat = jschema.Object(min_properties=1)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'minProperties': 1,
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_optional_field(self):
        Hat = jschema.Object(
            properties=jschema.Properties(size=jschema.Integer(optional=True))
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'properties': {'size': {'type': 'integer'}},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_additional_properties_field_as_boolean(self):
        Hat = jschema.Object(additional_properties=True)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'additionalProperties': True,
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_additional_properties_field_as_object(self):
        Hat = jschema.Object(additional_properties=jschema.Object())
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'additionalProperties': {'type': 'object'},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_additional_properties_field_as_object_with_ref(self):
        Hat = jschema.Object(
            additional_properties=jschema.Object(ref='otherProps')
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'otherProps': {'type': 'object'}},
            'additionalProperties': {'$ref': '#/definitions/otherProps'},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_additional_properties_field_as_object_with_refs(self):
        Hat = jschema.Object(
            additional_properties=jschema.Object(ref='otherProps'),
            properties=jschema.Properties(color=jschema.Integer(ref='color'))
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'otherProps': {'type': 'object'},
                'color': {'type': 'integer'}
            },
            'properties': {'color': {'$ref': '#/definitions/color'}},
            'required': ['color'],
            'additionalProperties': {'$ref': '#/definitions/otherProps'},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_additional_properties_field_as_object_with_nested_ref(self):
        Hat = jschema.Object(
            additional_properties=jschema.Object(
                ref='otherProps',
                properties=jschema.Properties(name=jschema.String(ref='name'))
            )
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'otherProps': {
                    'properties': {'name': {'$ref': '#/definitions/name'}},
                    'required': ['name'],
                    'type': 'object'},
                'name': {'type': 'string'}
            },
            'additionalProperties': {
                '$ref': '#/definitions/otherProps'
            },
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_properties_field(self):
        Hat = jschema.Object(
            properties=jschema.Properties(size=jschema.Object())
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'properties': {'size': {'type': 'object'}},
            'required': ['size'],
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_properties_field_with_ref(self):
        Hat = jschema.Object(
            properties=jschema.Properties(size=jschema.Object(ref='size'))
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'size': {'type': 'object'}},
            'properties': {'size': {'$ref': '#/definitions/size'}},
            'required': ['size'],
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_properties_field_with_refs(self):
        Hat = jschema.Object(
            properties=jschema.Properties(
                size=jschema.Object(ref='size'),
                color=jschema.Number(ref='color')
            )
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'size': {'type': 'object'}, 'color': {'type': 'number'}
            },
            'properties': {
                'size': {'$ref': '#/definitions/size'},
                'color': {'$ref': '#/definitions/color'}
            },
            'required': ['color', 'size'],
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_properties_field_with_nested_ref(self):
        Hat = jschema.Object(
            properties=jschema.Properties(
                ribbon=jschema.Object(
                    ref='ribbon',
                    properties=jschema.Properties(
                        color=jschema.Integer(ref='color')
                    )
                )
            )
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'ribbon': {
                    'properties': {'color': {'$ref': '#/definitions/color'}},
                    'required': ['color'],
                    'type': 'object'
                },
                'color': {'type': 'integer'}
            },
            'properties': {'ribbon': {'$ref': '#/definitions/ribbon'}},
            'required': ['ribbon'],
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_pattern_properties_field(self):
        Hat = jschema.Object(pattern_properties={'^hat_.*$': jschema.Object()})
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'patternProperties': {'^hat_.*$': {'type': 'object'}},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_pattern_properties_field_with_ref(self):
        Hat = jschema.Object(
            pattern_properties={'^hat_.*$': jschema.Object(ref='otherProps')}
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'otherProps': {'type': 'object'}},
            'patternProperties': {
                '^hat_.*$': {'$ref': '#/definitions/otherProps'}
            },
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_pattern_properties_field_with_refs(self):
        Hat = jschema.Object(
            pattern_properties={
                '^hat_.*$': jschema.Object(ref='otherProps'),
                '^meta_.*$': jschema.Object(ref='metaProps')
            }
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'otherProps': {'type': 'object'},
                'metaProps': {'type': 'object'}
            },
            'patternProperties': {
                '^hat_.*$': {'$ref': '#/definitions/otherProps'},
                '^meta_.*$': {'$ref': '#/definitions/metaProps'}
            },
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_pattern_properties_field_with_nested_ref(self):
        Hat = jschema.Object(
            pattern_properties={
                '^hat_.*$': jschema.Object(
                    ref='otherProps',
                    properties=jschema.Properties(
                        name=jschema.String(ref='name')
                    )
                )
            }
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'otherProps': {
                    'properties': {'name': {'$ref': '#/definitions/name'}},
                    'required': ['name'],
                    'type': 'object'},
                'name': {'type': 'string'}
            },
            'patternProperties': {
                '^hat_.*$': {'$ref': '#/definitions/otherProps'}
            },
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_schema_dependency(self):
        Hat = jschema.Object(
            dependencies=jschema.Dependencies(color=jschema.Object())
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'dependencies': {'color': {'type': 'object'}},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_schema_dependency_with_ref(self):
        Hat = jschema.Object(
            dependencies=jschema.Dependencies(
                color=jschema.Object(ref='color')
            )
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'color': {'type': 'object'}},
            'dependencies': {'color': {'$ref': '#/definitions/color'}},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_schema_dependency_with_refs(self):
        Hat = jschema.Object(
            dependencies=jschema.Dependencies(
                color=jschema.Object(ref='color'),
                size=jschema.Object(ref='size')
            )
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'color': {'type': 'object'}, 'size': {'type': 'object'}
            },
            'dependencies': {
                'color': {'$ref': '#/definitions/color'},
                'size': {'$ref': '#/definitions/size'}
            },
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_schema_dependency_with_nested_ref(self):
        Hat = jschema.Object(
            dependencies=jschema.Dependencies(
                color=jschema.Object(
                    ref='color',
                    properties=jschema.Properties(rgb=jschema.Array(ref='rgb'))
                )
            )
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'color': {
                    'properties': {'rgb': {'$ref': '#/definitions/rgb'}},
                    'required': ['rgb'],
                    'type': 'object'
                },
                'rgb': {'type': 'array'}
            },
            'dependencies': {'color': {'$ref': '#/definitions/color'}},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_property_dependency(self):
        Hat = jschema.Object(dependencies=jschema.Dependencies(color=['size']))
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'dependencies': {'color': ['size']},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())


class TestString(unittest.TestCase):
    """
    enum                    # all
    not                     # all

    """
    def test_type_field(self):
        Name = jschema.String()
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_id_field(self):
        schema = jschema.String().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'id': 'http://py.jschema/schemas/',
            'type': 'string'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Name = jschema.String(title='Name')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'title': 'Name',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_description_field(self):
        Name = jschema.String(description='Name or nickname')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'description': 'Name or nickname',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_default_field(self):
        Name = jschema.String(default='Anonymous')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'default': 'Anonymous',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_max_length_field(self):
        Name = jschema.String(max_length=32)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'maxLength': 32,
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_min_length_field(self):
        Name = jschema.String(min_length=1)
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'minLength': 1,
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_pattern_field(self):
        Name = jschema.String(pattern='.*')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'pattern': '.*',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())


class TestEmpty(unittest.TestCase):
    def test_id_field(self):
        schema = jschema.Empty(all_of=[jschema.Object()]).jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'id': 'http://py.jschema/schemas/',
            'allOf': [{'type': 'object'}]
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Name = jschema.Empty(all_of=[jschema.Object()], title='Name')
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'title': 'Name',
            'allOf': [{'type': 'object'}]
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_description_field(self):
        Name = jschema.Empty(
            all_of=[jschema.Object()], description='Name or nickname'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'description': 'Name or nickname',
            'allOf': [{'type': 'object'}]
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_default_field(self):
        Name = jschema.Empty(all_of=[jschema.Object()], default={})
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'default': {},
            'allOf': [{'type': 'object'}]
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_all_of(self):
        Height = jschema.Empty(all_of=[jschema.Integer(), jschema.Number()])
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'allOf': [{'type': 'integer'}, {'type': 'number'}]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_all_of_with_ref(self):
        Height = jschema.Empty(all_of=[jschema.Integer(ref='cm')])
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'cm': {'type': 'integer'}},
            'allOf': [{'$ref': '#/definitions/cm'}]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_all_of_with_refs(self):
        Height = jschema.Empty(
            all_of=[
                jschema.Number(ref='maxHeight', maximum=200),
                jschema.Number(ref='minHeight', minimum=50)
            ]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'maxHeight': {'maximum': 200, 'type': 'number'},
                'minHeight': {'minimum': 50, 'type': 'number'},
            },
            'allOf': [
                {'$ref': '#/definitions/maxHeight'},
                {'$ref': '#/definitions/minHeight'}
            ]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_all_of_with_nested_ref(self):
        Hat = jschema.Empty(
            all_of=[
                jschema.Object(
                    ref='size',
                    properties=jschema.Properties(
                        cm=jschema.Integer(ref='cm')
                    )
                )
            ]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'size': {
                    'properties': {'cm': {'$ref': '#/definitions/cm'}},
                    'required': ['cm'],
                    'type': 'object'
                },
                'cm': {'type': 'integer'}
            },
            'allOf': [{'$ref': '#/definitions/size'}]
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_any_of(self):
        Height = jschema.Empty(any_of=[jschema.Integer(), jschema.Number()])
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'anyOf': [{'type': 'integer'}, {'type': 'number'}]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_any_of_with_ref(self):
        Height = jschema.Empty(any_of=[jschema.Integer(ref='cm')])
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'cm': {'type': 'integer'}},
            'anyOf': [{'$ref': '#/definitions/cm'}]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_any_of_with_refs(self):
        Height = jschema.Empty(
            any_of=[
                jschema.Number(ref='maxHeight', maximum=200),
                jschema.Number(ref='minHeight', minimum=50)
            ]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'maxHeight': {'maximum': 200, 'type': 'number'},
                'minHeight': {'minimum': 50, 'type': 'number'},
            },
            'anyOf': [
                {'$ref': '#/definitions/maxHeight'},
                {'$ref': '#/definitions/minHeight'}
            ]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_any_of_with_nested_ref(self):
        Hat = jschema.Empty(
            any_of=[
                jschema.Object(
                    ref='size',
                    properties=jschema.Properties(
                        cm=jschema.Integer(ref='cm')
                    )
                )
            ]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'size': {
                    'properties': {'cm': {'$ref': '#/definitions/cm'}},
                    'required': ['cm'],
                    'type': 'object'
                },
                'cm': {'type': 'integer'}
            },
            'anyOf': [{'$ref': '#/definitions/size'}]
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_one_of(self):
        Height = jschema.Empty(one_of=[jschema.Integer(), jschema.Number()])
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'oneOf': [{'type': 'integer'}, {'type': 'number'}]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_one_of_with_ref(self):
        Height = jschema.Empty(one_of=[jschema.Integer(ref='cm')])
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {'cm': {'type': 'integer'}},
            'oneOf': [{'$ref': '#/definitions/cm'}]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_one_of_with_refs(self):
        Height = jschema.Empty(
            one_of=[
                jschema.Number(ref='maxHeight', maximum=200),
                jschema.Number(ref='minHeight', minimum=50)
            ]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'maxHeight': {'maximum': 200, 'type': 'number'},
                'minHeight': {'minimum': 50, 'type': 'number'},
            },
            'oneOf': [
                {'$ref': '#/definitions/maxHeight'},
                {'$ref': '#/definitions/minHeight'}
            ]
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_one_of_with_nested_ref(self):
        Hat = jschema.Empty(
            one_of=[
                jschema.Object(
                    ref='size',
                    properties=jschema.Properties(
                        cm=jschema.Integer(ref='cm')
                    )
                )
            ]
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'definitions': {
                'size': {
                    'properties': {'cm': {'$ref': '#/definitions/cm'}},
                    'required': ['cm'],
                    'type': 'object'
                },
                'cm': {'type': 'integer'}
            },
            'oneOf': [{'$ref': '#/definitions/size'}]
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())


if __name__ == '__main__':
    unittest.main()

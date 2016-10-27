import unittest

import jschema


class TestArray(unittest.TestCase):
    def test_type_field(self):
        Siblings = jschema.Array()
        expected_schema = {
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Array().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            'id': 'http://py.jschema/schemas/',
            'type': 'array'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Siblings = jschema.Array(title='Siblings')
        expected_schema = {
            'title': 'Siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_description_field(self):
        Siblings = jschema.Array(description='List of siblings')
        expected_schema = {
            'description': 'List of siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_default_field(self):
        Siblings = jschema.Array(default=[])
        expected_schema = {
            'default': [],
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_max_items_field(self):
        Siblings = jschema.Array(max_items=4)
        expected_schema = {
            'maxItems': 4,
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_min_items_field(self):
        Siblings = jschema.Array(min_items=1)
        expected_schema = {
            'minItems': 1,
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_unique_items_field(self):
        Siblings = jschema.Array(unique_items=True)
        expected_schema = {
            'uniqueItems': True,
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())


class TestBoolean(unittest.TestCase):
    def test_type_field(self):
        OnlyChild = jschema.Boolean()
        expected_schema = {
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Boolean().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            'id': 'http://py.jschema/schemas/',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        OnlyChild = jschema.Boolean(title='Only child')
        expected_schema = {
            'title': 'Only child',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_description_field(self):
        OnlyChild = jschema.Boolean(description='Indicates if only child')
        expected_schema = {
            'description': 'Indicates if only child',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_default_field(self):
        OnlyChild = jschema.Boolean(default=True)
        expected_schema = {
            'default': True,
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())


class TestInteger(unittest.TestCase):
    def test_type_field(self):
        Age = jschema.Integer()
        expected_schema = {
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Integer().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            'id': 'http://py.jschema/schemas/',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Age = jschema.Integer(title='Age')
        expected_schema = {
            'title': 'Age',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_description_field(self):
        Age = jschema.Integer(description='Age in years')
        expected_schema = {
            'description': 'Age in years',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_default_field(self):
        Age = jschema.Integer(default=0)
        expected_schema = {
            'default': 0,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_multiple_of_field(self):
        Age = jschema.Integer(multiple_of=1)
        expected_schema = {
            'multipleOf': 1,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_maximum_field(self):
        Age = jschema.Integer(maximum=100)
        expected_schema = {
            'maximum': 100,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_exclusive_maximum_field(self):
        Age = jschema.Integer(maximum=100, exclusive_maximum=True)
        expected_schema = {
            'maximum': 100,
            'exclusiveMaximum': True,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_minimum_field(self):
        Age = jschema.Integer(minimum=1)
        expected_schema = {
            'minimum': 1,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_exclusive_minimum_field(self):
        Age = jschema.Integer(minimum=1, exclusive_minimum=False)
        expected_schema = {
            'minimum': 1,
            'exclusiveMinimum': False,
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())


class TestNull(unittest.TestCase):
    def test_type_field(self):
        Brain = jschema.Null()
        expected_schema = {
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Null().jschema.asdict(id='http://py.jschema/schemas/')
        expected_schema = {
            'id': 'http://py.jschema/schemas/',
            'type': 'null'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Brain = jschema.Null(title='Brain')
        expected_schema = {
            'title': 'Brain',
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_description_field(self):
        Brain = jschema.Null(description='Represents the brain')
        expected_schema = {
            'description': 'Represents the brain',
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_default_field(self):
        Brain = jschema.Null(default=None)
        expected_schema = {
            'default': None,
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())


class TestNumber(unittest.TestCase):
    def test_type_field(self):
        Height = jschema.Number()
        expected_schema = {
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Number().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            'id': 'http://py.jschema/schemas/',
            'type': 'number'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Height = jschema.Number(title='Height')
        expected_schema = {
            'title': 'Height',
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_description_field(self):
        Height = jschema.Number(description='Height in cm')
        expected_schema = {
            'description': 'Height in cm',
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_default_field(self):
        Height = jschema.Number(default=176.2)
        expected_schema = {
            'default': 176.2,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_multiple_of_field(self):
        Height = jschema.Number(multiple_of=5.)
        expected_schema = {
            'multipleOf': 5.,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_maximum_field(self):
        Height = jschema.Number(maximum=200.)
        expected_schema = {
            'maximum': 200.,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_exclusive_maximum_field(self):
        Height = jschema.Number(maximum=200., exclusive_maximum=True)
        expected_schema = {
            'maximum': 200.,
            'exclusiveMaximum': True,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_minimum_field(self):
        Height = jschema.Number(minimum=10.)
        expected_schema = {
            'minimum': 10.,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_exclusive_minimum_field(self):
        Height = jschema.Number(minimum=10., exclusive_minimum=False)
        expected_schema = {
            'minimum': 10.,
            'exclusiveMinimum': False,
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())


class TestObject(unittest.TestCase):
    def test_type_field(self):
        Hat = jschema.Object()
        expected_schema = {
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_id_field(self):
        schema = jschema.Object().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            'id': 'http://py.jschema/schemas/',
            'type': 'object'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Hat = jschema.Object(title='Hat')
        expected_schema = {
            'title': 'Hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_description_field(self):
        Hat = jschema.Object(description='A type of hat')
        expected_schema = {
            'description': 'A type of hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_max_properties_field(self):
        Hat = jschema.Object(max_properties=2)
        expected_schema = {
            'maxProperties': 2,
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_min_properties_field(self):
        Hat = jschema.Object(min_properties=1)
        expected_schema = {
            'minProperties': 1,
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_additional_properties_field_as_boolean(self):
        Hat = jschema.Object(additional_properties=True)
        expected_schema = {
            'additionalProperties': True,
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_schema_dependency(self):
        Hat = jschema.Object(
            dependencies=jschema.Dependencies(color=jschema.Object())
        )
        expected_schema = {
            'dependencies': {'color': {'type': 'object'}},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_property_dependency(self):
        Hat = jschema.Object(dependencies=jschema.Dependencies(color=['size']))
        expected_schema = {
            'dependencies': {'color': ['size']},
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())


class TestString(unittest.TestCase):
    def test_type_field(self):
        Name = jschema.String()
        expected_schema = {
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_id_field(self):
        schema = jschema.String().jschema.asdict(
            id='http://py.jschema/schemas/'
        )
        expected_schema = {
            'id': 'http://py.jschema/schemas/',
            'type': 'string'
        }
        self.assertEqual(expected_schema, schema)

    def test_title_field(self):
        Name = jschema.String(title='Name')
        expected_schema = {
            'title': 'Name',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_description_field(self):
        Name = jschema.String(description='Name or nickname')
        expected_schema = {
            'description': 'Name or nickname',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_default_field(self):
        Name = jschema.String(default='Anonymous')
        expected_schema = {
            'default': 'Anonymous',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_max_length_field(self):
        Name = jschema.String(max_length=32)
        expected_schema = {
            'maxLength': 32,
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_min_length_field(self):
        Name = jschema.String(min_length=1)
        expected_schema = {
            'minLength': 1,
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_pattern_field(self):
        Name = jschema.String(pattern='.*')
        expected_schema = {
            'pattern': '.*',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())


if __name__ == '__main__':
    unittest.main()

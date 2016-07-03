import unittest

import jschema


class TestArray(unittest.TestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_type_field(self):
        Siblings = jschema.Array()
        self.assertEqual({'type': 'array'}, Siblings.jschema.asdict())

    def test_id_field(self):
        Siblings = jschema.Array(id='Siblings')
        self.assertEqual(
            {'id': 'Siblings', 'type': 'array'}, Siblings.jschema.asdict()
        )

    def test_schema_field(self):
        Siblings = jschema.Array(schema='http://json-schema.org/schema#')
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'array'},
            Siblings.jschema.asdict()
        )

    def test_title_field(self):
        Siblings = jschema.Array(title='Siblings')
        self.assertEqual(
            {'title': 'Siblings', 'type': 'array'}, Siblings.jschema.asdict()
        )

    def test_description_field(self):
        Siblings = jschema.Array(description='List of siblings')
        self.assertEqual(
            {'description': 'List of siblings', 'type': 'array'},
            Siblings.jschema.asdict()
        )

    def test_default_field(self):
        Siblings = jschema.Array(default=[])
        self.assertEqual(
            {'default': [], 'type': 'array'}, Siblings.jschema.asdict()
        )

    def test_additional_items_field_as_boolean(self):
        Siblings = jschema.Array(additional_items=True)
        self.assertEqual(
            {'additionalItems': True, 'type': 'array'},
            Siblings.jschema.asdict()
        )

    def test_additional_items_field_as_object(self):
        Siblings = jschema.Array(additional_items=jschema.Object())
        self.assertEqual(
            {'additionalItems': {'type': 'object'}, 'type': 'array'},
            Siblings.jschema.asdict()
        )

    def test_items_field_as_array(self):
        Siblings = jschema.Array(items=[jschema.Object(), jschema.Null()])
        self.assertEqual(
            {'items': [{'type': 'object'}, {'type': 'null'}], 'type': 'array'},
            Siblings.jschema.asdict()
        )

    def test_items_field_as_object(self):
        Siblings = jschema.Array(items=jschema.Object())
        self.assertEqual(
            {'items': {'type': 'object'}, 'type': 'array'},
            Siblings.jschema.asdict()
        )

    def test_max_items_field(self):
        Siblings = jschema.Array(max_items=4)
        self.assertEqual(
            {'maxItems': 4, 'type': 'array'}, Siblings.jschema.asdict()
        )

    def test_min_items_field(self):
        Siblings = jschema.Array(min_items=1)
        self.assertEqual(
            {'minItems': 1, 'type': 'array'}, Siblings.jschema.asdict()
        )

    def test_unique_items_field(self):
        Siblings = jschema.Array(unique_items=True)
        self.assertEqual(
            {'uniqueItems': True, 'type': 'array'}, Siblings.jschema.asdict()
        )


class TestBoolean(unittest.TestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_type_field(self):
        OnlyChild = jschema.Boolean()
        self.assertEqual({'type': 'boolean'}, OnlyChild.jschema.asdict())

    def test_id_field(self):
        OnlyChild = jschema.Boolean(id='OnlyChild')
        self.assertEqual(
            {'id': 'OnlyChild', 'type': 'boolean'}, OnlyChild.jschema.asdict()
        )

    def test_schema_field(self):
        OnlyChild = jschema.Boolean(schema='http://json-schema.org/schema#')
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'boolean'},
            OnlyChild.jschema.asdict()
        )

    def test_title_field(self):
        OnlyChild = jschema.Boolean(title='Only child')
        self.assertEqual(
            {'title': 'Only child', 'type': 'boolean'},
            OnlyChild.jschema.asdict()
        )

    def test_description_field(self):
        OnlyChild = jschema.Boolean(description='Indicates if only child')
        self.assertEqual(
            {'description': 'Indicates if only child', 'type': 'boolean'},
            OnlyChild.jschema.asdict()
        )

    def test_default_field(self):
        OnlyChild = jschema.Boolean(default=True)
        self.assertEqual(
            {'default': True, 'type': 'boolean'}, OnlyChild.jschema.asdict()
        )


class TestInteger(unittest.TestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_type_field(self):
        Age = jschema.Integer()
        self.assertEqual({'type': 'integer'}, Age.jschema.asdict())

    def test_id_field(self):
        Age = jschema.Integer(id='Age')
        self.assertEqual(
            {'id': 'Age', 'type': 'integer'}, Age.jschema.asdict()
        )

    def test_schema_field(self):
        Age = jschema.Integer(schema='http://json-schema.org/schema#')
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'integer'},
            Age.jschema.asdict()
        )

    def test_title_field(self):
        Age = jschema.Integer(title='Age')
        self.assertEqual(
            {'title': 'Age', 'type': 'integer'}, Age.jschema.asdict()
        )

    def test_description_field(self):
        Age = jschema.Integer(description='Age in years')
        self.assertEqual(
            {'description': 'Age in years', 'type': 'integer'},
            Age.jschema.asdict()
        )

    def test_default_field(self):
        Age = jschema.Integer(default=0)
        self.assertEqual(
            {'default': 0, 'type': 'integer'}, Age.jschema.asdict()
        )

    def test_multiple_of_field(self):
        Age = jschema.Integer(multiple_of=1)
        self.assertEqual(
            {'multipleOf': 1, 'type': 'integer'}, Age.jschema.asdict()
        )

    def test_maximum_field(self):
        Age = jschema.Integer(maximum=100)
        self.assertEqual(
            {'maximum': 100, 'type': 'integer'}, Age.jschema.asdict()
        )

    def test_exclusive_maximum_field(self):
        Age = jschema.Integer(maximum=100, exclusive_maximum=True)
        self.assertEqual(
            {'maximum': 100, 'exclusiveMaximum': True, 'type': 'integer'},
            Age.jschema.asdict()
        )

    def test_minimum_field(self):
        Age = jschema.Integer(minimum=1)
        self.assertEqual(
            {'minimum': 1, 'type': 'integer'}, Age.jschema.asdict()
        )

    def test_exclusive_minimum_field(self):
        Age = jschema.Integer(minimum=1, exclusive_minimum=False)
        self.assertEqual(
            {'minimum': 1, 'exclusiveMinimum': False, 'type': 'integer'},
            Age.jschema.asdict()
        )


class TestNull(unittest.TestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_type_field(self):
        Brain = jschema.Null()
        self.assertEqual({'type': 'null'}, Brain.jschema.asdict())

    def test_id_field(self):
        Brain = jschema.Null(id='Brain')
        self.assertEqual(
            {'id': 'Brain', 'type': 'null'}, Brain.jschema.asdict()
        )

    def test_schema_field(self):
        Brain = jschema.Null(schema='http://json-schema.org/schema#')
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'null'},
            Brain.jschema.asdict()
        )

    def test_title_field(self):
        Brain = jschema.Null(title='Brain')
        self.assertEqual(
            {'title': 'Brain', 'type': 'null'}, Brain.jschema.asdict()
        )

    def test_description_field(self):
        Brain = jschema.Null(description='Represents the brain')
        self.assertEqual(
            {'description': 'Represents the brain', 'type': 'null'},
            Brain.jschema.asdict()
        )

    def test_default_field(self):
        Brain = jschema.Null(default=None)
        self.assertEqual(
            {'default': None, 'type': 'null'}, Brain.jschema.asdict()
        )


class TestNumber(unittest.TestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all
    multipleOf              # number, integer
    maximum                 # number, integer
    exclusiveMaximum        # number, integer
    minimum                 # number, integer
    exclusiveMinimum        # number, integer

    """
    def test_type_field(self):
        Height = jschema.Number()
        self.assertEqual({'type': 'number'}, Height.jschema.asdict())

    def test_id_field(self):
        Height = jschema.Number(id='Height')
        self.assertEqual(
            {'id': 'Height', 'type': 'number'}, Height.jschema.asdict()
        )

    def test_schema_field(self):
        Height = jschema.Number(schema='http://json-schema.org/schema#')
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'number'},
            Height.jschema.asdict()
        )

    def test_title_field(self):
        Height = jschema.Number(title='Height')
        self.assertEqual(
            {'title': 'Height', 'type': 'number'}, Height.jschema.asdict()
        )

    def test_description_field(self):
        Height = jschema.Number(description='Height in cm')
        self.assertEqual(
            {'description': 'Height in cm', 'type': 'number'},
            Height.jschema.asdict()
        )

    def test_default_field(self):
        Height = jschema.Number(default=176.2)
        self.assertEqual(
            {'default': 176.2, 'type': 'number'}, Height.jschema.asdict()
        )


class TestObject(unittest.TestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all
    maxProperties           # object
    minProperties           # object
    required                # object
    additionalProperties    # object
    properties              # object
    patternProperties       # object
    dependencies            # object

    """
    def test_type_field(self):
        Hat = jschema.Object()
        self.assertEqual({'type': 'object'}, Hat.jschema.asdict())

    def test_id_field(self):
        Hat = jschema.Object(id='Hat')
        self.assertEqual({'id': 'Hat', 'type': 'object'}, Hat.jschema.asdict())

    def test_schema_field(self):
        Hat = jschema.Object(schema='http://json-schema.org/schema#')
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'object'},
            Hat.jschema.asdict()
        )

    def test_title_field(self):
        Hat = jschema.Object(title='Hat')
        self.assertEqual(
            {'title': 'Hat', 'type': 'object'}, Hat.jschema.asdict()
        )

    def test_description_field(self):
        Hat = jschema.Object(description='A type of hat')
        self.assertEqual(
            {'description': 'A type of hat', 'type': 'object'},
            Hat.jschema.asdict()
        )


class TestString(unittest.TestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all
    maxLength               # string
    minLength               # string
    pattern                 # string

    """
    def test_type_field(self):
        Name = jschema.String()
        self.assertEqual({'type': 'string'}, Name.jschema.asdict())

    def test_id_field(self):
        Name = jschema.String(id='Name')
        self.assertEqual(
            {'id': 'Name', 'type': 'string'}, Name.jschema.asdict()
        )

    def test_schema_field(self):
        Name = jschema.String(schema='http://json-schema.org/schema#')
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'string'},
            Name.jschema.asdict()
        )

    def test_title_field(self):
        Name = jschema.String(title='Name')
        self.assertEqual(
            {'title': 'Name', 'type': 'string'}, Name.jschema.asdict()
        )

    def test_description_field(self):
        Name = jschema.String(description='Name or nickname')
        self.assertEqual(
            {'description': 'Name or nickname', 'type': 'string'},
            Name.jschema.asdict()
        )

    def test_default_field(self):
        Name = jschema.String(default='Foo')
        self.assertEqual(
            {'default': 'Foo', 'type': 'string'}, Name.jschema.asdict()
        )


if __name__ == '__main__':
    unittest.main()

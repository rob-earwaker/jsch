import unittest

import jschema


class TestArray(unittest.TestCase):
    """
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all
    additionalItems         # array
    items                   # array
    maxItems                # array
    minItems                # array
    uniqueItems             # array

    """
    def test_schema_type_definition(self):
        Siblings = jschema.Array()
        self.assertEqual({'type': 'array'}, Siblings.jschema.asdict())

    def test_schema_id_definition(self):
        Siblings = jschema.Array(id='Siblings')
        self.assertEqual(
            {'id': 'Siblings', 'type': 'array'}, Siblings.jschema.asdict()
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
    def test_schema_type_definition(self):
        OnlyChild = jschema.Boolean()
        self.assertEqual({'type': 'boolean'}, OnlyChild.jschema.asdict())

    def test_schema_id_definition(self):
        OnlyChild = jschema.Boolean(id='OnlyChild')
        self.assertEqual(
            {'id': 'OnlyChild', 'type': 'boolean'}, OnlyChild.jschema.asdict()
        )

    def test_schema_definition(self):
        OnlyChild = jschema.Boolean(schema='http://json-schema.org/schema#')
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'boolean'},
            OnlyChild.jschema.asdict()
        )

    def test_schema_title_definition(self):
        OnlyChild = jschema.Boolean(title='Only child')
        self.assertEqual(
            {'title': 'Only child', 'type': 'boolean'},
            OnlyChild.jschema.asdict()
        )

    def test_schema_description_definition(self):
        OnlyChild = jschema.Boolean(description='Indicates if only child')
        self.assertEqual(
            {'description': 'Indicates if only child', 'type': 'boolean'},
            OnlyChild.jschema.asdict()
        )

    def test_schema_default_definition(self):
        OnlyChild = jschema.Boolean(default=True)
        self.assertEqual(
            {'default': True, 'type': 'boolean'}, OnlyChild.jschema.asdict()
        )


class TestInteger(unittest.TestCase):
    """
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
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
    def test_schema_type_definition(self):
        Age = jschema.Integer()
        self.assertEqual({'type': 'integer'}, Age.jschema.asdict())

    def test_schema_id_definition(self):
        Age = jschema.Integer(id='Age')
        self.assertEqual(
            {'id': 'Age', 'type': 'integer'}, Age.jschema.asdict()
        )


class TestNull(unittest.TestCase):
    """
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_schema_type_definition(self):
        Brain = jschema.Null()
        self.assertEqual({'type': 'null'}, Brain.jschema.asdict())

    def test_schema_id_definition(self):
        Brain = jschema.Null(id='Brain')
        self.assertEqual(
            {'id': 'Brain', 'type': 'null'}, Brain.jschema.asdict()
        )


class TestNumber(unittest.TestCase):
    """
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
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
    def test_schema_type_definition(self):
        Height = jschema.Number()
        self.assertEqual({'type': 'number'}, Height.jschema.asdict())

    def test_schema_id_definition(self):
        Height = jschema.Number(id='Height')
        self.assertEqual(
            {'id': 'Height', 'type': 'number'}, Height.jschema.asdict()
        )


class TestObject(unittest.TestCase):
    """
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
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
    def test_schema_type_definition(self):
        Hat = jschema.Object()
        self.assertEqual({'type': 'object'}, Hat.jschema.asdict())

    def test_schema_id_definition(self):
        Hat = jschema.Object(id='Hat')
        self.assertEqual({'id': 'Hat', 'type': 'object'}, Hat.jschema.asdict())


class TestString(unittest.TestCase):
    """
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
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
    def test_schema_type_definition(self):
        Name = jschema.String()
        self.assertEqual({'type': 'string'}, Name.jschema.asdict())

    def test_schema_id_definition(self):
        Name = jschema.String(id='Name')
        self.assertEqual(
            {'id': 'Name', 'type': 'string'}, Name.jschema.asdict()
        )


if __name__ == '__main__':
    unittest.main()

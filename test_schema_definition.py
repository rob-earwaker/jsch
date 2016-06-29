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
        class Person(jschema.Object):
            siblings = jschema.Array()
        self.assertEqual(
            {'type': 'array'}, Person.jschema()['properties']['siblings']
        )

    def test_schema_id_definition(self):
        class Person(jschema.Object):
            siblings = jschema.Array(id='siblings')
        self.assertEqual(
            {'id': 'siblings', 'type': 'array'},
            Person.jschema()['properties']['siblings']
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
        class Person(jschema.Object):
            only_child = jschema.Boolean()
        self.assertEqual(
            {'type': 'boolean'}, Person.jschema()['properties']['only_child']
        )

    def test_schema_id_definition(self):
        class Person(jschema.Object):
            only_child = jschema.Boolean(id='only-child')
        self.assertEqual(
            {'id': 'only-child', 'type': 'boolean'},
            Person.jschema()['properties']['only_child']
        )

    def test_schema_definition(self):
        class Person(jschema.Object):
            only_child = jschema.Boolean(
                schema='http://json-schema.org/schema#'
            )
        self.assertEqual(
            {'$schema': 'http://json-schema.org/schema#', 'type': 'boolean'},
            Person.jschema()['properties']['only_child']
        )

    def test_schema_title_definition(self):
        class Person(jschema.Object):
            only_child = jschema.Boolean(title='Only child')
        self.assertEqual(
            {'title': 'Only child', 'type': 'boolean'},
            Person.jschema()['properties']['only_child']
        )

    def test_schema_description_definition(self):
        class Person(jschema.Object):
            only_child = jschema.Boolean(
                description='Indicates whether the person is an only child'
            )
        expected_schema = {
            'description': 'Indicates whether the person is an only child',
            'type': 'boolean'
        }
        self.assertEqual(
            expected_schema, Person.jschema()['properties']['only_child']
        )

    def test_schema_default_definition(self):
        class Person(jschema.Object):
            only_child = jschema.Boolean(default=True)
        self.assertEqual(
            {'default': True, 'type': 'boolean'},
            Person.jschema()['properties']['only_child']
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
        class Person(jschema.Object):
            age = jschema.Integer()
        self.assertEqual(
            {'type': 'integer'}, Person.jschema()['properties']['age']
        )

    def test_schema_id_definition(self):
        class Person(jschema.Object):
            age = jschema.Integer(id='age')
        self.assertEqual(
            {'id': 'age', 'type': 'integer'},
            Person.jschema()['properties']['age']
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
        class Person(jschema.Object):
            brain = jschema.Null()
        self.assertEqual(
            {'type': 'null'}, Person.jschema()['properties']['brain']
        )

    def test_schema_id_definition(self):
        class Person(jschema.Object):
            brain = jschema.Null(id='brain')
        self.assertEqual(
            {'id': 'brain', 'type': 'null'},
            Person.jschema()['properties']['brain']
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
        class Person(jschema.Object):
            height = jschema.Number()
        self.assertEqual(
            {'type': 'number'}, Person.jschema()['properties']['height']
        )

    def test_schema_id_definition(self):
        class Person(jschema.Object):
            height = jschema.Number(id='height')
        self.assertEqual(
            {'id': 'height', 'type': 'number'},
            Person.jschema()['properties']['height']
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
        class Hat(jschema.Object):
            pass

        class Person(jschema.Object):
            hat = jschema.Object(Hat)
        self.assertEqual(
            {'type': 'object'}, Person.jschema()['properties']['hat']
        )

    def test_schema_id_definition(self):
        class Hat(jschema.Object):
            jschema_id = 'hat'

        class Person(jschema.Object):
            hat = jschema.Object(Hat)
        self.assertEqual(
            {'id': 'hat', 'type': 'object'},
            Person.jschema()['properties']['hat']
        )


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
        class Person(jschema.Object):
            name = jschema.String()
        self.assertEqual(
            {'type': 'string'}, Person.jschema()['properties']['name']
        )

    def test_schema_id_definition(self):
        class Person(jschema.Object):
            name = jschema.String(id='name')
        self.assertEqual(
            {'id': 'name', 'type': 'string'},
            Person.jschema()['properties']['name']
        )


if __name__ == '__main__':
    unittest.main()

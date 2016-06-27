import unittest

import jschema


class TestArray(unittest.TestCase):
    """
    id                      # meta
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
    definitions             # all
    enum                    # all
    type                    # all
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
    pass


class TestBoolean(unittest.TestCase):
    """
    definitions             # all
    enum                    # all
    type                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
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
    id                      # meta
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
    definitions             # all
    enum                    # all
    type                    # all
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
    pass


class TestNull(unittest.TestCase):
    """
    id                      # meta
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
    definitions             # all
    enum                    # all
    type                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    pass


class TestNumber(unittest.TestCase):
    """
    id                      # meta
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
    definitions             # all
    enum                    # all
    type                    # all
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
    pass


class TestObject(unittest.TestCase):
    """
    id                      # meta
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
    definitions             # all
    enum                    # all
    type                    # all
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
    pass


class TestString(unittest.TestCase):
    """
    id                      # meta
    $schema                 # meta
    title                   # meta
    description             # meta
    default                 # meta
    definitions             # all
    enum                    # all
    type                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all
    maxLength               # string
    minLength               # string
    pattern                 # string

    """
    pass


if __name__ == '__main__':
    unittest.main()

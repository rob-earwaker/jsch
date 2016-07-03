import re
import unittest

import jschema


class JSchemaTestCase(unittest.TestCase):
    def assertRaisesDefinitionError(self, message):
        return self.assertRaisesRegexp(
            jschema.JSchemaDefinitionError, re.escape(message)
        )


class TestArray(JSchemaTestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_id_field_required(self):
        with self.assertRaisesDefinitionError("'id' field is required"):
            jschema.Array()

    def test_schema_field(self):
        Siblings = jschema.Array(
            id='siblings', schema='http://json-schema.org/schema#'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_title_field(self):
        Siblings = jschema.Array(id='siblings', title='Siblings')
        expected_schema = {
            'title': 'Siblings', 'id': 'siblings', 'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_description_field(self):
        Siblings = jschema.Array(id='siblings', description='List of siblings')
        expected_schema = {
            'description': 'List of siblings',
            'id': 'siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_default_field(self):
        Siblings = jschema.Array(id='siblings', default=[])
        expected_schema = {'default': [], 'id': 'siblings', 'type': 'array'}
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_additional_items_field_as_boolean(self):
        Siblings = jschema.Array(id='siblings', additional_items=True)
        expected_schema = {
            'additionalItems': True, 'id': 'siblings', 'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_additional_items_field_as_object(self):
        Siblings = jschema.Array(
            id='siblings', additional_items=jschema.Object(id='sibling')
        )
        expected_schema = {
            'additionalItems': {'id': 'sibling', 'type': 'object'},
            'id': 'siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_array(self):
        Siblings = jschema.Array(
            id='siblings',
            items=[
                jschema.Object(id='sibling'), jschema.Null(id='unknownSibling')
            ]
        )
        expected_schema = {
            'items': [
                {'id': 'sibling', 'type': 'object'},
                {'id': 'unknownSibling', 'type': 'null'}
            ],
            'id': 'siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_items_field_as_object(self):
        Siblings = jschema.Array(
            id='siblings', items=jschema.Object(id='sibling')
        )
        expected_schema = {
            'items': {'id': 'sibling', 'type': 'object'},
            'id': 'siblings',
            'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_max_items_field(self):
        Siblings = jschema.Array(id='siblings', max_items=4)
        expected_schema = {'maxItems': 4, 'id': 'siblings', 'type': 'array'}
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_min_items_field(self):
        Siblings = jschema.Array(id='siblings', min_items=1)
        expected_schema = {'minItems': 1, 'id': 'siblings', 'type': 'array'}
        self.assertEqual(expected_schema, Siblings.jschema.asdict())

    def test_unique_items_field(self):
        Siblings = jschema.Array(id='siblings', unique_items=True)
        expected_schema = {
            'uniqueItems': True, 'id': 'siblings', 'type': 'array'
        }
        self.assertEqual(expected_schema, Siblings.jschema.asdict())


class TestBoolean(JSchemaTestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_id_field_required(self):
        with self.assertRaisesDefinitionError("'id' field is required"):
            jschema.Boolean()

    def test_schema_field(self):
        OnlyChild = jschema.Boolean(
            id='onlyChild', schema='http://json-schema.org/schema#'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'onlyChild',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_title_field(self):
        OnlyChild = jschema.Boolean(id='onlyChild', title='Only child')
        expected_schema = {
            'title': 'Only child', 'id': 'onlyChild', 'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_description_field(self):
        OnlyChild = jschema.Boolean(
            id='onlyChild', description='Indicates if only child'
        )
        expected_schema = {
            'description': 'Indicates if only child',
            'id': 'onlyChild',
            'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())

    def test_default_field(self):
        OnlyChild = jschema.Boolean(id='onlyChild', default=True)
        expected_schema = {
            'default': True, 'id': 'onlyChild', 'type': 'boolean'
        }
        self.assertEqual(expected_schema, OnlyChild.jschema.asdict())


class TestInteger(JSchemaTestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_id_field_required(self):
        with self.assertRaisesDefinitionError("'id' field is required"):
            jschema.Integer()

    def test_schema_field(self):
        Age = jschema.Integer(
            id='age', schema='http://json-schema.org/schema#'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'age',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_title_field(self):
        Age = jschema.Integer(id='age', title='Age')
        expected_schema = {'title': 'Age', 'id': 'age', 'type': 'integer'}
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_description_field(self):
        Age = jschema.Integer(id='age', description='Age in years')
        expected_schema = {
            'description': 'Age in years', 'id': 'age', 'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_default_field(self):
        Age = jschema.Integer(id='age', default=0)
        expected_schema = {'default': 0, 'id': 'age', 'type': 'integer'}
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_multiple_of_field(self):
        Age = jschema.Integer(id='age', multiple_of=1)
        expected_schema = {'multipleOf': 1, 'id': 'age', 'type': 'integer'}
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_maximum_field(self):
        Age = jschema.Integer(id='age', maximum=100)
        expected_schema = {'maximum': 100, 'id': 'age', 'type': 'integer'}
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_exclusive_maximum_field(self):
        Age = jschema.Integer(id='age', maximum=100, exclusive_maximum=True)
        expected_schema = {
            'maximum': 100,
            'exclusiveMaximum': True,
            'id': 'age',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_minimum_field(self):
        Age = jschema.Integer(id='age', minimum=1)
        expected_schema = {'minimum': 1, 'id': 'age', 'type': 'integer'}
        self.assertEqual(expected_schema, Age.jschema.asdict())

    def test_exclusive_minimum_field(self):
        Age = jschema.Integer(id='age', minimum=1, exclusive_minimum=False)
        expected_schema = {
            'minimum': 1,
            'exclusiveMinimum': False,
            'id': 'age',
            'type': 'integer'
        }
        self.assertEqual(expected_schema, Age.jschema.asdict())


class TestNull(JSchemaTestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_id_field_required(self):
        with self.assertRaisesDefinitionError("'id' field is required"):
            jschema.Null()

    def test_schema_field(self):
        Brain = jschema.Null(
            id='brain', schema='http://json-schema.org/schema#'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'brain',
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_title_field(self):
        Brain = jschema.Null(id='brain', title='Brain')
        expected_schema = {'title': 'Brain', 'id': 'brain', 'type': 'null'}
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_description_field(self):
        Brain = jschema.Null(id='brain', description='Represents the brain')
        expected_schema = {
            'description': 'Represents the brain',
            'id': 'brain',
            'type': 'null'
        }
        self.assertEqual(expected_schema, Brain.jschema.asdict())

    def test_default_field(self):
        Brain = jschema.Null(id='brain', default=None)
        expected_schema = {'default': None, 'id': 'brain', 'type': 'null'}
        self.assertEqual(expected_schema, Brain.jschema.asdict())


class TestNumber(JSchemaTestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_id_field_required(self):
        with self.assertRaisesDefinitionError("'id' field is required"):
            jschema.Number()

    def test_schema_field(self):
        Height = jschema.Number(
            id='height', schema='http://json-schema.org/schema#'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'height',
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_title_field(self):
        Height = jschema.Number(id='height', title='Height')
        expected_schema = {'title': 'Height', 'id': 'height', 'type': 'number'}
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_description_field(self):
        Height = jschema.Number(id='height', description='Height in cm')
        expected_schema = {
            'description': 'Height in cm', 'id': 'height', 'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_default_field(self):
        Height = jschema.Number(id='height', default=176.2)
        expected_schema = {'default': 176.2, 'id': 'height', 'type': 'number'}
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_multiple_of_field(self):
        Height = jschema.Number(id='height', multiple_of=5.)
        expected_schema = {'multipleOf': 5., 'id': 'height', 'type': 'number'}
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_maximum_field(self):
        Height = jschema.Number(id='height', maximum=200.)
        expected_schema = {'maximum': 200., 'id': 'height', 'type': 'number'}
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_exclusive_maximum_field(self):
        Height = jschema.Number(
            id='height', maximum=200., exclusive_maximum=True
        )
        expected_schema = {
            'maximum': 200.,
            'exclusiveMaximum': True,
            'id': 'height',
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_minimum_field(self):
        Height = jschema.Number(id='height', minimum=10.)
        expected_schema = {'minimum': 10., 'id': 'height', 'type': 'number'}
        self.assertEqual(expected_schema, Height.jschema.asdict())

    def test_exclusive_minimum_field(self):
        Height = jschema.Number(
            id='height', minimum=10., exclusive_minimum=False
        )
        expected_schema = {
            'minimum': 10.,
            'exclusiveMinimum': False,
            'id': 'height',
            'type': 'number'
        }
        self.assertEqual(expected_schema, Height.jschema.asdict())


class TestObject(JSchemaTestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_id_field_required(self):
        with self.assertRaisesDefinitionError("'id' field is required"):
            jschema.Object()

    def test_schema_field(self):
        Hat = jschema.Object(id='hat', schema='http://json-schema.org/schema#')
        expected_schema = {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_title_field(self):
        Hat = jschema.Object(id='hat', title='Hat')
        expected_schema = {'title': 'Hat', 'id': 'hat', 'type': 'object'}
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_description_field(self):
        Hat = jschema.Object(id='hat', description='A type of hat')
        expected_schema = {
            'description': 'A type of hat', 'id': 'hat', 'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_max_properties_field(self):
        Hat = jschema.Object(id='hat', max_properties=2)
        expected_schema = {'maxProperties': 2, 'id': 'hat', 'type': 'object'}
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_min_properties_field(self):
        Hat = jschema.Object(id='hat', min_properties=1)
        expected_schema = {'minProperties': 1, 'id': 'hat', 'type': 'object'}
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_required_field(self):
        Hat = jschema.Object(
            id='hat',
            properties=jschema.Properties(
                size=jschema.Integer(id='size', required=True)
            )
        )
        expected_schema = {
            'required': ['size'],
            'properties': {'size': {'id': 'size', 'type': 'integer'}},
            'id': 'hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_additional_properties_field_as_boolean(self):
        Hat = jschema.Object(id='hat', additional_properties=True)
        expected_schema = {
            'additionalProperties': True, 'id': 'hat', 'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_additional_properties_field_as_object(self):
        Hat = jschema.Object(
            id='hat',
            additional_properties=jschema.Object(id='additionalHatProperties')
        )
        expected_schema = {
            'additionalProperties': {
                'id': 'additionalHatProperties', 'type': 'object'
            },
            'id': 'hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_properties_field(self):
        Hat = jschema.Object(
            id='hat',
            properties=jschema.Properties(size=jschema.Object(id='size'))
        )
        expected_schema = {
            'properties': {'size': {'id': 'size', 'type': 'object'}},
            'id': 'hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_pattern_properties_field(self):
        Hat = jschema.Object(
            id='hat',
            pattern_properties={'^hat_.*$': jschema.Object(id='hatProperty')}
        )
        expected_schema = {
            'patternProperties': {
                '^hat_.*$': {'id': 'hatProperty', 'type': 'object'}
            },
            'id': 'hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_schema_dependency(self):
        Hat = jschema.Object(
            id='hat',
            dependencies=jschema.Dependencies(
                color=jschema.Object(
                    id='color',
                    properties=jschema.Properties(
                        size=jschema.Integer(id='size')
                    )
                )
            )
        )
        expected_schema = {
            'dependencies': {
                'color': {
                    'properties': {'size': {'id': 'size', 'type': 'integer'}},
                    'id': 'color',
                    'type': 'object'
                }
            },
            'id': 'hat',
            'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())

    def test_dependencies_field_as_property_dependency(self):
        Hat = jschema.Object(
            id='hat', dependencies=jschema.Dependencies(color=['size'])
        )
        expected_schema = {
            'dependencies': {'color': ['size']}, 'id': 'hat', 'type': 'object'
        }
        self.assertEqual(expected_schema, Hat.jschema.asdict())


class TestString(JSchemaTestCase):
    """
    definitions             # all
    enum                    # all
    allOf                   # all
    anyOf                   # all
    oneOf                   # all
    not                     # all

    """
    def test_id_field_required(self):
        with self.assertRaisesDefinitionError("'id' field is required"):
            jschema.String()

    def test_schema_field(self):
        Name = jschema.String(
            id='name', schema='http://json-schema.org/schema#'
        )
        expected_schema = {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'name',
            'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_title_field(self):
        Name = jschema.String(id='name', title='Name')
        expected_schema = {'title': 'Name', 'id': 'name', 'type': 'string'}
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_description_field(self):
        Name = jschema.String(id='name', description='Name or nickname')
        expected_schema = {
            'description': 'Name or nickname', 'id': 'name', 'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_default_field(self):
        Name = jschema.String(id='name', default='Anonymous')
        expected_schema = {
            'default': 'Anonymous', 'id': 'name', 'type': 'string'
        }
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_max_length_field(self):
        Name = jschema.String(id='name', max_length=32)
        expected_schema = {'maxLength': 32, 'id': 'name', 'type': 'string'}
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_min_length_field(self):
        Name = jschema.String(id='name', min_length=1)
        expected_schema = {'minLength': 1, 'id': 'name', 'type': 'string'}
        self.assertEqual(expected_schema, Name.jschema.asdict())

    def test_pattern_field(self):
        Name = jschema.String(id='name', pattern='.*')
        expected_schema = {'pattern': '.*', 'id': 'name', 'type': 'string'}
        self.assertEqual(expected_schema, Name.jschema.asdict())


if __name__ == '__main__':
    unittest.main()

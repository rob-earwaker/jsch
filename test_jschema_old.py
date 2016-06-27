import re
import unittest

import jschema_old


class JSchemaTestCase(unittest.TestCase):
    def assertFailsValidation(self, message):
        return self.assertRaisesRegexp(
            jschema_old.JsonSchemaValidationError, re.escape(message)
        )

    def assertInvalidDefinition(self, message):
        return self.assertRaisesRegexp(
            jschema_old.JsonSchemaDefinitionError, re.escape(message)
        )


class TestClass(JSchemaTestCase):
    def test_max_properties_invalid_type_definition(self):
        message = "invalid definition ['max_properties' must be int]: 'fuel'"
        with self.assertInvalidDefinition(message):
            class Engine(jschema_old.Class):
                max_properties = 'fuel'

    def test_max_properties_invalid_value_definition(self):
        message = "invalid definition ['max_properties' must be >= 0]: -1"
        with self.assertInvalidDefinition(message):
            class Engine(jschema_old.Class):
                max_properties = -1

    def test_max_properties_validation(self):
        class Engine(jschema_old.Class):
            max_properties = 1
        engine = Engine()
        engine.piston = 'solid'
        message = "invalid object [max_properties=1]"
        with self.assertFailsValidation(message):
            engine.crank = 'twist'

    def test_min_properties_invalid_type_definition(self):
        message = "invalid definition ['min_properties' must be int]: 'fuel'"
        with self.assertInvalidDefinition(message):
            class Engine(jschema_old.Class):
                min_properties = 'fuel'

    def test_min_properties_invalid_value_definition(self):
        message = "invalid definition ['min_properties' must be >= 0]: -1"
        with self.assertInvalidDefinition(message):
            class Engine(jschema_old.Class):
                min_properties = -1

    def test_min_properties_validation(self):
        class Engine(jschema_old.Class):
            min_properties = 1
        message = "invalid object [min_properties=1]"
        with self.assertFailsValidation(message):
            Engine()

    def test_required_invalid_type_definition(self):
        message = "invalid definition ['required' must be list]: 1"
        with self.assertInvalidDefinition(message):
            class Engine(jschema_old.Class):
                required = 1

    def test_required_invalid_item_type_definition(self):
        message = "invalid definition ['required' items must be str]: 2"
        with self.assertInvalidDefinition(message):
            class Engine(jschema_old.Class):
                required = ['piston', 2]

    def test_empty_required_list_invalid_definition(self):
        message = "invalid definition [length of 'required' must be >= 1]: []"
        with self.assertInvalidDefinition(message):
            class Engine(jschema_old.Class):
                required = []

    def test_required_duplicate_items_invalid_definition(self):
        message = (
            "invalid definition ['required' items must be unique]: "
            "['piston', 'crank', 'piston']"
        )
        with self.assertInvalidDefinition(message):
            class Engine(jschema_old.Class):
                required = ['piston', 'crank', 'piston']

    def test_required_validation(self):
        class Engine(jschema_old.Class):
            required = ['piston']
        message = "invalid object [required=['piston']]"
        with self.assertFailsValidation(message):
            Engine()

    def test_schema_with_max_properties(self):
        class Engine(jschema_old.Class):
            max_properties = 1
        self.assertEqual(
            {'maxProperties': 1, 'type': 'object'}, Engine.jschema
        )

    def test_schema_with_min_properties(self):
        class Engine(jschema_old.Class):
            min_properties = 1
        self.assertEqual(
            {'minProperties': 1, 'type': 'object'}, Engine.jschema
        )


class TestObject(JSchemaTestCase):
    def test_init_with_value(self):
        class Engine(jschema_old.Class):
            pass

        class Car(jschema_old.Class):
            engine = jschema_old.Object(Engine)
        engine = Engine()
        self.assertEqual(engine, Car(engine=engine).engine)

    def test_schema_with_no_validation_fields(self):
        class Engine(jschema_old.Class):
            pass

        class Car(jschema_old.Class):
            engine = jschema_old.Object(Engine)
        schema = Car.jschema['properties']['engine']
        self.assertEqual({'type': 'object'}, schema)

    def test_schema_with_max_properties(self):
        class Engine(jschema_old.Class):
            max_properties = 2

        class Car(jschema_old.Class):
            engine = jschema_old.Object(Engine)
        schema = Car.jschema['properties']['engine']
        self.assertEqual({'maxProperties': 2, 'type': 'object'}, schema)


class TestString(JSchemaTestCase):
    def test_init_with_value(self):
        class Person(jschema_old.Class):
            name = jschema_old.String()
        self.assertEqual('Bob', Person(name='Bob').name)

    def test_init_without_value(self):
        class Person(jschema_old.Class):
            name = jschema_old.String()
        self.assertIsNone(Person().name)

    def test_type_validation(self):
        class Person(jschema_old.Class):
            name = jschema_old.String()
        message = "invalid string: 12"
        with self.assertFailsValidation(message):
            Person().name = 12

    def test_max_length_invalid_type_definition(self):
        message = "invalid definition ['max_length' must be int]: 'Bob'"
        with self.assertInvalidDefinition(message):
            class Person(jschema_old.Class):
                name = jschema_old.String(max_length='Bob')

    def test_max_length_invalid_value_definition(self):
        message = "invalid definition ['max_length' must be >= 0]: -1"
        with self.assertInvalidDefinition(message):
            class Person(jschema_old.Class):
                name = jschema_old.String(max_length=-1)

    def test_max_length_validation(self):
        class Person(jschema_old.Class):
            name = jschema_old.String(max_length=10)
        message = "invalid string [max_length=10]: 'Michaelangelo'"
        with self.assertFailsValidation(message):
            Person().name = 'Michaelangelo'

    def test_min_length_invalid_type_definition(self):
        message = "invalid definition ['min_length' must be int]: 'Bob'"
        with self.assertInvalidDefinition(message):
            class Person(jschema_old.Class):
                name = jschema_old.String(min_length='Bob')

    def test_min_length_invalid_value_definition(self):
        message = "invalid definition ['min_length' must be >= 0]: -1"
        with self.assertInvalidDefinition(message):
            class Person(jschema_old.Class):
                name = jschema_old.String(min_length=-1)

    def test_min_length_validation(self):
        class Person(jschema_old.Class):
            name = jschema_old.String(min_length=5)
        message = "invalid string [min_length=5]: 'Bob'"
        with self.assertFailsValidation(message):
            Person().name = 'Bob'

    def test_pattern_validation(self):
        class Person(jschema_old.Class):
            name = jschema_old.String(pattern='^B')
        message = "invalid string [pattern='^B']: 'Dave'"
        with self.assertFailsValidation(message):
            Person().name = 'Dave'

    def test_schema_with_no_validation_fields(self):
        class Person(jschema_old.Class):
            name = jschema_old.String()
        schema = Person.jschema['properties']['name']
        self.assertEqual({'type': 'string'}, schema)

    def test_schema_with_max_length(self):
        class Person(jschema_old.Class):
            name = jschema_old.String(max_length=10)
        schema = Person.jschema['properties']['name']
        self.assertEqual({'maxLength': 10, 'type': 'string'}, schema)

    def test_schema_with_min_length(self):
        class Person(jschema_old.Class):
            name = jschema_old.String(min_length=5)
        schema = Person.jschema['properties']['name']
        self.assertEqual({'minLength': 5, 'type': 'string'}, schema)

    def test_schema_with_pattern(self):
        class Person(jschema_old.Class):
            name = jschema_old.String(pattern='^B')
        schema = Person.jschema['properties']['name']
        self.assertEqual({'pattern': '^B', 'type': 'string'}, schema)


class TestInteger(JSchemaTestCase):
    def test_init_with_value(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer()
        self.assertEqual(23, Person(age=23).age)

    def test_init_without_value(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer()
        self.assertIsNone(Person().age)

    def test_type_validation(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer()
        message = "invalid integer: 0.7"
        with self.assertFailsValidation(message):
            Person().age = 0.7

    def test_multiple_of_validation(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(multiple_of=7)
        message = "invalid integer [multiple_of=7]: 12"
        with self.assertFailsValidation(message):
            Person().age = 12

    def test_maximum_validation(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(maximum=23)
        message = "invalid integer [maximum=23]: 35"
        with self.assertFailsValidation(message):
            Person().age = 35

    def test_exclusive_maximum_validation(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(maximum=23, exclusive_maximum=True)
        message = "invalid integer [maximum=23, exclusive_maximum=True]: 23"
        with self.assertFailsValidation(message):
            Person().age = 23

    def test_minimum_validation(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(minimum=18)
        message = "invalid integer [minimum=18]: 10"
        with self.assertFailsValidation(message):
            Person().age = 10

    def test_exclusive_minimum_validation(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(minimum=18, exclusive_minimum=True)
        message = "invalid integer [minimum=18, exclusive_minimum=True]: 18"
        with self.assertFailsValidation(message):
            Person().age = 18

    def test_schema_with_no_validation_fields(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer()
        schema = Person.jschema['properties']['age']
        self.assertEqual({'type': 'integer'}, schema)

    def test_schema_with_multiple_of(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(multiple_of=7)
        schema = Person.jschema['properties']['age']
        self.assertEqual({'multipleOf': 7, 'type': 'integer'}, schema)

    def test_schema_with_maximum(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(maximum=23)
        schema = Person.jschema['properties']['age']
        self.assertEqual({'maximum': 23, 'type': 'integer'}, schema)

    def test_schema_with_exclusive_maximum(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(maximum=23, exclusive_maximum=True)
        schema = Person.jschema['properties']['age']
        self.assertEqual(
            {'exclusiveMaximum': True, 'maximum': 23, 'type': 'integer'},
            schema
        )

    def test_schema_with_minimum(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(minimum=18)
        schema = Person.jschema['properties']['age']
        self.assertEqual({'minimum': 18, 'type': 'integer'}, schema)

    def test_schema_with_exclusive_minimum(self):
        class Person(jschema_old.Class):
            age = jschema_old.Integer(minimum=18, exclusive_minimum=True)
        schema = Person.jschema['properties']['age']
        self.assertEqual(
            {'exclusiveMinimum': True, 'minimum': 18, 'type': 'integer'},
            schema
        )


if __name__ == '__main__':
    unittest.main()

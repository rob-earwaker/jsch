import re
import unittest

import jschema


class JSchemaTestCase(unittest.TestCase):
    def assertFailsValidation(self, message):
        return self.assertRaisesRegexp(
            jschema.JsonSchemaValidationError, re.escape(message)
        )

    def assertInvalidDefinition(self, message):
        return self.assertRaisesRegexp(
            jschema.JsonSchemaDefinitionError, re.escape(message)
        )


class TestClass(JSchemaTestCase):
    def test_schema_with_max_properties(self):
        class Engine(jschema.Class):
            max_properties = 1
        self.assertEqual(
            {'maxProperties': 1, 'type': 'object'}, Engine.jschema
        )

    def test_max_properties_invalid_type_definition(self):
        message = "invalid definition [max_properties must be int]: 'fuel'"
        with self.assertInvalidDefinition(message):
            class Engine(jschema.Class):
                max_properties = 'fuel'

    def test_max_properties_invalid_value_definition(self):
        message = "invalid definition [max_properties must be >= 0]: -1"
        with self.assertInvalidDefinition(message):
            class Engine(jschema.Class):
                max_properties = -1


class TestObject(JSchemaTestCase):
    def test_init_with_value(self):
        class Engine(jschema.Class):
            pass

        class Car(jschema.Class):
            engine = jschema.Object(Engine)
        engine = Engine()
        self.assertEqual(engine, Car(engine=engine).engine)

    def test_schema_with_no_validation_fields(self):
        class Engine(jschema.Class):
            pass

        class Car(jschema.Class):
            engine = jschema.Object(Engine)
        schema = Car.jschema['properties']['engine']
        self.assertEqual({'type': 'object'}, schema)

    def test_schema_with_max_properties(self):
        class Engine(jschema.Class):
            max_properties = 2

        class Car(jschema.Class):
            engine = jschema.Object(Engine)
        schema = Car.jschema['properties']['engine']
        self.assertEqual({'maxProperties': 2, 'type': 'object'}, schema)


class TestString(JSchemaTestCase):
    def test_init_with_value(self):
        class Person(jschema.Class):
            name = jschema.String()
        self.assertEqual('Bob', Person(name='Bob').name)

    def test_init_without_value(self):
        class Person(jschema.Class):
            name = jschema.String()
        self.assertIsNone(Person().name)

    def test_type_validation(self):
        class Person(jschema.Class):
            name = jschema.String()
        message = "invalid string: 12"
        with self.assertFailsValidation(message):
            Person().name = 12

    def test_max_length_invalid_type_definition(self):
        message = "invalid definition [max_length must be int]: 'Bob'"
        with self.assertInvalidDefinition(message):
            class Person(jschema.Class):
                name = jschema.String(max_length='Bob')

    def test_max_length_invalid_value_definition(self):
        message = "invalid definition [max_length must be >= 0]: -1"
        with self.assertInvalidDefinition(message):
            class Person(jschema.Class):
                name = jschema.String(max_length=-1)

    def test_max_length_validation(self):
        class Person(jschema.Class):
            name = jschema.String(max_length=10)
        message = "invalid string [max_length=10]: 'Michaelangelo'"
        with self.assertFailsValidation(message):
            Person().name = 'Michaelangelo'

    def test_min_length_invalid_type_definition(self):
        message = "invalid definition [min_length must be int]: 'Bob'"
        with self.assertInvalidDefinition(message):
            class Person(jschema.Class):
                name = jschema.String(min_length='Bob')

    def test_min_length_invalid_value_definition(self):
        message = "invalid definition [min_length must be >= 0]: -1"
        with self.assertInvalidDefinition(message):
            class Person(jschema.Class):
                name = jschema.String(min_length=-1)

    def test_min_length_validation(self):
        class Person(jschema.Class):
            name = jschema.String(min_length=5)
        message = "invalid string [min_length=5]: 'Bob'"
        with self.assertFailsValidation(message):
            Person().name = 'Bob'

    def test_pattern_validation(self):
        class Person(jschema.Class):
            name = jschema.String(pattern='^B')
        message = "invalid string [pattern='^B']: 'Dave'"
        with self.assertFailsValidation(message):
            Person().name = 'Dave'

    def test_schema_with_no_validation_fields(self):
        class Person(jschema.Class):
            name = jschema.String()
        schema = Person.jschema['properties']['name']
        self.assertEqual({'type': 'string'}, schema)

    def test_schema_with_max_length(self):
        class Person(jschema.Class):
            name = jschema.String(max_length=10)
        schema = Person.jschema['properties']['name']
        self.assertEqual({'maxLength': 10, 'type': 'string'}, schema)

    def test_schema_with_min_length(self):
        class Person(jschema.Class):
            name = jschema.String(min_length=5)
        schema = Person.jschema['properties']['name']
        self.assertEqual({'minLength': 5, 'type': 'string'}, schema)

    def test_schema_with_pattern(self):
        class Person(jschema.Class):
            name = jschema.String(pattern='^B')
        schema = Person.jschema['properties']['name']
        self.assertEqual({'pattern': '^B', 'type': 'string'}, schema)


class TestInteger(JSchemaTestCase):
    def test_init_with_value(self):
        class Person(jschema.Class):
            age = jschema.Integer()
        self.assertEqual(23, Person(age=23).age)

    def test_init_without_value(self):
        class Person(jschema.Class):
            age = jschema.Integer()
        self.assertIsNone(Person().age)

    def test_type_validation(self):
        class Person(jschema.Class):
            age = jschema.Integer()
        message = "invalid integer: 0.7"
        with self.assertFailsValidation(message):
            Person().age = 0.7

    def test_multiple_of_validation(self):
        class Person(jschema.Class):
            age = jschema.Integer(multiple_of=7)
        message = "invalid integer [multiple_of=7]: 12"
        with self.assertFailsValidation(message):
            Person().age = 12

    def test_maximum_validation(self):
        class Person(jschema.Class):
            age = jschema.Integer(maximum=23)
        message = "invalid integer [maximum=23]: 35"
        with self.assertFailsValidation(message):
            Person().age = 35

    def test_exclusive_maximum_validation(self):
        class Person(jschema.Class):
            age = jschema.Integer(maximum=23, exclusive_maximum=True)
        message = "invalid integer [maximum=23, exclusive_maximum=True]: 23"
        with self.assertFailsValidation(message):
            Person().age = 23

    def test_minimum_validation(self):
        class Person(jschema.Class):
            age = jschema.Integer(minimum=18)
        message = "invalid integer [minimum=18]: 10"
        with self.assertFailsValidation(message):
            Person().age = 10

    def test_exclusive_minimum_validation(self):
        class Person(jschema.Class):
            age = jschema.Integer(minimum=18, exclusive_minimum=True)
        message = "invalid integer [minimum=18, exclusive_minimum=True]: 18"
        with self.assertFailsValidation(message):
            Person().age = 18

    def test_schema_with_no_validation_fields(self):
        class Person(jschema.Class):
            age = jschema.Integer()
        schema = Person.jschema['properties']['age']
        self.assertEqual({'type': 'integer'}, schema)

    def test_schema_with_multiple_of(self):
        class Person(jschema.Class):
            age = jschema.Integer(multiple_of=7)
        schema = Person.jschema['properties']['age']
        self.assertEqual({'multipleOf': 7, 'type': 'integer'}, schema)

    def test_schema_with_maximum(self):
        class Person(jschema.Class):
            age = jschema.Integer(maximum=23)
        schema = Person.jschema['properties']['age']
        self.assertEqual({'maximum': 23, 'type': 'integer'}, schema)

    def test_schema_with_exclusive_maximum(self):
        class Person(jschema.Class):
            age = jschema.Integer(maximum=23, exclusive_maximum=True)
        schema = Person.jschema['properties']['age']
        self.assertEqual(
            {'exclusiveMaximum': True, 'maximum': 23, 'type': 'integer'},
            schema
        )

    def test_schema_with_minimum(self):
        class Person(jschema.Class):
            age = jschema.Integer(minimum=18)
        schema = Person.jschema['properties']['age']
        self.assertEqual({'minimum': 18, 'type': 'integer'}, schema)

    def test_schema_with_exclusive_minimum(self):
        class Person(jschema.Class):
            age = jschema.Integer(minimum=18, exclusive_minimum=True)
        schema = Person.jschema['properties']['age']
        self.assertEqual(
            {'exclusiveMinimum': True, 'minimum': 18, 'type': 'integer'},
            schema
        )


if __name__ == '__main__':
    unittest.main()

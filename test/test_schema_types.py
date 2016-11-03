import unittest

import jsch


class TestSchemaTypes(unittest.TestCase):
    def test_array_type_keyword(self):
        schema = jsch.Array()
        self.assertEqual('array', schema.type)

    def test_boolean_type_keyword(self):
        schema = jsch.Boolean()
        self.assertEqual('boolean', schema.type)

    def test_integer_type_keyword(self):
        schema = jsch.Integer()
        self.assertEqual('integer', schema.type)

    def test_null_type_keyword(self):
        schema = jsch.Null()
        self.assertEqual('null', schema.type)

    def test_number_type_keyword(self):
        schema = jsch.Number()
        self.assertEqual('number', schema.type)

    def test_object_type_keyword(self):
        schema = jsch.Object()
        self.assertEqual('object', schema.type)

    def test_string_type_keyword(self):
        schema = jsch.String()
        self.assertEqual('string', schema.type)

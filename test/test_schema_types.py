import unittest

import jsch


class TestArrayType(unittest.TestCase):
    def test_type_keyword(self):
        schema = jsch.Array()
        self.assertEqual('array', schema.type)


class TestBooleanType(unittest.TestCase):
    def test_type_keyword(self):
        schema = jsch.Boolean()
        self.assertEqual('boolean', schema.type)


class TestIntegerType(unittest.TestCase):
    def test_type_keyword(self):
        schema = jsch.Integer()
        self.assertEqual('integer', schema.type)


class TestNullType(unittest.TestCase):
    def test_type_keyword(self):
        schema = jsch.Null()
        self.assertEqual('null', schema.type)


class TestNumberType(unittest.TestCase):
    def test_type_keyword(self):
        schema = jsch.Number()
        self.assertEqual('number', schema.type)


class TestObjectType(unittest.TestCase):
    def test_type_keyword(self):
        schema = jsch.Object()
        self.assertEqual('object', schema.type)


class TestStringType(unittest.TestCase):
    def test_type_keyword(self):
        schema = jsch.String()
        self.assertEqual('string', schema.type)

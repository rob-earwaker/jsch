import unittest

import jschema


class JSchemaTestCase(unittest.TestCase):
    def assertDefinitionError(self, message):
        return self.assertRaisesRegex(jschema.DefinitionError, message)


class TestJSchema(JSchemaTestCase):
    def test_max_items_not_integer(self):
        message = "'max_items' must be an integer"
        with self.assertDefinitionError(message):
            jschema.JSchema(max_items=0.5)

    def test_max_items_lt_zero(self):
        message = "'max_items' must be gte zero"
        with self.assertDefinitionError(message):
            jschema.JSchema(max_items=-1)

    def test_minimum_not_number(self):
        message = "'minimum' must be a number"
        with self.assertDefinitionError(message):
            jschema.JSchema(minimum='5')

    def test_exclusive_minimum_not_bool(self):
        message = "'exclusive_minimum' must be a boolean"
        with self.assertDefinitionError(message):
            jschema.JSchema(minimum=1, exclusive_minimum='True')

    def test_exclusive_minimum_without_minimum(self):
        message = "'minimum' must be present if 'exclusive_minimum' is defined"
        with self.assertDefinitionError(message):
            jschema.JSchema(exclusive_minimum=True)

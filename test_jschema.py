import unittest

import jschema


class JSchemaTestCase(unittest.TestCase):
    def assertDefinitionError(self, message):
        return self.assertRaisesRegex(jschema.DefinitionError, message)


class TestJSchema(JSchemaTestCase):
    def test_max_items_not_int(self):
        message = "'max_items' must be an int"
        with self.assertDefinitionError(message):
            jschema.JSchema(max_items=0.5)

    def test_max_items_less_than_zero(self):
        message = "'max_items' must be greater than or equal to zero"
        with self.assertDefinitionError(message):
            jschema.JSchema(max_items=-1)

    def test_min_items_not_int(self):
        message = "'min_items' must be an int"
        with self.assertDefinitionError(message):
            jschema.JSchema(min_items=0.5)

    def test_min_items_less_than_zero(self):
        message = "'min_items' must be greater than or equal to zero"
        with self.assertDefinitionError(message):
            jschema.JSchema(min_items=-1)

    def test_maximum_not_int_or_float(self):
        message = "'maximum' must be an int or float"
        with self.assertDefinitionError(message):
            jschema.JSchema(maximum='5')

    def test_exclusive_maximum_not_bool(self):
        message = "'exclusive_maximum' must be a bool"
        with self.assertDefinitionError(message):
            jschema.JSchema(maximum=1, exclusive_maximum='True')

    def test_exclusive_maximum_without_maximum(self):
        message = "'maximum' must be present if 'exclusive_maximum' is defined"
        with self.assertDefinitionError(message):
            jschema.JSchema(exclusive_maximum=True)

    def test_minimum_not_int_or_float(self):
        message = "'minimum' must be an int or float"
        with self.assertDefinitionError(message):
            jschema.JSchema(minimum='5')

    def test_exclusive_minimum_not_bool(self):
        message = "'exclusive_minimum' must be a bool"
        with self.assertDefinitionError(message):
            jschema.JSchema(minimum=1, exclusive_minimum='True')

    def test_exclusive_minimum_without_minimum(self):
        message = "'minimum' must be present if 'exclusive_minimum' is defined"
        with self.assertDefinitionError(message):
            jschema.JSchema(exclusive_minimum=True)

    def test_multiple_of_not_int_or_float(self):
        message = "'multiple_of' must be an int or float"
        with self.assertDefinitionError(message):
            jschema.JSchema(multiple_of='2.3')

    def test_max_length_not_int(self):
        message = "'max_length' must be an int"
        with self.assertDefinitionError(message):
            jschema.JSchema(max_length=0.5)

    def test_max_length_less_than_zero(self):
        message = "'max_length' must be greater than or equal to zero"
        with self.assertDefinitionError(message):
            jschema.JSchema(max_length=-1)

    def test_min_length_not_int(self):
        message = "'min_length' must be an int"
        with self.assertDefinitionError(message):
            jschema.JSchema(min_length=0.5)

    def test_min_length_less_than_zero(self):
        message = "'min_length' must be greater than or equal to zero"
        with self.assertDefinitionError(message):
            jschema.JSchema(min_length=-1)

    def test_pattern_not_str(self):
        message = "'pattern' must be a str"
        with self.assertDefinitionError(message):
            jschema.JSchema(pattern=8)

    def test_additional_items_not_bool_or_schema(self):
        message = "'additional_items' must be a bool or a schema"
        with self.assertDefinitionError(message):
            jschema.JSchema(additional_items='False')

    def test_items_not_schema_or_list(self):
        message = "'items' must be a schema or a list"
        with self.assertDefinitionError(message):
            jschema.JSchema(items=9.6)

    def test_items_list_item_not_schema(self):
        message = "'items' list must contain only schemas"
        with self.assertDefinitionError(message):
            jschema.JSchema(items=[jschema.JSchema(), '{}'])

    def test_unique_items_not_bool(self):
        message = "'unique_items' must be a bool"
        with self.assertDefinitionError(message):
            jschema.JSchema(unique_items='True')

    def test_max_properties_not_int(self):
        message = "'max_properties' must be an int"
        with self.assertDefinitionError(message):
            jschema.JSchema(max_properties=0.5)

    def test_max_properties_less_than_zero(self):
        message = "'max_properties' must be greater than or equal to zero"
        with self.assertDefinitionError(message):
            jschema.JSchema(max_properties=-1)

    def test_min_properties_not_int(self):
        message = "'min_properties' must be an int"
        with self.assertDefinitionError(message):
            jschema.JSchema(min_properties=0.5)

    def test_min_properties_less_than_zero(self):
        message = "'min_properties' must be greater than or equal to zero"
        with self.assertDefinitionError(message):
            jschema.JSchema(min_properties=-1)

    def test_required_not_list(self):
        message = "'required' must be a list"
        with self.assertDefinitionError(message):
            jschema.JSchema(required='[]')

    def test_required_list_empty(self):
        message = "'required' list must have at least one item"
        with self.assertDefinitionError(message):
            jschema.JSchema(required=[])

    def test_required_list_item_not_str(self):
        message = "'required' list item must be a str"
        with self.assertDefinitionError(message):
            jschema.JSchema(required=[8])

    def test_required_list_with_duplicates(self):
        message = "'required' list items must be unique"
        with self.assertDefinitionError(message):
            jschema.JSchema(required=['a', 'b', 'c', 'a'])

    def test_additional_properties_not_bool_or_schema(self):
        message = "'additional_properties' must be a bool or a schema"
        with self.assertDefinitionError(message):
            jschema.JSchema(additional_properties='False')

    def test_properties_not_dict(self):
        message = "'properties' must be a dict"
        with self.assertDefinitionError(message):
            jschema.JSchema(properties=[9])

    def test_properties_dict_key_not_str(self):
        message = "'properties' dict key must be a str"
        with self.assertDefinitionError(message):
            jschema.JSchema(properties={8: jschema.JSchema()})

    def test_properties_dict_value_not_schema(self):
        message = "'properties' dict value must be a schema"
        with self.assertDefinitionError(message):
            jschema.JSchema(properties={'name': '{}'})

    def test_pattern_properties_not_dict(self):
        message = "'pattern_properties' must be a dict"
        with self.assertDefinitionError(message):
            jschema.JSchema(pattern_properties=[9])

    def test_pattern_properties_dict_key_not_str(self):
        message = "'pattern_properties' dict key must be a str"
        with self.assertDefinitionError(message):
            jschema.JSchema(pattern_properties={8: jschema.JSchema()})

    def test_pattern_properties_dict_value_not_schema(self):
        message = "'pattern_properties' dict value must be a schema"
        with self.assertDefinitionError(message):
            jschema.JSchema(pattern_properties={'name': '{}'})

    def test_type_not_str_or_list(self):
        message = "'type' must be a str or a list"
        with self.assertDefinitionError(message):
            jschema.JSchema(type=45)

    def test_type_str_not_primitive_type(self):
        message = "'type' str must be a primitive type"
        with self.assertDefinitionError(message):
            jschema.JSchema(type='float')

    def test_type_list_item_not_str(self):
        message = "'type' list item must be a str"
        with self.assertDefinitionError(message):
            jschema.JSchema(type=['string', 7])

    def test_type_list_item_not_primitive_type(self):
        message = "'type' list item must be a primitive type"
        with self.assertDefinitionError(message):
            jschema.JSchema(type=['string', 'float'])

    def test_type_list_items_not_unique(self):
        message = "'type' list items must be unique"
        with self.assertDefinitionError(message):
            jschema.JSchema(type=['string', 'null', 'null'])

    def test_additional_items_as_bool(self):
        jschema.JSchema(additional_items=True)

    def test_additional_items_as_schema(self):
        jschema.JSchema(additional_items=jschema.JSchema())

    def test_items_as_schema(self):
        jschema.JSchema(items=jschema.JSchema())

    def test_items_as_list(self):
        jschema.JSchema(items=[jschema.JSchema(), jschema.JSchema()])

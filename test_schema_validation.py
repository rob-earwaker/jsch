import unittest

import jschema


class SchemaValidationTestCase(unittest.TestCase):
    def assertRaisesSchemaValidationError(self, message):
        regex = '^{0}$'.format(message)
        return self.assertRaisesRegex(jschema.SchemaValidationError, regex)


class TestAdditionalItemsValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jschema.JSchema(additional_items=True)

    def test_passes_when_schema(self):
        jschema.JSchema(additional_items=jschema.JSchema())

    def test_fails_when_not_bool_or_schema(self):
        message = "'additional_items' must be a bool or a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(additional_items='False')


class TestAdditionalPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jschema.JSchema(additional_properties=True)

    def test_passes_when_schema(self):
        jschema.JSchema(additional_properties=jschema.JSchema())

    def test_fails_when_not_bool_or_schema(self):
        message = "'additional_properties' must be a bool or a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(additional_properties='False')


class TestAllOfValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jschema.JSchema(all_of=[jschema.JSchema(), jschema.JSchema()])

    def test_fails_when_not_list(self):
        message = "'all_of' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(all_of='[]')

    def test_fails_when_list_empty(self):
        message = "'all_of' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(all_of=[])

    def test_fails_when_list_item_not_schema(self):
        message = "'all_of' list item must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(all_of=[jschema.JSchema(), '{}'])


class TestAnyOfValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jschema.JSchema(any_of=[jschema.JSchema(), jschema.JSchema()])

    def test_fails_when_not_list(self):
        message = "'any_of' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(any_of='[]')

    def test_fails_when_list_empty(self):
        message = "'any_of' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(any_of=[])

    def test_fails_when_list_item_not_schema(self):
        message = "'any_of' list item must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(any_of=[jschema.JSchema(), '{}'])


class TestDefinitionsValidation(SchemaValidationTestCase):
    def test_passes_when_dict(self):
        jschema.JSchema(definitions={'name': jschema.JSchema()})

    def test_fails_when_not_dict(self):
        message = "'definitions' must be a dict"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(definitions=True)

    def test_fails_when_dict_key_not_str(self):
        message = "'definitions' dict key must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(definitions={7: jschema.JSchema()})

    def test_fails_when_dict_value_not_schema(self):
        message = "'definitions' dict value must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(definitions={'name': '{}'})


class TestDependenciesValidation(SchemaValidationTestCase):
    def test_passes_when_dict_with_schema_values(self):
        jschema.JSchema(dependencies={'name': jschema.JSchema()})

    def test_passes_when_dict_with_list_values(self):
        jschema.JSchema(dependencies={'name': ['age', 'height']})

    def test_fails_when_not_dict(self):
        message = "'dependencies' must be a dict"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(dependencies=['name'])

    def test_fails_when_dict_key_not_str(self):
        message = "'dependencies' dict key must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(dependencies={7: jschema.JSchema()})

    def test_fails_when_dict_value_not_schema_or_list(self):
        message = "'dependencies' dict value must be a schema or a list"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(dependencies={'name': False})

    def test_fails_when_dict_list_value_empty(self):
        message = "'dependencies' dict value list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(dependencies={'name': []})

    def test_fails_when_dict_list_value_item_not_str(self):
        message = "'dependencies' dict value list item must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(dependencies={'name': [7]})

    def test_fails_when_dict_list_value_item_str_not_unique(self):
        message = "'dependencies' dict value list item str must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(dependencies={'name': ['a', 'b', 'a']})


class TestEnumValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jschema.JSchema(enum=['name', True, None, 8, {}, ['a']])

    def test_fails_when_not_list(self):
        message = "'enum' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum='[]')

    def test_fails_when_list_empty(self):
        message = "'enum' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=[])

    def test_fails_when_list_item_not_primitive_type(self):
        message = "'enum' list item must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=[{'a', 'b'}])

    def test_fails_when_list_item_list_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=[['a', 'b'], ['a', 'b'], ['b', 'c']])

    def test_fails_when_list_item_bool_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=[True, True, False])

    def test_fails_when_list_item_int_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=[5, 5, 67])

    def test_fails_when_list_item_null_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=[None, None])

    def test_fails_when_list_item_float_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=[4.8, 4.8, 1.9])

    def test_fails_when_list_item_dict_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=[{'a': 'b'}, {'a': 'b'}, {'b': 'c'}])

    def test_fails_when_list_item_str_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(enum=['name', 'name', 'age'])


class TestExclusiveMaximumValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jschema.JSchema(maximum=1, exclusive_maximum=True)

    def test_fails_when_not_bool(self):
        message = "'exclusive_maximum' must be a bool"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(maximum=1, exclusive_maximum='True')


class TestExclusiveMinimumValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jschema.JSchema(minimum=1, exclusive_minimum=True)

    def test_fails_when_not_bool(self):
        message = "'exclusive_minimum' must be a bool"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(minimum=1, exclusive_minimum='True')


class TestItemsValidation(SchemaValidationTestCase):
    def test_passes_when_schema(self):
        jschema.JSchema(items=jschema.JSchema())

    def test_passes_when_list(self):
        jschema.JSchema(items=[jschema.JSchema(), jschema.JSchema()])

    def test_fails_when_not_schema_or_list(self):
        message = "'items' must be a schema or a list"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(items=9.6)

    def test_fails_when_list_item_not_schema(self):
        message = "'items' list must contain only schemas"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(items=[jschema.JSchema(), '{}'])


class TestMaximumValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(maximum=5)

    def test_passes_when_float(self):
        jschema.JSchema(maximum=7.6)

    def test_fails_when_not_int_or_float(self):
        message = "'maximum' must be an int or float"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(maximum='5')

    def test_fails_when_not_present_with_exclusive_maximum_defined(self):
        message = "'maximum' must be present if 'exclusive_maximum' is defined"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(exclusive_maximum=True)


class TestMaxItemsValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(max_items=5)

    def test_fails_when_not_int(self):
        message = "'max_items' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(max_items=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'max_items' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(max_items=-1)


class TestMaxLengthValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(max_length=5)

    def test_fails_when_not_int(self):
        message = "'max_length' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(max_length=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'max_length' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(max_length=-1)


class TestMaxPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(max_properties=5)

    def test_fails_when_not_int(self):
        message = "'max_properties' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(max_properties=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'max_properties' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(max_properties=-1)


class TestMinimumValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(minimum=5)

    def test_passes_when_float(self):
        jschema.JSchema(minimum=7.6)

    def test_fails_when_not_int_or_float(self):
        message = "'minimum' must be an int or float"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(minimum='5')

    def test_fails_when_not_present_with_exclusive_minimum_defined(self):
        message = "'minimum' must be present if 'exclusive_minimum' is defined"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(exclusive_minimum=True)


class TestMinItemsValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(min_items=5)

    def test_fails_when_not_int(self):
        message = "'min_items' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(min_items=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'min_items' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(min_items=-1)


class TestMinLengthValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(min_length=5)

    def test_fails_when_not_int(self):
        message = "'min_length' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(min_length=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'min_length' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(min_length=-1)


class TestMinPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(min_properties=5)

    def test_fails_when_not_int(self):
        message = "'min_properties' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(min_properties=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'min_properties' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(min_properties=-1)


class TestMultipleOfValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jschema.JSchema(multiple_of=5)

    def test_passes_when_float(self):
        jschema.JSchema(multiple_of=7.6)

    def test_fails_when_not_int_or_float(self):
        message = "'multiple_of' must be an int or float"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(multiple_of='2.3')

    def test_fails_when_not_greater_then_zero(self):
        message = "'multiple_of' must be greater than zero"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(multiple_of=0)


class TestNotValidation(SchemaValidationTestCase):
    def test_passes_when_schema(self):
        jschema.JSchema(not_=jschema.JSchema())

    def test_fails_when_not_schema(self):
        message = "'not_' must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(not_='{}')


class TestOneOfValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jschema.JSchema(one_of=[jschema.JSchema(), jschema.JSchema()])

    def test_fails_when_not_list(self):
        message = "'one_of' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(one_of='[]')

    def test_fails_when_list_empty(self):
        message = "'one_of' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(one_of=[])

    def test_fails_when_list_item_not_schema(self):
        message = "'one_of' list item must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(one_of=[jschema.JSchema(), '{}'])


class TestPatternValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jschema.JSchema(pattern='^name$')

    def test_fails_when_not_str(self):
        message = "'pattern' must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(pattern=8)


class TestPatternPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_dict(self):
        jschema.JSchema(pattern_properties={'^name$': jschema.JSchema()})

    def test_fails_when_not_dict(self):
        message = "'pattern_properties' must be a dict"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(pattern_properties=[9])

    def test_fails_when_dict_key_not_str(self):
        message = "'pattern_properties' dict key must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(pattern_properties={8: jschema.JSchema()})

    def test_fails_when_dict_value_not_schema(self):
        message = "'pattern_properties' dict value must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(pattern_properties={'name': '{}'})


class TestPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_dict(self):
        jschema.JSchema(properties={'name': jschema.JSchema()})

    def test_fails_when_not_dict(self):
        message = "'properties' must be a dict"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(properties=[9])

    def test_fails_when_dict_key_not_str(self):
        message = "'properties' dict key must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(properties={8: jschema.JSchema()})

    def test_fails_when_dict_value_not_schema(self):
        message = "'properties' dict value must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(properties={'name': '{}'})


class TestRequiredValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jschema.JSchema(required=['name', 'age'])

    def test_fails_when_not_list(self):
        message = "'required' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(required='[]')

    def test_fails_when_list_empty(self):
        message = "'required' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(required=[])

    def test_fails_when_list_item_not_str(self):
        message = "'required' list item must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(required=[8])

    def test_fails_when_list_str_item_not_unique(self):
        message = "'required' list item str must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(required=['a', 'b', 'c', 'a'])


class TestSchemaValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jschema.JSchema().asdict(root=True, schema='http://jschema.org/sch#')

    def test_fails_when_not_str(self):
        message = "'schema' must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema().asdict(root=True, schema=76)


class TestTypeValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jschema.JSchema(type='number')

    def test_passes_when_list(self):
        jschema.JSchema(type=['array', 'object', 'integer', 'null', 'string'])

    def test_fails_when_not_str_or_list(self):
        message = "'type' must be a str or a list"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(type=45)

    def test_fails_when_str_not_primitive_type(self):
        message = "'type' str must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(type='float')

    def test_fails_when_list_item_not_str(self):
        message = "'type' list item must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(type=['string', 7])

    def test_fails_when_list_item_str_not_primitive_type(self):
        message = "'type' list item str must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(type=['string', 'float'])

    def test_fails_when_list_item_str_not_unique(self):
        message = "'type' list item str must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(type=['string', 'null', 'null'])


class TestUniqueItemsValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jschema.JSchema(unique_items=False)

    def test_fails_when_not_bool(self):
        message = "'unique_items' must be a bool"
        with self.assertRaisesSchemaValidationError(message):
            jschema.JSchema(unique_items='True')


if __name__ == '__main__':
    unittest.main()

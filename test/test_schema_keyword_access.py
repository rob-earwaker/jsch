import unittest

import jsch


class KeywordAccessTestCase(unittest.TestCase):
    def assertRaisesAttributeError(self, message):
        regex = '^{0}$'.format(message)
        return self.assertRaisesRegex(AttributeError, regex)


class TestAdditionalItemsKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(additional_items=True)
        self.assertEqual(True, schema.additional_items)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.additional_items)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.additional_items = True


class TestAdditionalPropertiesKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(additional_properties=True)
        self.assertEqual(True, schema.additional_properties)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.additional_properties)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.additional_properties = True


class TestAllOfKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(all_of=[jsch.Schema()])
        self.assertEqual([jsch.Schema()], schema.all_of)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.all_of)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.all_of = [jsch.Schema()]


class TestAnyOfKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(any_of=[jsch.Schema()])
        self.assertEqual([jsch.Schema()], schema.any_of)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.any_of)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.any_of = [jsch.Schema()]


class TestDefaultKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(default=0)
        self.assertEqual(0, schema.default)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.default)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.default = 0


class TestDefinitionsKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(definitions={'name': jsch.Schema()})
        self.assertEqual({'name': jsch.Schema()}, schema.definitions)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.definitions)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.definitions = {'name': jsch.Schema()}


class TestDependenciesKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(dependencies={'name': ['age']})
        self.assertEqual({'name': ['age']}, schema.dependencies)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.dependencies)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.dependencies = {'name': ['age']}


class TestDescriptionKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(description='Represents a schema')
        self.assertEqual('Represents a schema', schema.description)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.description)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.description = 'Represents a schema'


class TestEnumKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(enum=[9, 7, 2])
        self.assertEqual([9, 7, 2], schema.enum)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.enum)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.enum = [9, 7, 2]


class TestExclusiveMaximumKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(maximum=9, exclusive_maximum=True)
        self.assertEqual(True, schema.exclusive_maximum)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.exclusive_maximum)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.exclusive_maximum = True


class TestExclusiveMinimumKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(minimum=1, exclusive_minimum=True)
        self.assertEqual(True, schema.exclusive_minimum)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.exclusive_minimum)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.exclusive_minimum = True


class TestIdKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(id='#def')
        self.assertEqual('#def', schema.id)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.id)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.id = '#def'


class TestItemsKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(items=jsch.Schema())
        self.assertEqual(jsch.Schema(), schema.items)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.items)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.items = jsch.Schema()


class TestMaxItemsKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(max_items=6)
        self.assertEqual(6, schema.max_items)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.max_items)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.max_items = 6


class TestMaxLengthKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(max_length=2)
        self.assertEqual(2, schema.max_length)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.max_length)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.max_length = 2


class TestMaxPropertiesKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(max_properties=6)
        self.assertEqual(6, schema.max_properties)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.max_properties)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.max_properties = 6


class TestMaximumKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(maximum=8.9)
        self.assertEqual(8.9, schema.maximum)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.maximum)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.maximum = 8.9


class TestMinItemsKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(min_items=3)
        self.assertEqual(3, schema.min_items)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.min_items)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.min_items = 3


class TestMinLengthKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(min_length=2)
        self.assertEqual(2, schema.min_length)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.min_length)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.min_length = 2


class TestMinPropertiesKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(min_properties=4)
        self.assertEqual(4, schema.min_properties)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.min_properties)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.min_properties = 4


class TestMinimumKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(minimum=6.2)
        self.assertEqual(6.2, schema.minimum)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.minimum)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.minimum = 6.2


class TestMultipleOfKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(multiple_of=4.7)
        self.assertEqual(4.7, schema.multiple_of)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.multiple_of)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.multiple_of = 4.7


class TestNotKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(not_=jsch.Schema())
        self.assertEqual(jsch.Schema(), schema.not_)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.not_)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.not_ = jsch.Schema()


class TestOneOfKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(one_of=[jsch.Schema()])
        self.assertEqual([jsch.Schema()], schema.one_of)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.one_of)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.one_of = [jsch.Schema()]


class TestPatternKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(pattern='[0-9A-Z]')
        self.assertEqual('[0-9A-Z]', schema.pattern)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.pattern)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.pattern = '[0-9A-Z]'


class TestPatternPropertiesKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(pattern_properties={'[0-9]': jsch.Schema()})
        self.assertEqual({'[0-9]': jsch.Schema()}, schema.pattern_properties)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.pattern_properties)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.pattern_properties = {'[0-9]': jsch.Schema()}


class TestPropertiesKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(properties={'name': jsch.Schema()})
        self.assertEqual({'name': jsch.Schema()}, schema.properties)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.properties)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.properties = {'name': jsch.Schema()}


class TestRefKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(ref='#/definitions/person')
        self.assertEqual('#/definitions/person', schema.ref)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.ref)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.ref = '#/definitions/person'


class TestRequiredKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(required=['name', 'age'])
        self.assertEqual(['name', 'age'], schema.required)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.required)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.required = ['name', 'age']


class TestTitleKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(title='jsch')
        self.assertEqual('jsch', schema.title)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.title)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.title = 'jsch'


class TestTypeKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(type='string')
        self.assertEqual('string', schema.type)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.type)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.type = 'string'


class TestUniqueItemsKeywordAccess(KeywordAccessTestCase):
    def test_read_property(self):
        schema = jsch.Schema(unique_items=True)
        self.assertEqual(True, schema.unique_items)

    def test_read_unassigned_property(self):
        schema = jsch.Schema()
        self.assertIsNone(schema.unique_items)

    def test_set_property(self):
        schema = jsch.Schema()
        message = "can't set keyword attribute"
        with self.assertRaisesAttributeError(message):
            schema.unique_items = True

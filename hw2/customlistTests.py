import unittest
from customlist import CustomList

# assertEqual сравивает по сумме элементов !!!!!!!!!!!!!

class CustomListAddAndRaddTests(unittest.TestCase):
    def setUp(self):
        self.custom_list_1 = CustomList([5, 1, 3, 7])
        self.custom_list_2 = CustomList([1, 2, -4])
        self.custom_list_3 = CustomList([1, 2, -4, 5])
        self.basic_list = [1, 2, -4]

    def test_larger_add_smaller(self):
        result = self.custom_list_1 + self.custom_list_2
        self.assertEqual(result, CustomList([6, 3, -1, 7]))

    def test_smaller_add_larger(self):
        result = self.custom_list_2 + self.custom_list_1
        self.assertEqual(result, CustomList([6, 3, -1, 7]))

    def test_equal_size_adding(self):
        result = self.custom_list_1 + self.custom_list_3
        self.assertEqual(result, CustomList([6, 3, -1, 12]))

    def test_basic_list_adding_right(self):
        result = self.custom_list_1 + self.basic_list
        self.assertEqual(result, CustomList([6, 3, -1, 7]))
        self.assertIsInstance(result, CustomList)

    def test_basic_list_adding_left(self):
        result = self.basic_list + self.custom_list_1
        self.assertEqual(result, CustomList([6, 3, -1, 7]))
        self.assertIsInstance(result, CustomList)

    def test_non_support_type(self):
        obj_diff_types_list = [1, '', {}, (), float(1)]
        for obj in obj_diff_types_list:
            with self.assertRaises(TypeError):
                self.custom_list_1 + obj
                obj + self.custom_list_1


class CustomListSubAndRsubTests(unittest.TestCase):
    def setUp(self):
        self.custom_list_1 = CustomList([5, 1, 3, 7])
        self.custom_list_2 = CustomList([1, 2, -4])
        self.custom_list_3 = CustomList([1, 2, -4, 5])
        self.basic_list = [1, 2, -4]

    def test_larger_sub_smaller(self):
        result = self.custom_list_1 - self.custom_list_2
        self.assertEqual(result, CustomList([4, -1, 7, 7]))

    def test_smaller_sub_larger(self):
        result = self.custom_list_2 - self.custom_list_1
        self.assertEqual(result, CustomList([-4, 1, -7, -7]))

    def test_equal_size_subbing(self):
        result = self.custom_list_1 - self.custom_list_3
        self.assertEqual(result, CustomList([4, -1, 7, 2]))

    def test_basic_list_subbing_right(self):
        result = self.custom_list_1 - self.basic_list
        self.assertEqual(result, CustomList([4, -1, 7, 7]))
        self.assertIsInstance(result, CustomList)

    def test_basic_list_subbing_left(self):
        result = self.basic_list - self.custom_list_1
        self.assertEqual(result, CustomList([-4, 1, -7, -7]))
        self.assertIsInstance(result, CustomList)

    def test_non_support_type(self):
        obj_diff_types_list = [1, '', {}, (), float(1)]
        for obj in obj_diff_types_list:
            with self.assertRaises(TypeError):
                self.custom_list_1 - obj
                obj - self.custom_list_1


class CustomListComparisonTests(unittest.TestCase):
    def setUp(self):
        self.custom_list_1 = CustomList([5, 0, 0, 0])
        self.custom_list_2 = CustomList([1, 2, 5])
        self.custom_list_3 = CustomList([1, 2, 1, 1])

        self.basic_list_1 = [6, 2, -4]
        self.basic_list_2 = [4, 1, 1]
        self.basic_list_3 = [-2, 7]

    def test_smaller(self):
        self.assertTrue(self.custom_list_1 < self.custom_list_2)
        self.assertFalse(self.custom_list_1 < self.custom_list_3)
        self.assertFalse(self.custom_list_3 < self.custom_list_1)

        self.assertTrue(self.custom_list_1 < self.basic_list_2)
        self.assertTrue(self.basic_list_1 < self.custom_list_1)
        self.assertTrue(self.basic_list_2 < self.custom_list_2)


    def test_smaller_or_equal(self):
        self.assertTrue(self.custom_list_1 <= self.custom_list_2)
        self.assertTrue(self.custom_list_1 <= self.custom_list_3)
        self.assertTrue(self.custom_list_3 <= self.custom_list_1)

        self.assertTrue(self.custom_list_1 <= self.basic_list_2)
        self.assertTrue(self.basic_list_3 <= self.custom_list_1)

    def test_equal(self):
        self.assertTrue(self.custom_list_1 == self.custom_list_3)
        self.assertFalse(self.custom_list_1 == self.custom_list_2)

        self.assertTrue(self.custom_list_1 == self.basic_list_3)
        self.assertFalse(self.custom_list_1 == self.basic_list_1)

    def test_not_equal(self):
        self.assertTrue(self.custom_list_1 != self.custom_list_2)
        self.assertFalse(self.custom_list_1 != self.custom_list_3)

        self.assertFalse(self.custom_list_1 != self.basic_list_3)
        self.assertTrue(self.custom_list_1 != self.basic_list_1)

    def test_larger(self):
        self.assertTrue(self.custom_list_2 > self.custom_list_1)
        self.assertFalse(self.custom_list_1 > self.custom_list_3)
        self.assertFalse(self.custom_list_3 > self.custom_list_1)

        self.assertFalse(self.custom_list_1 > self.basic_list_2)
        self.assertFalse(self.basic_list_1 > self.custom_list_1)
        self.assertTrue(self.custom_list_2 > self.basic_list_2)

    def test_larger_or_equal(self):
        self.assertFalse(self.custom_list_1 >= self.custom_list_2)
        self.assertTrue(self.custom_list_2 >= self.custom_list_1)
        self.assertTrue(self.custom_list_1 >= self.custom_list_3)

        self.assertTrue(self.basic_list_3 >= self.custom_list_1)
        self.assertTrue(self.basic_list_2 >= self.custom_list_1)
import unittest
from custommeta import CustomMeta


class SomeClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


class TestCustomMeta(unittest.TestCase):
    def setUp(self):
        self.some_class_obj = SomeClass()

    def test_class_fields_renamed(self):
        self.assertEqual(self.some_class_obj.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.some_class_obj.x

    def test_class_functions_renamed(self):
        self.assertEqual(self.some_class_obj.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.some_class_obj.line()

    def test_obj_fields_renamed(self):
        self.assertEqual(self.some_class_obj.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.some_class_obj.val

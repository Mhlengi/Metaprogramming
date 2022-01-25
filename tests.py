import unittest
from unittest import TestCase

from records import Person, Dog


class RecordTests(TestCase):
    def test_creation(self):
        Person(name="JAMES", age=110, income=24000.0)

        with self.assertRaises(TypeError):
            Person(name="JAMES", age=160, income=24000.0)

        with self.assertRaises(TypeError):
            Person(name="JAMES")

        with self.assertRaises(TypeError):
            Person(name="JAMES", age=-1, income=24000.0)

        with self.assertRaises(TypeError):
            Person(name="JAMES", age="150", income=24000.0)

        with self.assertRaises(TypeError):
            Person(name="JAMES", age="150", wealth=24000.0)

    def test_properties(self):
        james = Person(name="JAMES", age=34, income=24000.0)

        self.assertEqual(james.age.value, 34)
        self.assertEqual(james.income.value, 24000.0)

        with self.assertRaises(AttributeError):
            james.age.value = 32

    def test_str(self):
        james = Person(name="JAMES", age=34, income=24000.0)

        self.assertTrue("name='JAMES'" in str(james))
        self.assertTrue("# The person's age" in str(james))
        self.assertTrue("income=24000.0" in str(james))

    def test_dog(self):
        mike = Dog(name="mike", habitat="land", weight=50., bark="ARF")
        self.assertEqual(mike.weight.value, 50)

        with self.assertRaises(TypeError):
            Dog(name="mike", habitat="", weight=50., bark="ARF")

        with self.assertRaises(AttributeError):
            mike.habitat.value = ""


if __name__ == '__main__':
    unittest.main()

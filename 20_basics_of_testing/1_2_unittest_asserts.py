import unittest
from typing import Iterable


class TestAsserts(unittest.TestCase):

    def test_true_false_equality(self):
        true = True
        none = None
        self.assertTrue(true)
        self.assertFalse(not true)
        self.assertIs(true, True)
        self.assertIsNot(true, False)
        self.assertIsNone(none)
        self.assertIsNotNone(not none)
        self.assertIsInstance([], Iterable)
        self.assertNotIsInstance(0, str)

        self.assertAlmostEqual(4, 5, delta=1)
        self.assertNotAlmostEqual(4, 20, delta=1)

    def test_compare(self):
        self.assertGreater(7, 4)
        self.assertGreaterEqual(7, 7)
        self.assertLess(5, 6)
        self.assertLessEqual(5, 7)

    def test_sequence(self):
        self.assertListEqual([1, 2], [1, 2])
        self.assertTupleEqual((1, 2), (1, 2))
        self.assertSetEqual({2, 3}, {3, 2})
        self.assertDictEqual({'key1': 1, 'key2': 2}, {'key2': 2, 'key1': 1})
        self.assertSequenceEqual([1, 2, 3], (1, 2, 3))
        self.assertCountEqual([1, 2, 3], (3, 2, 1))

    def test_presence(self):
        self.assertIn(3, [1, 2, 3])
        self.assertNotIn(999, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()

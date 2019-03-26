import unittest

from helpers.hash_map import HashMap


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.small_map = HashMap(size=2)

    def test_hash_map(self):
        self.small_map.put('Orange', 1.5)
        self.small_map.put('Apple', 2)
        self.small_map.put('Apple', 4)
        self.small_map.put('Apple', 6)
        self.small_map.put('Grape', -10)
        self.small_map.put(5, 6)
        self.assertEqual(1.5, self.small_map.get('Orange'))
        self.assertEqual(6, self.small_map.get('Apple'))
        self.assertEqual(-10, self.small_map.get('Grape'))
        self.assertEqual(6, self.small_map.get(5))
        self.assertIsNone(self.small_map.get('Banana'))


if __name__ == '__main__':
    unittest.main()

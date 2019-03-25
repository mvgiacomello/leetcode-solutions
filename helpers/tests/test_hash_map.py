import unittest

from helpers.hash_map import HashMap


class _TestHashMap(unittest.TestCase):
    def test_hash_map(self):
        map = HashMap(10)
        map.put('Orange', 1.5)
        map.put('Apple', 2)
        map.put('Apple', 4)
        map.put('Grape', -10)
        self.assertEqual(1.5, map.get('Orange'))
        self.assertEqual(4, map.get('Apple'))
        self.assertEqual(-10, map.get('Grape'))
        self.assertIsNone(map.get('Banana'))


if __name__ == '__main__':
    unittest.main()

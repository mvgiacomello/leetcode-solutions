import unittest

from helpers.hash_map import HashMap


class TestHashMap(unittest.TestCase):
    def test_put_on_small_map(self):
        self.assertRaises(ValueError, HashMap, -1)
        self.assertRaises(ValueError, HashMap, 0)
        self.assertRaises(ValueError, HashMap, 1)

    def test_put_same_key(self):
        map = HashMap()
        map.put('Apple', 'Are good good for you')
        map.put('Apple', 'Are bad for you')
        map.put('Apple', 0)
        self.assertEqual(0, map.get('Apple'))

    def test_put_integer(self):
        map = HashMap()
        map.put(-1, -1)
        map.put(0, 0)
        map.put(1, 1)
        self.assertEqual(-1, map.get(-1))
        self.assertEqual(0, map.get(0))
        self.assertEqual(1, map.get(1))

    def test_put_string(self):
        map = HashMap()
        map.put('Apple', 'Apple')
        map.put('Orange', 'Orange')
        map.put('Grape', 'Grape')
        self.assertEqual('Apple', map.get('Apple'))
        self.assertEqual('Orange', map.get('Orange'))
        self.assertEqual('Grape', map.get('Grape'))

    def test_put_other_objects(self):
        # Dummy class
        class Test:
            self.value = 0
        test_object = Test()

        map = HashMap()
        map.put(test_object, 'Apple')
        self.assertEqual('Apple', map.get(test_object))

    def test_put_and_get_different_types(self):
        map = HashMap(2)
        map.put('Apple', 'Apple')
        map.put('Orange', 'Orange')
        map.put('Grape', 'Grape')
        map.put(1, 1)
        map.put(2, 2)
        map.put(3, 3)
        self.assertEqual('Apple', map.get('Apple'))
        self.assertEqual('Orange', map.get('Orange'))
        self.assertEqual('Grape', map.get('Grape'))
        self.assertEqual(1, map.get(1))
        self.assertEqual(2, map.get(2))
        self.assertEqual(3, map.get(3))

    def test_get_on_empty_map(self):
        map = HashMap()
        self.assertIsNone(map.get('Apple'))

    def test_large_with_lots_of_entries(self):
        map = HashMap(2)
        map.put('Apple', 'Apple')
        for index in range(0, 2000):
            map.put('Apple' + str(index), 'Apple')
        self.assertEqual('Apple', map.get('Apple'))


if __name__ == '__main__':
    unittest.main()

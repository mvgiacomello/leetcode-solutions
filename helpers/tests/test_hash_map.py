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

    def test_hash_function(self):
        hashed_things_with_seed_eleven = [[1276629, 'Apple'], [13980558, 'Banana'], [34879626494972, 'dragon fruit'],
                                          [60, 1], [61, 2], [62, 3],
                                          [141627, True], [1329462, False], [133201, None]]
        map = HashMap()
        map.seed = 11
        for entry in hashed_things_with_seed_eleven:
            self.assertEqual(entry[0], map._hash(entry[1]),
                             'Expected hash \'{expected}\' for key \'{key}\''.format(expected=entry[0], key=entry[1]))

    def test_expected_positions(self):
        size = 10
        map = HashMap(size)
        self.assertEqual(0, map._position(0))
        self.assertEqual(1, map._position(1))
        self.assertEqual(2, map._position(2))
        self.assertEqual(3, map._position(3))
        self.assertEqual(4, map._position(4))
        self.assertEqual(5, map._position(5))
        self.assertEqual(6, map._position(6))
        self.assertEqual(7, map._position(7))
        self.assertEqual(8, map._position(8))
        self.assertEqual(9, map._position(9))
        self.assertEqual(0, map._position(10))
        self.assertEqual(1, map._position(11))
        self.assertEqual(2, map._position(12))
        self.assertEqual(3, map._position(13))

    def test_unexpected_positions(self):
        size = 10
        map = HashMap(size)
        self.assertEqual(9, map._position(-1))
        self.assertEqual(8, map._position(-2))
        self.assertRaises(ValueError, map._position, None)
        self.assertRaises(ValueError, map._position, 'test')
        self.assertRaises(ValueError, map._position, '')


if __name__ == '__main__':
    unittest.main()

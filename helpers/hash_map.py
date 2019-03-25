import unittest
from typing import Any

from helpers.linked_list import LinkedList


class HashMap:
    def __init__(self, initial_size=100):
        self.entries = [LinkedList()] * initial_size

    def put(self, key, value):
        pass
        # TODO: implement me

    def get(self, key) -> object:
        pass
        # TODO: implement me

    def _hash(self, object):
        pass
        # TODO: implement me

    def _position(self, object):
        pass
        # TODO: implement me


class HashNode:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key


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

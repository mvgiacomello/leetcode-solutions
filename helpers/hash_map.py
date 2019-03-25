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

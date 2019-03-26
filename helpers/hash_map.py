from typing import Any, List

from helpers.linked_list import LinkedList, LinkedListNode


class HashMap:
    def __init__(self, size=100):
        if size <= 1:
            raise ValueError('size should be higher than 1')
        # Initialize the list with None values
        self.entries: List = [None] * size
        self.size: int = size
        self.seed = 11

    def put(self, key: Any, value: Any):
        """
        Store the pair in the hash map
        :param key: key of of the the pair to store
        :param value: value to store
        """
        position: int = self._position(self._hash(key))
        if self.entries[position] is None:
            # Key does not exist, create a list and add it
            self.entries[position] = LinkedList()
            self.entries[position].add(HashNode(key=key, value=value))
        else:
            # Check whether the position is already taken
            current = self.entries[position].head
            while current is not None and current.value.key != key:
                current = current.next
            # Update value if the key already exist or just add to the existing list
            if current is None:
                self.entries[position].add(HashNode(key=key, value=value))
            else:
                current.value.value = value

    def get(self, key: Any) -> Any:
        """
        Retrieve the value of a certain key
        :param key: the key to retrieve its value
        :return: the value of the key or None if key does not exist
        """
        position = self._position(self._hash(key))
        if self.entries[position] is None:
            return None
        else:
            current: LinkedListNode = self.entries[position].head
            while current is not None and current.value.key != key:
                current = current.next
            return None if current is None else current.value.value

    def _hash(self, key: Any) -> int:
        """
        :param key: the value to get the hash from. Must be able to cast to string
        :return: hash (integer) representative of the key
        """
        sum = 1
        string = str(key)
        for char in string:
            sum = sum * self.seed + ord(char)
        return sum

    def _position(self, hash: int) -> int:
        """
        :param hash: the hashed value of the key
        :return: the position in the list where value should be stored
        """
        position = hash % self.size
        return position


class HashNode:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value

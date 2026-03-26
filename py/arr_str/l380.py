import random


class RandomizedSet:

    def __init__(self):
        self._sets = set()

    def insert(self, val: int) -> bool:
        if val not in self._sets:
            self._sets.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self._sets:
            self._sets.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        if self._sets is None:
            return None
        index = random.randint(0, len(self._sets)-1)
        return list(self._sets)[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

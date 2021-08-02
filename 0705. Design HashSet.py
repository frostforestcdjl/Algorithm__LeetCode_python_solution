#Runtime: 136 ms, faster than 98.54% of Python3 online submissions for Design HashSet.
#Memory Usage: 19.2 MB, less than 45.80% of Python3 online submissions for Design HashSet.

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cont =set()

    def add(self, key: int) -> None:
        self.cont.add(key)

    def remove(self, key: int) -> None:
        self.cont.add(key)
        self.cont.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.cont
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

#Runtime: 188 ms, faster than 98.94% of Python3 online submissions for Design HashMap.
#Memory Usage: 17.1 MB, less than 89.83% of Python3 online submissions for Design HashMap.

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map_dic = {}
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.map_dic[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.map_dic:
            return self.map_dic[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.map_dic[key] = 0
        self.map_dic.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

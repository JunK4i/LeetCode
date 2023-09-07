class RandomizedSet:

    def __init__(self):
        self.set_data = set()

    def insert(self, val: int) -> bool:
        if val in self.set_data:
            return False
        else:
            self.set_data.add(val)
            return True 

    def remove(self, val: int) -> bool:
        if val in self.set_data:
            self.set_data.discard(val)
            return True
        else:
                return False

    def getRandom(self) -> int:
        return random.sample(self.set_data,1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
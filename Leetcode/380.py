from collections import defaultdict
import random

class RandomizedSet:
    def __init__(self):
        self.map = defaultdict(int) 

    def insert(self, val: int) -> bool:
        if not self.map[val]:
            self.map[val] += 1
            return True

        else:
            return False

    def remove(self, val: int) -> bool:
        if self.map[val]:
            self.map[val] -= 1
            del self.map[val]
            return True

        else:
            del self.map[val]
            return False
        
    def getRandom(self) -> int:
        return random.choice(list(self.map.keys()))
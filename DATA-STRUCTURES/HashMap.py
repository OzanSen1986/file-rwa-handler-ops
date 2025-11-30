
class HashMap:
    def __init__(self, size) -> None:
        self.hashmap = [None for i in range(size)]
    
    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def get(self, key) -> None:
        i = self.key_to_index(key)
        tup = self.hashmap[i]
        if tup is None:
            raise Exception('Sorry, key was not found')
        return tup[1]


    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)
    
    def __repr(self) -> None:
        buckets = []


class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_val = {}  # key: (value, frequency)
        self.frequency_to_keys = defaultdict(OrderedDict)  # {frequency: {key: value}}
        self.capacity = capacity
        self.size = 0
        self.min = None

    def delete_key(self, key: int):
        # deletion: when key exists
        if key not in self.key_to_val:
            raise Exception(f"{key} does not exist.")
        _, frequency = self.key_to_val.pop(key)

        del self.frequency_to_keys[frequency][key]
        if not self.frequency_to_keys[frequency]:
            del self.frequency_to_keys[frequency]

        self.size -= 1

    def add_key_value(self, key: int, value: int, frequency: int):
        # insertion: when key does not exist.
        if key in self.key_to_val:
            raise Exception(f"Key={key} already exists")

        self.key_to_val[key] = value, frequency
        self.frequency_to_keys[frequency][key] = value

        self.size += 1

    def evict(self):
        # Evict the least frequently used key
        key, _ = self.frequency_to_keys[self.min].popitem(last=False)
        del self.key_to_val[key]
        if not self.frequency_to_keys[self.min]:
            del self.frequency_to_keys[self.min]
        self.size -= 1

    def get(self, key: int) -> int:
        if self.capacity == 0 or key not in self.key_to_val:
            return -1

        value, frequency = self.key_to_val[key]
        self.delete_key(key)
        self.add_key_value(key, value, frequency + 1)
        if frequency == self.min and not self.frequency_to_keys.get(frequency):
            self.min += 1
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            # Modify an existing key
            _, frequency = self.key_to_val[key]
            self.delete_key(key)
            self.add_key_value(key, value, frequency + 1)
            if frequency == self.min and not self.frequency_to_keys.get(frequency):
                self.min += 1
        else:
            # Add a new key
            if self.size == self.capacity:
                self.evict()
            self.add_key_value(key, value, 1)
            self.min = 1  

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

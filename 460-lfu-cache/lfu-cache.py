class OrderedSet:
    def __init__(self, iterable=None):
        self.dict = OrderedDict()
        if iterable:
            self.add_all(iterable)

    def add_all(self, iterable):
        for item in iterable:
            self.add(item)

    def add(self, item):
        self.dict[item] = None

    def remove(self, item):
        self.dict.pop(item, None)

    def peek(self):
        if not self.dict:
            raise KeyError("OrderedSet is empty!")
        return next(iter(self.dict))

    def pop(self):
        if not self.dict:
            raise KeyError("OrderedSet is empty!")
        return self.dict.popitem(last=False)[0]

    def contains(self, item):
        return item in self.dict

    def __iter__(self):
        return iter(self.dict)

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self.dict.keys())})"

    def __bool__(self):
        return bool(self.dict)

    def __len__(self):
        return len(self.dict)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min = None
        self.key_to_value = {}  # {key: (value, frequency)}
        # {frequency: {keys}} and keys are in an OrderedSet
        self.frequency_to_keys = defaultdict(OrderedSet)

    def pop_from_frequency(self, frequency, item=None) -> Optional[int]:
        if not item:
            key = self.frequency_to_keys[frequency].pop()
        else:
            key = self.frequency_to_keys[frequency].remove(item)
        if not self.frequency_to_keys[frequency]:
            del self.frequency_to_keys[frequency]
        return key

    def update_frequency(self, frequency, key):
        self.pop_from_frequency(frequency, key)
        if frequency not in self.frequency_to_keys:
            if self.min and frequency == self.min:
                self.min += 1
        self.frequency_to_keys[frequency + 1].add(key)

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1

        # update key_to_value
        value, frequency = self.key_to_value[key]
        self.key_to_value[key] = (value, frequency + 1)

        # update frequency_to_keys and self.min
        self.update_frequency(frequency, key)
        # self.pop_from_frequency(frequency, key)
        # if frequency not in self.frequency_to_keys:
        #     if self.min and frequency == self.min:
        #         self.min += 1
        # self.frequency_to_keys[frequency + 1].add(key)
        return value

    def evict(self):
        # is only used before insertion
        frequency = self.min
        key = self.pop_from_frequency(frequency)
        del self.key_to_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # update
        if key in self.key_to_value:
            # update key_to_value
            _, frequency = self.key_to_value[key]
            self.key_to_value[key] = (value, frequency + 1)

            # update frequency_to_keys and self.min
            self.update_frequency(frequency, key)
            # self.pop_from_frequency(frequency, key)
            # if frequency not in self.frequency_to_keys:
            #     if self.min and frequency == self.min:
            #         self.min += 1
            # self.frequency_to_keys[frequency + 1].add(key)

        # insertion
        else:
            if self.capacity == len(self.key_to_value):
                self.evict()
            # add to key_to_value
            self.key_to_value[key] = (value, 1)

            # add to frequency_to_keys and self.min
            self.frequency_to_keys[1].add(key)
            self.min = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

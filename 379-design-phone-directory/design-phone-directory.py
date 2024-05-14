class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slots = deque(range(maxNumbers))
        self.is_slot_available = [True] * maxNumbers

    def get(self) -> int:
        if not self.slots:
            return -1

        slot = self.slots.popleft()
        self.is_slot_available[slot] = False
        return slot

    def check(self, number: int) -> bool:
        return self.is_slot_available[number]

    def release(self, number: int) -> None:
        if self.is_slot_available[number]:
            return
        self.slots.append(number)
        self.is_slot_available[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

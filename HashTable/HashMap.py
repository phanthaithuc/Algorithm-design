class HashMap:
    def __init__(self):
        self.key = []
        self.value = []

    def add(self, key: int, value: int) -> None:
        if key in self.key:
            self.value[self.key.index(key)] = value
        else:
            self.key.append(key)
            self.value.append(value)

    def get(self, key: int):
        if key in self.key:
            return self.value[self.key.index(key)]
        else:
            return -1

    def remove(self, key: int, value: int) -> None:
        if key in self.key:
            self.value.pop(self.key.index(key))
            self.key.remove(key)

    def print(self):
        for i in range(len(self.key)):
            print(" key = ", i, "value =", self.key[i])

if __name__ == "__main__":
    new_hash = HashMap()
    new_hash.add(1, 3)
    new_hash.add(1, 2)
    new_hash.print()


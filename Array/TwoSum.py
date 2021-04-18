class TwoSum():
    def __init__(self):
        self.nums = []

    def add(self, value: int):
        self.nums.append(value)

    def find(self, k) -> []:
        d = {}
        res = []
        for i in range(len(self.nums)):
            complement = k - self.nums[i]
            d[self.nums[i]] = i
            if complement in d:
                res.append([self.nums[i], self.nums[d.get(complement)]])

        print("List d = ", d)
        print("Result = ", res)

        if not res:
            print("False")
        else:
            print("True")

    def print(self):
        if not self.nums:
            print("No value")
        else:
            print("Nums = ", self.nums)


class TwoSum1:
    def __init__(self):
        self.nums = []

    def add(self, number):
        self.nums.append(number)

    def find(self, k) -> []:
        d = {}
        res = []
        if not self.nums:
            for i in len(range(self.nums)):
                complement = k - self.nums(i)
                d[nums[i]] = i
                if complement in d:
                    res.append([self.nums[i], self.nums[d.get(complement)]])
            if not res:
                print("False")
            else:
                print("True")

        else:
            print("Empty array")
        return res


if __name__ == '__main__':
    test = TwoSum()
    test.add(0)
    test.add(0)
    test.find(0)


def canSum(targetSum, numbers: []):
    table = [False] * (targetSum + 1)
    table[0] = True
    print(table)
    for i in range(len(numbers)):
        if table[i] is True:
            for num in numbers:
                if i + num < len(table):
                    table[i + num] = True
    print(table)
    return table[targetSum]


numbers = [3,5,7]
print(canSum(7, [2,3,6,7]))


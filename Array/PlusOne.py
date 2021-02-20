
def plusOne(arr: []):
    if not arr:
        return
    if len(arr) == 1 and arr[0] == 9:
        arr = [1,0]
        return arr
    elif len(arr) == 1 and arr[0] < 9:
        arr[0] = arr[0] + 1
        return arr
    i = len(arr) - 2
    arr[-1] = arr[-1] + 1
    if arr[-1] >= 10:
        arr[-1] = 0
        carry = 1
    else:
        carry = 0
    while i >= 0:
        plus = arr[i] + carry
        if plus >= 10:
            arr[i] = 0
            carry = 1
        else:
            carry = 0
            arr[i] = plus
        i -= 1
    if carry == 1:
        arr.insert(0, 1)

    return arr





if __name__ == "__main__":
    arr = [2,9,9]
    # print(plusOne(arr))
    # print(plusOne([0,9,9]))
    # print(plusOne([2,3,5]))
    # print(plusOne([9]))
    # print(plusOne([1,9]))
    # print(plusOne([0,8]))
    # print(plusOne([0]))
    print(plusOne([9,9]))
    print(plusOne([1,9,9,9]))
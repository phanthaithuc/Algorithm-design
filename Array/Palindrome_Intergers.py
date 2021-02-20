def is_palindrome(nums):
    if not nums or nums < 0:
        return False

    res = []
    while nums:
        digit = abs(nums) % 10
        res.append(digit)
        nums //= 10

    if len(res) <= 2:
        return False

    mid = len(res) // 2
    i = 0
    j = len(res) - 1
    while i < mid:
        if res[i] == res[j]:
            flag = True
        else:
            return False

        i += 1
        j -= 1

    return flag


print(is_palindrome(-121))
print(-123 % 10)

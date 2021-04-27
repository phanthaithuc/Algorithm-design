string = "aba"


def helper(string: str, left: int, right: int) -> bool:
    if not string:
        return False
    l = left
    r = right
    while l < right:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


def valid_palindrome(string: str) -> bool:
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            if helper(string, left + 1, right) is True:
                return True
            elif helper(string, left, right - 1) is True:
                return True

            return False
    return True


print(valid_palindrome(string))

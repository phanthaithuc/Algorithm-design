s = "A man, a plan, a canal: Panama"


def palindrome(s: str) -> bool:
    s = s.lower()
    s_stripped = ''.join(list(filter(lambda x: x.isalnum() == True, s)))
    low = 0
    high = len(s_stripped) - 1
    while low <= high:
        if s_stripped[low] == s_stripped[high]:
            low += 1
            high -= 1
            continue
        else:
            return False

    return True


print(palindrome(s))

print(s)

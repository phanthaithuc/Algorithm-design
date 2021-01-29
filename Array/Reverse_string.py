str = ["h","e","l","l","o"]

def reverse_string(str):
    left = 0
    right = len(str)-1
    while left < right:
        str[left], str[right] = str[right], str[left]
        left+=1
        right -=1
    return str

print("new reverse string: ", reverse_string(str))
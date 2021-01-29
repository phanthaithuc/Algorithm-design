nums = [3,5,12,5,13]

def findPythagon(nums:[]):
    h = {}
    for i in nums:
        h[i] = i*i
    return h

print(findPythagon(nums))


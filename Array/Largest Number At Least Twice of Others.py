def twice(nums):
    m = max(nums)
    if all(m>=2*x for x in nums if x!=m):
        return nums.index(m)
    else:
        return -1
if __name__ == "__main__":
    nums = [0,0,2,3]
    print(twice(nums))

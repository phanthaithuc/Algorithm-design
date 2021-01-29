def swap(nums: [], k):
    i = 0
    while i < k:
        helper(nums)
        i += 1

    return nums


def helper(nums: []):
    j = len(nums) - 1
    temp = nums[-1]
    while j > 0:
        nums[j] = nums[j - 1]
        j -= 1
    nums[0] = temp


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    swap(nums, 3)
    print(nums)

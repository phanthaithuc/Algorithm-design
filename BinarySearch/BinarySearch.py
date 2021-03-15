nums = [-1, 0, 3, 5, 9, 12]
nums_1 = []


def binarySearch(nums: [], k: int) -> (int, str):
    if not nums:
        print("Not Found")
        return

    mid = len(nums) // 2
    left = 0
    right = len(nums) - 1

    if nums[mid] == k:
        print(k, "appear in the array at index: ", mid)
    if nums[mid] > k:
        binarySearch(nums[0:mid - 1], k)
    elif nums[mid] < k:
        binarySearch(nums[mid:], k)


binarySearch(nums, 9)

binarySearch(nums_1, -2)

print(binarySearch.__annotations__['return'])

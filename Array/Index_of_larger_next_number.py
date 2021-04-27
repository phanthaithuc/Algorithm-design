def larger_number(nums: []) -> []:
    if not nums:
        return
    res = []
    for i in range(len(nums) - 1):
        if nums[i + 1] <= nums[i]:
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    res.append(j)
                    break
                res.append(-1)

        elif nums[i + 1] > nums[i]:
            res.append(i + 1)

    return res

    # while i < len(nums) - 1:
    #     j = i + 1
    #     if nums[j] <= nums[i]:
    #         while j < len(nums) - 1:
    #             if j < len(nums) - 1:
    #                 j += 1
    #             if nums[j] > nums[i]:
    #                 res.append(j)
    #                 i += 1
    #                 break
    #             else:
    #                 res.append(-1)
    #                 i += 1
    #
    #     elif nums[j] > nums[i]:
    #         res.append(j)
    #         i += 1
    #



print(larger_number([3, 2, 5, 6, 9, 8]))

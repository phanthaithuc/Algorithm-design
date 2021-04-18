from collections import defaultdict
def intersection(nums1: [], nums2: []) -> []:
    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1
    hash_map = defaultdict(int)
    res = []
    for i in range(len(nums1)):
        if nums1[i] in hash_map:
            hash_map[nums1[i]] += 1
        else:
            hash_map[nums1[i]] = 1

    for j in range(len(nums2)):
        if nums2[j] in hash_map and nums2[j] > 0:
            res.append(nums2[j])
            #hash_map[nums2[j]] -= 1
    return hash_map

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersection(nums1, nums2))
nums1= [1,1,1,0,1,1,1,0,1,1,1,1]
nums = [1,0,1,0,1,1,1,1,0]


def slide_windows_solution(nums:[]) -> int:
    start = res = zeros = 0
    for end in range(len(nums)):
        if nums[end] == 0:
            zeros+=1
        while zeros > 1:
            if nums[start]==0:
                zeros-=1
            start+=1
        res = max(res, end-start+1)
    return res

def zero_index_solution(nums:[]) ->int:
    zero_index = -1
    current_count = 0
    max_count = 0

    for index, num in enumerate(nums):
        if num == 0:
            max_count = max(max_count, current_count)
            current_count = index - zero_index - 1
            zero_index = index
        current_count += 1

    return max(max_count, current_count)



print(zero_index_solution(nums1))
print(slide_windows_solution(nums1))

def findklargest(nums: [], k: int):
    order = {}
    count = 0
    for i in nums:
        order[i] = count
        count+=1

    print(order)

def findKlargest(nums: [], k: int):
    max = 0
    k-max = float('inf')
    for i in nums:
        if i > max:
            max = i




list = [3, 5, 2, 4, 6, 8]
findklargest(list, 3)
nums = [3, 3, 2, 1, 3, 2, 1]

start = 0
one = two = three = 0
three_index = 0

for i in range(len(nums)):
    if nums[i] == 1:
        one+=1
    elif nums[i]==2:
        two+=1
    else: three+=1

end = one+ two
print(range(one, len(nums)-1 - three))


while one > 0:
    nums[start]= 1
    start+=1
    one-=1

while two > 0 :
    nums[start+two] = 2
    two-=1

while three > 0:
    nums[end] = 3
    three-=1
    end+=1




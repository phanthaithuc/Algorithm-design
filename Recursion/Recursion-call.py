import time
import numpy as np


def sum1(array: []):
    if len(array) == 0:
        return 0
    rest = array[1:]
    return array[0] + sum1(rest)



def sum2(array : []):
    return sum3(array, 0)

def sum3(array, index):
    if index == len(array):
        return 0

    return array[index] + sum3(array, index+1)

nums = np.random.randint(999999999, size = 950)
print(nums)

start_1 = time.time()
resutl_1 = sum1(nums)
print("Result_1 = ", resutl_1, "Time1 = ", time.time() - start_1)

start_2 = time.time()
result_2 = sum2(nums)
print("Result_2 = ", result_2, "Time2 = ", time.time() - start_2)


start_3 = time.time()
result_3 = sum(nums)
print("Result_3 = ", result_3, "Time3 = ", time.time() - start_3)



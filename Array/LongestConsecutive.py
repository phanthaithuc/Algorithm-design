array = [100, 4, 200, 1, 3, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 500, 700, 1000]

array1 = array
print(sorted(array1))


def longestconsucutive(array: []):
    if array is None:
        return
    if len(array) == 1:
        return 1
    array.sort()
    current_count = 1
    max_count = 0
    for i in range(len(array) - 1):
        if array[i + 1] == array[i] + 1:
            current_count += 1
        elif array[i + 1] != array[i] + 1:
            current_count = 1
        if current_count >= max_count:
            max_count = current_count

    return max_count


print(longestconsucutive(array))

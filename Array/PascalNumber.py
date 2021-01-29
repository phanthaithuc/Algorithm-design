numRows = 5
triangle = [1]
prevRows = []
i = 1

while i < numRows:
    prevRows = triangle[i-1]
    newRow = [1]
    j = 1
    while j < len(prevRows):
        newRow.append([prevRows[i - 1] + prevRows[i]])
        j += 1
    newRow.append(1)
    triangle.append(newRow)

    i += 1

print(triangle)
f = open("2020\Day3\Day3Input.txt", "r")
data = f.readlines()
f.close()

slope = [line.strip('\n') for line in data]

indexInRow = 0
indexInRow2 = 0
indexInRow3 = 0
indexInRow4 = 0
indexInRow5 = 0
countTrees = 0
countTrees2 = 0
countTrees3 = 0
countTrees4 = 0
countTrees5 = 0
count = 0

for currentRow in slope:
    if currentRow[indexInRow] == '#':
        countTrees += 1
    if currentRow[indexInRow2] == '#':
        countTrees2 += 1
    if currentRow[indexInRow3] == '#':
        countTrees3 += 1
    if currentRow[indexInRow4] == '#':
        countTrees4 += 1
    indexInRow += 3
    indexInRow2 += 1
    indexInRow3 += 5
    indexInRow4 += 7
    if indexInRow > len(currentRow) - 1:
        indexInRow -= len(currentRow)
    if indexInRow2 > len(currentRow) - 1:
        indexInRow2 -= len(currentRow)
    if indexInRow3 > len(currentRow) - 1:
        indexInRow3 -= len(currentRow)
    if indexInRow4 > len(currentRow) - 1:
        indexInRow4 -= len(currentRow)
    if count % 2 == 0:
        if currentRow[indexInRow5] == '#':
            countTrees5 += 1
        indexInRow5 += 1
        if indexInRow5 > len(currentRow) - 1:
            indexInRow5 -= len(currentRow)
    count += 1

print(countTrees)
totalCountTrees = countTrees * countTrees2 * countTrees3 * countTrees4 * countTrees5
print(totalCountTrees)
# 3178236360 is too low
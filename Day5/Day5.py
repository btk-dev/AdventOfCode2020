f = open("2020\Day5\Day5Input.txt", "r")
data = f.readlines()
f.close()

seats = [line.strip('\n') for line in data]

rows = 128
seatID = 0
seatIDs = []
highestSeatID = 0

for seat in seats:
    lowestRow = 0
    highestRow = 128
    lowestCol = 0
    highestCol = 8
    currentSeat = 0
    if seat[0] == 'B':
        lowestRow = (highestRow - lowestRow) / 2
        lowestRow = round(lowestRow)
    if seat[0] == 'F':
        highestRow -= (highestRow - lowestRow) / 2
        highestRow = round(highestRow) - 1
    if seat[1] == 'B':
        lowestRow = (highestRow - lowestRow) / 2 + lowestRow
        lowestRow = round(lowestRow)
    if seat[1] == 'F':
        highestRow -= (highestRow - lowestRow) / 2
        highestRow = round(highestRow) - 1
    if seat[2] == 'B':
        lowestRow = (highestRow - lowestRow) / 2 + lowestRow
        lowestRow = round(lowestRow)
    if seat[2] == 'F':
        highestRow -= (highestRow - lowestRow) / 2
        highestRow = round(highestRow) - 1
    if seat[3] == 'B':
        lowestRow = (highestRow - lowestRow) / 2 + lowestRow
        lowestRow = round(lowestRow)
    if seat[3] == 'F':
        highestRow -= (highestRow - lowestRow) / 2
        highestRow = round(highestRow) - 1
    if seat[4] == 'B':
        lowestRow = (highestRow - lowestRow) / 2 + lowestRow
        lowestRow = round(lowestRow)
    if seat[4] == 'F':
        highestRow -= (highestRow - lowestRow) / 2
        highestRow = round(highestRow) - 1
    if seat[5] == 'B':
        lowestRow = (highestRow - lowestRow) / 2 + lowestRow
        lowestRow = round(lowestRow)
    if seat[5] == 'F':
        highestRow -= (highestRow - lowestRow) / 2
        highestRow = round(highestRow) - 1
    if seat[6] == 'B':
        lowestRow = highestRow
    if seat[6] == 'F':
        highestRow = lowestRow
    if seat[7] == 'R':
        lowestCol = (highestCol - lowestCol) / 2 + lowestCol
        lowestCol = round(lowestCol)
    if seat[7] == 'L':
        highestCol -= (highestCol - lowestCol) / 2
        highestCol = round(highestCol) - 1
    if seat[8] == 'R':
        lowestCol = (highestCol - lowestCol) / 2 + lowestCol
        lowestCol = round(lowestCol)
    if seat[8] == 'L':
        highestCol -= (highestCol - lowestCol) / 2
        highestCol = round(highestCol) - 1
    if seat[9] == 'R':
        lowestCol = highestCol
    if seat[9] == 'L':
        highestCol = lowestCol
    
    seatID = lowestRow * 8 + lowestCol
    seatIDs.append(seatID)
    if seatID > highestSeatID:
        highestSeatID = seatID

print(highestSeatID)
res = list(set(range(max(seatIDs) + 1)) - set(seatIDs))

seatIDs = sorted(seatIDs)
last_seat = len(seatIDs) - 1
wrongSeatIDs = []
currentIndex = 0
while currentIndex < last_seat:
    if seatIDs[currentIndex + 1] - seatIDs[currentIndex] == 2:
        wrongSeatIDs.append(seatIDs[currentIndex + 1])
    currentIndex += 1

print(wrongSeatIDs)
#This barely works. Lots of duplicates. Had to manually go through and compare where there was a missing number and no duplicate. Fix later.
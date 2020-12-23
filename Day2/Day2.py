f = open("2020\Day2\Day2Input.txt", "r")
data = f.readlines()
f.close()
numValid = 0
numValidNew = 0

passwords = [line.strip('\n') for line in data]

for password in passwords:
    rules = password.split(" ")
    bounds = rules[0]
    bounds = bounds.split("-")
    lowerBound = bounds[0]
    upperBound = bounds[1]

    key = rules[1].strip(':')

    pw = rules[2]
    count = 0
    for x in pw:
        if x == key:
            count += 1

    if count >= int(lowerBound) and count <= int(upperBound):
        numValid += 1

    validPositionOne = int(lowerBound)
    validPositionTwo = int(upperBound)

    if validPositionOne - 1 < len(pw) and validPositionTwo - 1 < len(pw):
        print(pw[validPositionOne - 1] + ' ' + pw[validPositionTwo - 1])
        if pw[validPositionOne - 1] == key and pw[validPositionTwo - 1] != key:
            numValidNew += 1
        elif pw[validPositionTwo - 1] == key and pw[validPositionOne - 1] != key:
            numValidNew += 1
    
print(numValid)
print(numValidNew)
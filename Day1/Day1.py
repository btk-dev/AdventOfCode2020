f = open("2020\Day1\Day1Input.txt", "r")
data = f.read()

numbers = [int(line) for line in data.split()]

f.close()

myNumbers = []

for number in numbers:
    myNumbers.append(number)

for mult in range(len(myNumbers)):
    for mult2 in range(len(myNumbers)):
        for mult3 in range(len(myNumbers)):
            if (myNumbers[mult] + myNumbers[mult2])  + myNumbers[mult3] == 2020:
                print(myNumbers[mult] * myNumbers[mult2] * myNumbers[mult3])
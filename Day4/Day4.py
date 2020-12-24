with open("2020\Day4\Day4Input.txt") as f:
    lines = f.read()

tests = lines.split("\n\n")
passports = []
for test in tests:
    test = ' '.join(test.splitlines())
    passports.append(test)

validCount = 0
validCount2 = 0

for passport in passports:
    validByr = False
    validIyr = False
    validEyr = False
    validHgt = False
    validHcl = False
    validEcl = False
    validPid = False
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
        validCount += 1
        fields = passport.split(" ")
        for field in fields:
            if 'byr' in field:
                info = field.split(':')
                if int(info[1]) >= 1920 and int(info[1]) <= 2002:
                    validByr = True
            if 'iyr' in field:
                info = field.split(':')
                if int(info[1]) >= 2010 and int(info[1]) <= 2020:
                    validIyr = True
            if 'eyr' in field:
                info = field.split(':')
                if int(info[1]) >= 2020 and int(info[1]) <= 2030:
                    validEyr = True
            if 'hgt' in field:
                info = field.split(':')
                if 'cm' in info[1]:
                    info[1] = info[1][:-2]
                    if int(info[1]) >= 150 and int(info[1]) <= 193:
                        validHgt = True
                if 'in' in info[1]:
                    info[1] = info[1][:-2]
                    if int(info[1]) >=59 and int(info[1]) <=76:
                        validHgt = True
            if 'hcl' in field:
                info = field.split(':')
                if '#' in info[1]:
                    info[1] = info[1][1:]
                    if len(info[1]) <= 6:
                        validHcl = True
                        #May need to change as I don't validate no letters above f
            if 'ecl' in field:
                info = field.split(':')
                if 'amb' in info[1] or 'blu' in info[1] or 'brn' in info[1] or 'gry' in info[1] or 'grn' in info[1] or 'hzl' in info[1] or 'oth' in info[1]:
                    validEcl = True
            if 'pid' in field:
                info = field.split(':')
                if len(info[1]) == 9:
                    validPid = True
        if validPid and validIyr and validHgt and validHcl and validEyr and validEcl and validByr:
            validCount2 += 1

print(validCount)
print(validCount2)
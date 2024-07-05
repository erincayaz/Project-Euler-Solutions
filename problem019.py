def isLeapYear(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True

    return False

def getDayCountOfMonths(n):
    if isLeapYear(n):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

curYear = 1901
curDay = 2
count = 0
while curYear <= 2000:
    dayCount = getDayCountOfMonths(curYear)
    for i in dayCount:
        curDay += i
        curDay %= 7

        if curDay == 0:
            count += 1

    curYear += 1

print(count)

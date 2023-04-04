# 1번
def grade(score):
    if (score > 89):
        return "A"
    elif (score > 79):
        return "B"
    elif (score > 69):
        return "C"
    elif (score > 59):
        return "D"
    else:
        return "F"

# 2번
def quadrant(x, y):
    if (x*y > 0):
        if (x > 0):
            return "제 1사분면"
        else:
            return "제 3사분면"
    else:
        if (x > 0):
            return "제 4사분면"
        else:
            return "제 2사분면"

# 3번
def leapYear(year):
    if (year%400 == 0):
        return "윤년입니다."
    elif (year%4 == 0):
        if (year%100 != 0):
            return "윤년입니다."
        else:
            return "윤년이 아닙니다."
    else:
        return "윤년이 아닙니다."

# 4번
def dice(a, b, c):
    if a == b == c:
        return 10000 + a*1000
    elif a == b or b == c:
        return 1000 + b*100
    elif a == c:
        return 1000 + a*100
    else:
        return max(a, b, c)*100

# 5번
def alarm(time):
    hour = time//100
    minute = time%100
    if minute>44:
        return "%d시 %d분"%(hour, minute-45)
    elif minute<45 and hour>0:
        return "%d시 %d분"%(hour-1, minute+15)
    else:
        return "23시 %d분"%(minute+15)
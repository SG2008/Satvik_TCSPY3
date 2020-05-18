import sys
import math


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "test at line {0} ok.".format(linenum)
    else:
        msg = "test at line {0} FAILED".format(linenum)
    print(msg)


def test_suite():
    test(turn_clockwise("N") == ("E"))
    test(turn_clockwise("S") == ("W"))
    test(turn_clockwise("W") == ("N"))
    test(turn_clockwise("rubbish") == None)
    # test(turn_clockwise(42) == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("halloween") == None)
    test(day_add("Monday", -4) == "Thursday")
    test(day_add("Tuesday", -8) == "Monday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(secs_in(9010) == 10)
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(0, 0, 12, 8) == 0)


def turn_clockwise(compass_point):
    if compass_point == "N":
        return "E"
    if compass_point == "E":
        return "S"
    if compass_point == "S":
        return "W"
    if compass_point == "W":
        return "N"


def day_name(day):
    if day == 0:
        return "Sunday"
    if day == 1:
        return "Monday"
    if day == 2:
        return "Tuesday"
    if day == 3:
        return "Wednesday"
    if day == 4:
        return "Thursday"
    if day == 5:
        return "Friday"
    if day == 6:
        return "Saturday"


def day_num(day):
    if day == "Sunday":
        return 0
    if day == "Monday":
        return 1
    if day == "Tuesday":
        return 2
    if day == "Wednesday":
        return 3
    if day == "Thursday":
        return 4
    if day == "Friday":
        return 5
    if day == "Saturday":
        return 6


def day_add(day, delta):
    return day_name((day_num(day) + delta) % 7)


def days_in_month(month):
    if month == "January":
        return 31
    if month == "February":
        return 28
    if month == "March":
        return 31
    if month == "April":
        return 30
    if month == "May":
        return 31
    if month == "June":
        return 30
    if month == "July":
        return 31
    if month == "August":
        return 31
    if month == "September":
        return 30
    if month == "October":
        return 31
    if month == "November":
        return 30
    if month == "December":
        return 31


def to_secs(hour, minutes, sec):
    return ((hour*60*60) + (minutes*60) + sec)//1


def hours_in(total_secs):
    return total_secs//60//60


def minutes_in(total_secs):
    return total_secs // 60 % 60


def secs_in(total_secs):
    return total_secs % 60


def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope vertical line is undefined"
    return (y2 - y1) / (x2 - x1)


def intercept(x1, y1, x2, y2):
    return y2 - (slope(x1, y1, x2, y2)) * x2


test_suite()

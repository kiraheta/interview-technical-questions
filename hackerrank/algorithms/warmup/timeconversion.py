#!usr/bin/python3

"""
Given a time in 12-hour AM/PM format, convert it to military
(24-hour) time.

Sample Input:
07:05:45PM

Sample Output:
19:05:45
"""


def timeConversion(s):
    hours = s[:2]
    mins = s[3:5]
    am_pm = s[8:10]
    if am_pm == "AM":
        if hours == "12":
            military_time = "00" + s[2:8]
        else:
            military_time = s[:8]
    else:
        if hours != "12":
            hours = int(hours) + 12
            military_time = str(hours) + s[2:8]
        else:
            military_time = s[:8]
    return military_time


if __name__ == '__main__':
    s = "07:05:45PM"
    result = timeConversion(s)
    print(result)

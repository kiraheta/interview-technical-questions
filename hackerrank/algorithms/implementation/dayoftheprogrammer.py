#!usr/bin/python3

"""
Given a year, y, find the date of the 256th day of that year
according to the official Russian calendar during that year. Then
print it in the format dd.mm.yyyy, where dd is the two-digit day,
mm is the two-digit month, and yyyy is y.

Sample Input:
2017

Sample Output:
13.09.2017
"""


def solve(year):
    if year == 1918:
        date = "26.09.1918"
    else:
        if (year < 1918 and year % 4 == 0) or (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            date = "12.09." + str(year)
        else:
            date = "13.09." + str(year)
    return date


if __name__ == '__main__':
    year = 2017
    result = solve(year)
    print(result)

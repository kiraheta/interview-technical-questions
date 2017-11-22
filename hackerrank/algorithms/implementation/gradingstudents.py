#!usr/bin/python3

"""
Given the initial value of grade for each of Sam's students,
write code to automate the rounding process to the following
rules:

-If the difference between the grade and the next multiple of 5
is less than 3, round grade up to the next multiple of 5.

-If the value of grade is less than 38, no rounding occurs as the
result will still be a failing grade.

Sample Input:
4
73
67
38
33

Sample Output:
75
67
40
33
"""


def solve(grades):
    for i in range(len(grades)):
        if 0 <= grades[i] <= 100:
            if grades[i] >= 38:
                difference = 5 - (grades[i] % 5)
                if difference < 3:
                    grades[i] += difference
    return grades


if __name__ == '__main__':
    n = 4
    grades = [75, 67, 40, 33]
    result = solve(grades)
    print("\n".join(map(str, result)))

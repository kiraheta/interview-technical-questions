#!usr/bin/python3

"""
Given the height for each individual candle, find and print the 
tallest number of candles that can successfully be blown out.

Sample Input:
4
3 2 1 3

Sample Output:
2
"""


def birthdayCakeCandles(n, ar):
    tallest_candle = max(ar)
    sum = 0
    for candle in ar:
        if candle == tallest_candle:
            sum += 1
    return sum


if __name__ == '__main__':
    n = 4
    ar = [3, 2, 1, 3]
    result = birthdayCakeCandles(n, ar)
    print(result)

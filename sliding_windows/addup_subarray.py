
"""
Given an array of positive integers, find the subarrays that
add up to a given number

Input - [1, 7, 4, 3, 1, 2, 1, 5, 1]
Sum - 7
"""

def addup(arr, num):
    res = []
    total, i, start_index = 0, 0, 0

    while i < len(arr):
        total = total + arr[i]
        while total > num:
            total = total - arr[start_index]
            start_index = start_index + 1

        if total == num:
            res.append(arr[start_index:i+1])

        i = i + 1

    return res


print(addup([1,7,4,3,1,2,1,5,1], 7))

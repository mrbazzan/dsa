
"""
Given an array of positive integers, find the subarrays that
add up to a given number

Input - [1, 7, 4, 3, 1, 2, 1, 5, 1]
Sum - 7
"""

# [1]
# [1, 7]
# # answer [7]
# [7, 4] --> [4] --> [4, 3]
# # answer = [4, 3]
# [4, 3, 1] --> [3, 1] --> [3, 1, 2] --> [3, 1, 2, 1]
# # answer = [3, 1, 2, 1]
# [3, 1, 2, 1, 5] --> [1, 2, 1, 5] --> [2, 1, 5] --> [1, 5] --> [1, 5, 1]
# # answer = [1, 5, 1]
# [5, 1] --> 

def addup(arr, num):
    res = []
    total = 0

    left, right = 0, 0
    while right<len(arr):
        total = total + arr[right]

        while total>num:
            total = total - arr[left]
            left = left + 1

        if total == num:
            res.append(arr[left:right+1])

        right = right + 1

    return res


print(addup([1,7,4,3,1,2,1,5,1], 7))

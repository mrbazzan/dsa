
"""
Given an array of integers, find maximum sum subarray of the
required size

Input: [-1, 2, 3, 1, -3, 2]
Subarray size: 2
Answer: [2, 3]
"""

def max_subarray(arr, size):
    left, total = 0, 0
    res = float("-inf")
    start, end = 0, 0

    for right in range(1, len(arr)+1):
        total = total + arr[right-1]
        if ((right - left) + 1) > size:
            if total > res:
                res = total
                start, end = left, right

            total = total - arr[left]
            left = left + 1

    return arr[start:end]


print(max_subarray([-1, 2, 3, 1, -3, 2], 2))
print(max_subarray([-1, 2, 3, 0, -3, 9], 2))
print(max_subarray([4, 2, -1, 2, 6, 0, -1], 3))

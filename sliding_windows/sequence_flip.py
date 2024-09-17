
"""
Given an array of 0's and 1's, find the maximum sequence of continuous 1's
that can be formed by flipping at most k 0's to 1's.

Input - [0, 1, 0, 1, 0, 0, 1, 1]
Max Flips(k) - 2
"""

def sequence_flip(arr, k):
    left = 0
    total = 0
    num_flip = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            num_flip = num_flip + 1

        while num_flip > k:
            if arr[left] == 0:
                num_flip = num_flip - 1
            left = left + 1

        total = max(total, len(arr[left:right+1]))
    return total

print(sequence_flip([0,1,0,1,0,0,1,1], 2))


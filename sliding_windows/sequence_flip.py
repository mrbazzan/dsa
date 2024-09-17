
"""
Given an array of 0's and 1's, find the maximum sequence of continuous 1's
that can be formed by flipping at most k 0's to 1's.

Input - [0, 1, 0, 1, 0, 0, 1, 1]
Max Flips(k) - 2
"""

def sequence_flip(arr, k):
    left = 0
    max_details = {'start': 0, 'end': 0, 'length': 0}
    num_flip = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            num_flip = num_flip + 1

        while num_flip > k:
            if arr[left] == 0:
                num_flip = num_flip - 1
            left = left + 1

        length = 1+right - left
        if length > max_details['length']:
            max_details['length'] = length
            max_details['start'] = left
            max_details['end'] = right
    return arr[max_details['start']:max_details['end']+1]

print(sequence_flip([0,1,0,1,0,0,1,1], 2))


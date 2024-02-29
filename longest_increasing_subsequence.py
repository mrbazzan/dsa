
def longest_increasing_subsequence(nums):
    length = 0
    for index in range(len(nums)):
        # TODO: You don't have to store the array, just
        # keep track of its length. Show this in code.
        subsequence = [nums[index]]
        current_largest_number = nums[index]
        for i in range(index+1, len(nums)):
            if nums[i] > current_largest_number:
                subsequence.append(nums[i])
                current_largest_number = nums[i]

        if len(subsequence) > length:
            length = len(subsequence)

    return length


print(longest_increasing_subsequence([60, 22, 9, 31, 18, 43, 21, 50, 10, 80]))


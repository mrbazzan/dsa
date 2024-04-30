

def rob(nums):
    rob0, rob1 = 0, 0
    for num in nums:
        new_rob = max(rob0 + num, rob1)
        rob0 = rob1
        rob1 = new_rob

    return rob1

def circular_rob(nums):
    return max(
        nums[0],
        rob(nums[:-1]),
        rob(nums[1:]),
    )

print(circular_rob([4]))
print(circular_rob([4,2]))
print(circular_rob([2,3,2]))
print(circular_rob([4,2,3]))
print(circular_rob([1,2,3,1]))
print(circular_rob([3,2,6,6,4]))
print(circular_rob([3,2,7,6]))
print(circular_rob([4,1,2,1,3]))
print(circular_rob([3,1,2,1,4]))
print(circular_rob([2,7,7,7,4]))
print(circular_rob([4,2,3,7,4,3,3,4]))

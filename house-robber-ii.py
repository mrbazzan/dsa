

def rob(nums):
    arr = [0 for _ in range(len(nums))]
    arr[0] = nums[0]

    for i in range(1, len(nums)):
        two_step = arr[i-2] if i >= 2 else 0
        arr[i] = max(nums[i] + two_step, arr[i-1])

    return arr[-1]


def circular_rob(nums):
    length = len(nums) - 1

    if length <= 2:
        return max(nums)

    return max(
        nums[0]+rob(nums[2:length]),
        nums[-1]+rob(nums[1:length-1]),
        nums[-2]+rob(nums[:length-2]),
    )

print(circular_rob([2,3,2]))
print(circular_rob([4,2,3]))
print(circular_rob([1,2,3,1]))
print(circular_rob([3,2,6,6,4]))
print(circular_rob([3,2,7,6]))
print(circular_rob([4,1,2,1,3]))
print(circular_rob([3,1,2,1,4]))
print(circular_rob([2,7,7,7,4]))
print(circular_rob([4,2,3,7,4,3,3,4]))



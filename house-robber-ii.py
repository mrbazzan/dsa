
def rob(nums):
    arr = [0 for _ in range(len(nums))]
    arr[0] = nums[0]

    for i, num in enumerate(nums[1:]):
        two_steps_back = arr[i-1] if i >= 1 else 0
        # print(i, two_steps_back, num, arr[i])

        answer = two_steps_back + num

        if (i+2 != len(nums)):
            arr[i+1] = max(((arr[i-1] if i >= 0 else 0) + num), arr[i])
        else:
            arr[i+1] = max(((nums[i-1] if i > 1 else 0) + num), arr[i])

    return arr


print(rob([2,3,2]))
print(rob([1,2,3,1]))
print(rob([3,2,6,6,4]))
print(rob([3,2,7,6]))


# print(rob([1,2,2,4,1]))
# print(rob([1,2,2,2,1]))
# print("---------: ", rob([1,2,3,1]))
# print("---------: ", rob([2,1,1,2]))
# print("---------: ", rob([1,2,7,8,4,5]))
# print("---------: ", rob([2,7,9,3,1]))




from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remainder = nums[i+1:]
            diff = target - nums[i]
            if diff in remainder:
                return [i, i+1+remainder.index(diff) if diff==nums[i] else nums.index(diff)]


print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
print(Solution().twoSum([2, 5, 11, 11, 5], 10))



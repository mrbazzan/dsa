
from typing import List

class Solution:

    def product(self, nums):
        total = 1
        for i in nums:
            total *= i
        return total

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(self.product(nums[:i] + nums[i+1:]))

        return answer

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))

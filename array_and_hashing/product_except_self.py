
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        # sweep through the array to calculate the
        # prefix product for each index
        for i in range(1, len(nums)):
            answer[i] = nums[i-1] * answer[i-1]

        # reverse through the array
        post_product = 1
        for i in range(len(nums)-2, -1, -1):
            post_product *= nums[i+1]
            answer[i] *= post_product

        return answer

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))


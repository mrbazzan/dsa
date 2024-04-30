
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_total = 0
        left, right = 0, len(height)-1

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            max_total = max(max_total, area)

            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_total

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))



from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_total = 0
        length = len(height)

        for i in range(length):
            left, right = 0, length-1
            while height[i] > height[right]:
                right = right - 1

            while height[length-1-i] > height[left]:
                left = left + 1

            max_total = max(max_total,
                            height[i]*(right-i),
                            height[length-1-i] * (length-1-i-left)
                        )

        return max_total

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))


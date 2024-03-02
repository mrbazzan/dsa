
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count, highest = 1, 0
        for i in range(len(nums)):
            number = nums[i]
            while (number+1) in nums:
                count += 1
                number += 1

            if count > highest:
                highest = count

            count = 1

        return highest


print(Solution().longestConsecutive([]))
print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))


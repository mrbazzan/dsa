
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set = set(nums)
        length = 0
        for num in nums:
            # find the starting point of the sequence
            if (num - 1) not in hash_set:
                count = 1
                while (num+count) in hash_set:
                    count += 1
                length = max(count, length)
        return length


print(Solution().longestConsecutive([]))
print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))


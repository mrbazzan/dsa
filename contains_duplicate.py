
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,2,3,1]))


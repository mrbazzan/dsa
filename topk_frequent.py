
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for num in nums:
            frequent[num] = 1 + frequent.get(num, 0)

        return sorted(frequent, key=lambda x: frequent[x], reverse=True)[:k]

print(Solution().topKFrequent([1,1,1,2,2,3],2))
print(Solution().topKFrequent([1],1))
print(Solution().topKFrequent([1,2,1,2,2,1,1,1,2,4,3,4,3,3],3))


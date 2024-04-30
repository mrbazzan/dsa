
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the count of each element
        frequent = {}
        for num in nums:
            frequent[num] = 1 + frequent.get(num, 0)

        # make a bucket sort with the count as key
        bucket = [[] for i in range(len(nums)+1)]
        for num, count in frequent.items():
            bucket[count].append(num)

        # generate the result
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for element in bucket[i]:
                result.append(element)
                if len(result) == k:
                    return result


print(Solution().topKFrequent([1,1,1,2,2,3],2))
print(Solution().topKFrequent([1],1))
print(Solution().topKFrequent([2,1,1,8,8,2,2,1,1,1,2,4,3,4,3,3],4))



from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target_dict = {nums[i]: i for i in range(len(nums))}
        x, y, length = 0, 0, len(nums)
        triplets = set()
        while x <= length-3:
            y = y + 1
            if y == length:
                x, y = x + 1, x + 1

            required = 0 - nums[x] - nums[y]
            if required not in target_dict:
                continue

            z = target_dict[required]
            if x != y and x != z and y != z:
                triplets.add(tuple(sorted((nums[x], nums[y], required))))

        return triplets


print(Solution().threeSum([-1,0,1,2,-1,-4]))
# print(Solution().threeSum([0,1,1]))
# print(Solution().threeSum([0,0,0]))


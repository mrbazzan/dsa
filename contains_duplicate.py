
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,2,3,1]))


def contains(arr):
    hash_set = set()
    for num in arr:
        if num in hash_set:
            return True
        hash_set.add(num)


    return False

print(contains([1,2,3,4]))
print(contains([1,2,3,1]))


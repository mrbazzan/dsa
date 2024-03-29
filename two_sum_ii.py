
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(numbers)-1
        while left_pointer < right_pointer:
            total = numbers[left_pointer] + numbers[right_pointer]
            if total > target:
                right_pointer = right_pointer - 1
            elif total < target:
                left_pointer = left_pointer + 1
            else:
                return [left_pointer+1, right_pointer+1]


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([2, 3, 4], 6))
print(Solution().twoSum([-1, 0], -1))
print(Solution().twoSum([-1, 0, 2, 7, 11, 15], 20))


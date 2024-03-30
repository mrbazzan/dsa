
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        triplets = []
        previous = float('-inf')
        for i in range(len(arr)):
            left, right = i+1, len(arr)-1
            target = 0 - arr[i]

            while (arr[i] != previous) and left < right:
                total = arr[left] + arr[right]

                if total > target:
                    right = right - 1

                elif total < target: # [-4, -1, -1, 0, 1, 2]
                    left = left + 1

                else:
                    triplets.append([arr[i], arr[left], arr[right]])

                    # move forward if the number is same
                    left = left + 1
                    while left < right and arr[left] == arr[left-1]:
                        left = left + 1

            previous = arr[i]

        return triplets


print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,1]))
print(Solution().threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))


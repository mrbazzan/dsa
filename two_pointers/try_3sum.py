
class Solution:
    def three_sum(self, nums):
        sorted_nums = sorted(nums)
        soln = {}
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                goal = sorted_nums[i] + sorted_nums[left] +  sorted_nums[right]
                if goal < 0:
                    left = left + 1
                elif goal > 0:
                    right = right - 1
                else:
                    answer = [
                        sorted_nums[i],
                        sorted_nums[left],
                        sorted_nums[right]
                    ]
                    soln[tuple(answer)] = answer

                    right = right - 1
        return list(soln.values())


# sorted_nums = [-4, -1, -1, 0, 1, 2]

# for loop one
#   i = -4; left = -1; right = 2
#   -4, -1, 2
#   -4, 0, 2
#   -4, 1, 2


# for loop two
#    i = -1; left = -1; right = 2
#    -1, 0, 2
#    -1, 1, 2

# for loop three
# i = -1; left = 0; right = 2
#
nums = [-1,0,1,2,-1,-4]
print(Solution().three_sum(nums))
print(Solution().three_sum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))


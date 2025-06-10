
from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0

        left, right = 0, 1
        while right<len(s):

            output = max(output, len(s[left:right]))

            if s[right] != s[left]:
                print(s[left:right])
                left = right
                print("Change: ", output)

            right = right + 1

        print(s[left:right])
        print("Output: ", output)
        return output


# print(Solution().characterReplacement("XYYX", 0) == 2)
print(Solution().characterReplacement("XYYX", 2) == 4)
# print(Solution().characterReplacement("XYYYX", 2) == 5)
# print(Solution().characterReplacement("AAABABB", 1) == 5)
# print(Solution().characterReplacement("AAABABB", 2) == 6)
# print(Solution().characterReplacement("AABBABB", 1) == 5)
# print(Solution().characterReplacement("CABBABB", 1) == 5)


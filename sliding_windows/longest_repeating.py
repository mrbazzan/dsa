
from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        output = 0
        left, right = 0, 0

        while left < len(s):

            frequent_count = 0
            substring_map= {}
            while right < len(s):

                substring_map[s[right]] = 1 + substring_map.get(s[right], 0)

                # NOTE: Get the most frequent character at each point
                frequent_count = max(frequent_count, substring_map[s[right]])

                if (right-left+1) - frequent_count <= k:
                    output = max(output, (right-left+1))

                right += 1

            left = left + 1
            right = left

        return output


print(Solution().characterReplacement("XYYX", 0) == 2)
print(Solution().characterReplacement("XYYX", 2) == 4)
print(Solution().characterReplacement("XYYXX", 2) == 5)
print(Solution().characterReplacement("XYYXY", 2) == 5)
print(Solution().characterReplacement("XYYXYXY", 2) == 6)
print(Solution().characterReplacement("XYYXYX", 2) == 5)
print(Solution().characterReplacement("XYYYX", 2) == 5)
print(Solution().characterReplacement("AAABABB", 1) == 5)
print(Solution().characterReplacement("AAABABB", 2) == 6)
print(Solution().characterReplacement("AABBABB", 1) == 5)
print(Solution().characterReplacement("CABBABB", 1) == 5)



from typing import List

class Solution:
    def get_map(self, s: str) -> dict:
        hash_map = {}
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        return hash_map

    def characterReplacement(self, s: str, k: int) -> int:

        output = 0
        frequent_count = 0
        left, right = 0, 0
        while left < len(s):
            while right < len(s):
                substring_map = self.get_map(s[left:right+1])

                # NOTE: Get the most frequent character at each point
                frequent_count = max(frequent_count, substring_map[s[right]])

                if len(s[left:right+1]) - frequent_count <= k:
                    output = max(output, len(s[left:right+1]))

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


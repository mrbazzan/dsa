
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

    def freq_count(self, hash_map: dict) -> str:
        count = 0
        for c in hash_map:
            if hash_map[c] > count:
                char = c
                count = hash_map[c]
        return count

    def characterReplacement(self, s: str, k: int) -> int:

        output = 0
        left = 0
        while left < len(s):

            frequent_count = self.freq_count(self.get_map(s[:left]))
            # print(s[:left], frequent_count)

            if len(s[:left]) - frequent_count <= k:
                output = max(output, len(s[:left]))

            left = left + 1

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


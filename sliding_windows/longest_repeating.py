
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

    def freq_char(self, hash_map: dict) -> str:
        count = 0
        char = ''
        for c in hash_map:
            if hash_map[c] > count:
                char = c
                count = hash_map[c]
        return char

    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = self.get_map(s)
        frequent_char = self.freq_char(hash_map)

        output = 0
        left, right = 0, 0
        cont = []
        while left < len(s):

            count = 0
            while (count <= k) and right < len(s):
                if s[right] != frequent_char: count+=1
                right += 1

            cont.append(s[left:right])
            output = max(output, len(s[left:right]))

            left = left + 1
            right = left

        print(cont, frequent_char)
        return output


# print(Solution().characterReplacement("XYYX", 0) == 2)
# print(Solution().characterReplacement("XYYX", 2) == 4)
# print(Solution().characterReplacement("XYYXX", 2) == 5)
# print(Solution().characterReplacement("XYYXY", 2) == 5)
# print(Solution().characterReplacement("XYYXYXY", 2) == 6)

print(Solution().characterReplacement("XYYXYX", 2) == 5)

# print(Solution().characterReplacement("XYYYX", 2) == 5)

print(Solution().characterReplacement("AAABABB", 1) == 5)
print(Solution().characterReplacement("AAABABB", 2) == 6)

# print(Solution().characterReplacement("AABBABB", 1) == 5)
# print(Solution().characterReplacement("CABBABB", 1) == 5)



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

    def char_to_change(self, hash_map: dict) -> str:
        count = 0
        to_change = ''
        for char in hash_map:
            if hash_map[char] > count:
                to_change = char
                count = hash_map[char]
        return to_change

    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = self.get_map(s)
        to_change = self.char_to_change(hash_map)

        output = 0
        left, right = 0, 0
        cont = []
        while left < len(s):

            count = 0
            while right < len(s):
                if s[right] != to_change: count += 1
                if count == k:
                    cont.append(s[left:right+1])
                    output = max(output, len(s[left:right+1]))
                right+=1

            left = left + 1
            right = left

        print(cont)
        return output


# print(Solution().characterReplacement("XYYX", 0) == 2)
# print(Solution().characterReplacement("XYYX", 2) == 4)
# print(Solution().characterReplacement("XYYXX", 2) == 5)

# print(Solution().characterReplacement("XYYXY", 2) == 5)
# print(Solution().characterReplacement("XYYXYXY", 2) == 6)

print(Solution().characterReplacement("XYYXYX", 2) == 5)

# print(Solution().characterReplacement("XYYYX", 2) == 5)
# print(Solution().characterReplacement("AAABABB", 1) == 5)
# print(Solution().characterReplacement("AAABABB", 2) == 6)
# print(Solution().characterReplacement("AABBABB", 1) == 5)
# print(Solution().characterReplacement("CABBABB", 1) == 5)


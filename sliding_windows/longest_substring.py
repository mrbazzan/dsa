
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_dict = {}
        length = 0
        left, right = 0, len(s)

        while left < right:
            if s[left] not in sub_dict:
                sub_dict[s[left]] = left

            else:
                # if character already in sub_dict,
                # start counting from the character after it.
                left = sub_dict[s[left]] + 1

                sub_dict = {}
                sub_dict[s[left]] = left

            left = left + 1
            length = max(length, len(sub_dict))

        return length

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("abcbedbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("pwwkewfgh"))

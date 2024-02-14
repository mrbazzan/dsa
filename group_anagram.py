
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = [[strs[0]]]
        for word in strs[1:]:
            for group in groups:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    break
            else:
                groups.append([word])

        return groups


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams([""]))


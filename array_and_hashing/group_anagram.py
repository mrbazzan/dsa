
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new_str = sorted(strs, key=lambda x: sorted(x))

        first_word = new_str[0]
        groups = [[]]
        for word in new_str:
            if sorted(word) == sorted(first_word):
                groups[-1].append(word)
            else:
                groups.append([word])
                first_word = word

        return groups

        # from collections import defaultdict
        # w = defaultdict(list)
        # for s in strs:
        #     w[''.join(sorted(s))].append(s)

        # return list(w.values())

        # OR

        # result = defaultdict(list)
        # for word in strs:
        #     count = [0] * 26
        #     for c in word:
        #         count[ord(c) - ord("a")] += 1

        #     result[tuple(count)].append(word)

        # return list(result.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams([""]))


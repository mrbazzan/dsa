
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

print(Solution().isAnagram("anagram", "aaangrm"))
print(Solution().isAnagram("cat", "rat"))
print(Solution().isAnagram("ab", "a"))



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # make a dictionary of the character in each words
        # and their counts
        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

        for char, count in dict_t.items():
            if dict_s.get(char) != count:
                return False

        return True

print(Solution().isAnagram("anagram", "abangrm"))
print(Solution().isAnagram("anagram", "aaangrm"))
print(Solution().isAnagram("cat", "rat"))
print(Solution().isAnagram("ab", "a"))


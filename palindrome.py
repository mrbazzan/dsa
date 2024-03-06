
class Solution:
     def isPalindrome(self, s: str) -> bool:
         forward = ""
         backward = ""
         for i in range(len(s)):
             if s[i].isalnum():
                 forward += s[i].lower()
             if s[len(s)-1-i].isalnum():
                 backward += s[len(s)-1-i].lower()

         if forward == backward:
             return True

         return False

print(Solution().isPalindrome("A man, a plan, a canal: Panama "))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
print(Solution().isPalindrome("1221"))


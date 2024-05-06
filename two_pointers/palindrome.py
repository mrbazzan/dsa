
class Solution:
     def isPalindrome(self, s: str) -> bool:
         forward = ""
         backward = ""
         left, right = 0, len(s)-1

         while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while right > left and  not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

         return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama "))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome("    "))
print(Solution().isPalindrome("1221"))


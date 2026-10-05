import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True  # Empty string is a palindrome
            
        # Remove non-alphanumeric characters and convert to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Two-pointer approach
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
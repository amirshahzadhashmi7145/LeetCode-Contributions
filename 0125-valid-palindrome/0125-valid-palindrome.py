class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_string = [ch.lower() for ch in s if ch.isalnum()]
        n = len(cleaned_string)
        for i in range(n//2):
         if cleaned_string[i] != cleaned_string[n-1-i]:
          return False
        return True
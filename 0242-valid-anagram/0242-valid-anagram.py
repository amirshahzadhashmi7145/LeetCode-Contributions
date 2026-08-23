class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
         return False
        n = len(s)
        book = {}
        for ch in s:
         book[ch] = book.get(ch,0)+1
        for ch in t:
         if book.get(ch,0) == 0:
          return False
         book[ch] = book.get(ch,0) - 1
        return True
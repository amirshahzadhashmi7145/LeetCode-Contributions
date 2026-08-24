class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, n = 0, len(s)
        while i < n and s[i] == " ":
          i += 1
    
        sign = 1
        if i < n and s[i] in "+-":
         sign = -1 if s[i] == "-" else 1
         i += 1
 
        result = 0
        while i < n and s[i].isdigit():
         result = result * 10 + int(s[i])
         i += 1
        
        return max(-2**31, min(2**31-1, result*sign)) 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(',']':'[','}':'{'}
    
        for ch in s:
         if ch in pairs:
          if not stack:
           return False
          if stack.pop() != pairs[ch]:
           return False
         else:
          stack.append(ch)
        return len(stack) == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
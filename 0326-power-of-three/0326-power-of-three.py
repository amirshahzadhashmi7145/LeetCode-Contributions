class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
         return False
     
        while n % 3 == 0:
         n //= 3
        return n == 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        while x > 0 or y > 0:
         if x % 2 != y % 2:
          count += 1
         x //= 2
         y //= 2

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
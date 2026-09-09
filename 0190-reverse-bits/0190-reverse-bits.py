class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):          # fixed width — zeros are cargo too
            bit = n % 2              # peel the lowest bit
            result = result * 2 + bit   # push it onto the other side
            n //= 2                  # chop
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
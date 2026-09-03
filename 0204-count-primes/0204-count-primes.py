class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        alive = [True] * n
        alive[0] = alive[1] = False
        i = 2
        while i * i < n:
            if alive[i]:
                for j in range(i * i, n, i):
                    alive[j] = False
            i += 1
        return sum(alive)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
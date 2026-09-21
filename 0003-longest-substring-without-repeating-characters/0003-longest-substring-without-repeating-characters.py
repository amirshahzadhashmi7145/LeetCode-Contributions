class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        left, best = 0, 0

        for right in range(len(s)):
         while s[right] in window:
          window.remove(s[left])
          left += 1
         window.add(s[right])
         
         best = max(best, right - left + 1)

        return best

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = min(strs, key = len)
        for i in range(len(shortest)):
         for word in strs:
           if(word[i] != shortest[i]):
            return shortest[:i]
        return shortest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
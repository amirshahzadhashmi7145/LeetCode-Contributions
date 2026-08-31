class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_ending = nums[0]
        record = nums[0]

        for i in range(1, len(nums)):
         best_ending = max(nums[i], nums[i] + best_ending)
         if best_ending > record:
          record = best_ending
        
        return record
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums
        self.array = nums[:]
        

    def reset(self):
        """
        :rtype: List[int]
        """
        self.array = self.original[:]
        return self.array
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        n = len(self.array)
        for i in range(n-1,0,-1):
         j = random.randint(0, i)
         self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
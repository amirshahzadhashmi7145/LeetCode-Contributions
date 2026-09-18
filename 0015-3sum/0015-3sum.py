class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-2):
         if nums[i] > 0:
          break
         if i > 0 and nums[i] == nums[i-1]:
          continue
         left, right = i+1, n-1
        
         while left < right:
          total = nums[i]+nums[left]+nums[right]
 
          if total < 0:
           left += 1
          elif total > 0:
           right -= 1
          else: 
           result.append([nums[i],nums[left],nums[right]])
           left += 1
           right -= 1
           while left < right and nums[left] == nums[left-1]:
            left += 1

        return result
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
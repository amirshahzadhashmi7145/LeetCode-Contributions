class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        for i in range(1, n+1):

         if (i%3 == 0 and i%5 == 0):
          result.append("FizzBuzz") 
         elif (i%3 == 0):
          result.append("Fizz")
         elif (i%5 == 0):
          result.append("Buzz")
         else:
          result.append(str(i))

        return result
         
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
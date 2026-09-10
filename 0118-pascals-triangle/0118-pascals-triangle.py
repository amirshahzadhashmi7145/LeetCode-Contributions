class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for _ in range(numRows-1):
         prev = triangle[-1]
         row = [1]
         for j in range(1,len(prev)):
          row.append(prev[j-1]+prev[j])
         row.append(1)
         triangle.append(row)
        return triangle

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
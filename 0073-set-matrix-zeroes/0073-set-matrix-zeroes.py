class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
      
        for r in range(m):
         for c in range(n):
          if matrix[r][c] == 0:
           rows.add(r)
           cols.add(c)

        for r in range(m):
         for c in range(n):
          if r in rows or c in cols:
           matrix[r][c] = 0

        return matrix
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
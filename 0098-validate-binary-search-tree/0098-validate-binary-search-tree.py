# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        return self.check(root, float('-inf'),float('inf'))

    def check(self,node,low,high):
         if node == None:
          return True
        
         if node.val <= low:
          return False
    
         if node.val >= high:
          return False

         if self.check(node.left,low,node.val) == False:
          return False

         if self.check(node.right,node.val,high) == False:
          return False

         return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.mirror(root.left,root.right)


    def mirror(self,a,b):
     if a is None and b is None:
      return True
     if a is None or b is None:
      return False
     if a.val != b.val:
      return False
     if self.mirror(a.left,b.right) == False:
       return False
     if self.mirror(a.right,b.left) == False:
       return False
     return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        # find middle
        slow = fast = head
        while fast and fast.next:
         slow = slow.next
         fast = fast.next.next
 
        #reverse from middle
        prev = None
        current = slow
        while current:
         next = current.next
         current.next = prev
         prev = current
         current = next

        #now compare head and prev(head reversed half)
        while prev:
         if (head.val != prev.val):
          return False
         head = head.next
         prev = prev.next
        
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #traverse:
        listOfVal = list()
        while head.next is not None:
            print(head.val)
            listOfVal.append(head.val)
            head = head.next
        listOfVal.append(head.val)
        
        #check palindrome
        length =  len(listOfVal) -1
        i = 0
        
        while (i<length):
            if (listOfVal[i] != listOfVal[length]):
                return False
            else:
                length-=1
                i+=1
        
        return True
            

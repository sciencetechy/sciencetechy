"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        if len(lists) == 1:
            if not lists[0]:
                return None
            else:
                return lists[0]
                
        list1 = lists[0]

        for i in range(0, len(lists)-1, 1):
            list2 = lists[i+1]
            cur = dummy = ListNode()

            while list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
        
            if list1 or list2:
                cur.next = list1 if list1 else list2
            
            list1 = dummy.next
        
        return dummy.next
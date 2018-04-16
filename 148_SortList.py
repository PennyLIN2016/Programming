# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # my solution 680s
    def SortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = {}
        key = []
        while head:
            if head.val not in key:
                s[head.val]= [head]
                key.append(head.val)
            else:
                s[head.val].append(head)
            head = head.next

        key.sort()
        pre = ListNode(-1)
        next = pre
        for i in range(len(key)):
            for value in s[key[i]]:
                value.next = None
                next.next = value
                next = next.next

        return pre.next





if __name__ == '__main__':

    P1 = ListNode(9)
    P2 = ListNode(1)
    P3 = ListNode(2)
    P4 = ListNode(4)

    P1.next = P2
    P2.next = P3
    P3.next = P4

    t = P1
    while t:
        print(t.val)
        t = t.next

    print('before---')

    k = Solution()
    r = k.SortList(P1)

    t = r
    while t:
        print(t.val)
        t = t.next

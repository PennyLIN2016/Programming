# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeKLists1(self, lists: list[ListNode]) -> ListNode:
        # Runtime: 7164 ms, faster than 5.01% of Python3 online submissions for Merge k Sorted Lists.
        # Memory Usage: 17.9 MB, less than 52.10% of Python3 online submissions for Merge k Sorted Lists.
        # time: o(n the number of all nodes) space: o(n)
        curNodes = []
        for node in lists:
            if node: curNodes.append(node)
        if not curNodes: return None
        pre = ListNode(val=0)
        head = pre
        while curNodes:
            v, pos = None, float('inf'), -1
            for i, n in enumerate(curNodes):
                if n.val < v:
                    v = n.val
                    pos = i
            pre.next = curNodes[pos]
            pre = pre.next
            curNodes[pos] = curNodes[pos].next
            if not curNodes[pos]:
                curNodes = curNodes[:pos]+ curNodes[pos+1:] if pos != len(curNodes)-1 else curNodes[:pos]
        return head.next

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # Runtime: 149 ms, faster than 59.69% of Python3 online submissions for Merge k Sorted Lists.
        # Memory Usage: 18.5 MB, less than 19.73% of Python3 online submissions for Merge k Sorted Lists.
        # heapq solution: time: o(m*k) m* k = the number of all nodes space: o(m*k)
        import heapq
        h = []
        pre = ListNode(val=0)
        head = pre
        for node in lists:
            while node:
                # heapq does not support ListNode item
                #heapq.heappush(h, [node.val, node])
                heapq.heappush(h, node.val)
                node = node.next
        while h:

            pre.next = ListNode((heapq.heappop(h)))
            pre = pre.next

        return head.next











if __name__ == '__main__':
    obj = Solution()
    t1 = [[1,4,5],[1,3,4],[2,6]]

    print('input: {}'.format(t1))
    r = obj.mergeKLists(t1)
    print('output: {}'.format(r))
    print('--------END--------')
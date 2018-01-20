# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        '''
        :type lists: List[ListNode]
        :rtype: ListNode
        '''
        null_set = []
        Comp_list = lists[:]

        r = ListNode(-1)
        head = r
        while  len(null_set)< len(lists):
            min_val = float('inf')
            tmp = -1
            for i in xrange(len(Comp_list)):
                if not Comp_list[i]:
                    if i not in null_set:
                        null_set.append(i)
                    continue
                if Comp_list[i].val< min_val:
                    min_val = Comp_list[i].val
                    tmp = i

            r.next = Comp_list[tmp]
            r = r.next
            if Comp_list[tmp]:
                Comp_list[tmp] = Comp_list[tmp].next


        return  head.next


if __name__ == '__main__':

    list1 = []
    list2 = []

    for i in xrange(5):
        node1 = ListNode(2*i)
        list1.append(node1)
        node2= ListNode(2*i+1)
        list2.append(node2)
        if i > 0:
            list1[i-1].next = node1
            list2[i-1].next = node2
    print

    tmp1 = list1[0]
    print 'list 1:',
    while tmp1:
        print tmp1.val,
        tmp1=tmp1.next

    tmp2 = list2[0]
    print '\n list 2:',
    while tmp2:
        print tmp2.val,
        tmp2=tmp2.next


    k = Solution()
    list_total= []
    list_total.append(list1[0])
    list_total.append(list2[0])
    r = k.mergeKLists(list_total)

    tmp3 = r
    print'\n result :',
    while tmp3:
        print tmp3.val,
        tmp3 = tmp3.next
    print

    '''
    k = Solution()
    list_total= []
    list_total.append(ListNode(1))
    list_total.append(ListNode(0))
    r = k.mergeKLists(list_total)

    tmp3 = r
    print' result :',
    while tmp3:
        print tmp3.val,
        tmp3 = tmp3.next
    print
    '''




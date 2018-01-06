class listnode(object):
    def __init__(self,value):
        self.value = value
        self.next = None


class question(object):
    def twoaddtion(self, node1, node2):
        """
        :type node1: listnode
        :type node2: listnode
        :type: return : listnode
        """

        # the return node
        r = listnode(-1)
        tmp1 = r
        carryflag = 0

        while node1 or node2 or carryflag:
            if not (node1 or node2):
                tmp1.value = carryflag
                tmp1.next = None
                carryflag =  0
            elif not node1 and node2:
                if node2.value +carryflag > 9 :
                    tmp1.value = node2.value +carryflag  -10
                    tmp1.next = listnode(-1)
                    carryflag = 1
                else:
                    tmp1.value = node2.value +carryflag
                    carryflag = 0
                    node2 = node2.next
            elif not node2 and node1:
                if node1.value +carryflag > 9 :
                    tmp1.value = node1.value +carryflag  -10
                    tmp1.next = listnode(-1)
                    carryflag = 1
                else:
                    tmp1.value = node1.value +carryflag
                    tmp1.next = listnode(-1)
                    carryflag = 0
                    node1 = node1.next
            else:
                 if (node1.value + node2.value + carryflag) > 9 :
                    tmp1.value = node1.value + node2.value+carryflag  -10
                    tmp1.next = listnode(-1)
                    carryflag = 1
                    node1 = node1.next
                    node2 = node2.next
                 else:
                    tmp1.value = node1.value + node2.value + carryflag
                    tmp1.next = listnode(-1)
                    carryflag = 0
                    node1 = node1.next
                    node2 = node2.next
            tmp1 = tmp1.next

        return r


if __name__ == '__main__':
    l1 = listnode(2)
    l12 = listnode(4)
    l13 = listnode(3)
    l1.next = l12
    l12.next = l13

    l2 = listnode(5)
    l22 = listnode(6)
    l23 = listnode(4)
    l2.next = l22
    l22.next = l23

    try:
        tmp = l1
        print 'Node1:',
        while tmp:
            print tmp.value,
            tmp = tmp.next
        print

        tmp = l2
        print 'Node2:',
        while tmp:
            print tmp.value,
            tmp = tmp.next
        print

        k= question()
        tmp = k.twoaddtion(l1,l2)
        print 'Addition:',
        while tmp.value != -1:
            print tmp.value,
            tmp = tmp.next
        print

    except:
        print 'ERROR!!'



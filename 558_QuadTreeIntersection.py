
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    #Runtime: 224 ms, faster than 89.36% of Python online submissions for Quad Tree Intersection.
    #Memory Usage: 13.7 MB, less than 16.67% of Python online submissions for Quad Tree Intersection.
    # google solution:
    # can't pass on 09/06/2022 neither in python 2 or python 3.9
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        quadTree1.topLeft=self.intersect(quadTree1.topLeft,quadTree2.topLeft)
        quadTree1.topRight=self.intersect(quadTree1.topRight,quadTree2.topRight)
        quadTree1.bottomLeft=self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
        quadTree1.bottomRight=self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)

        if quadTree1.topLeft.isLeaf and quadTree1.topRight.isLeaf and quadTree1.bottomRight.isLeaf and quadTree1.bottomLeft.isLeaf:
            if quadTree1.topLeft.val==quadTree1.topRight.val==quadTree1.bottomLeft.val==quadTree1.bottomRight.val:
                quadTree1.isLeaf=True
                quadTree1.val=quadTree1.topLeft.val
        return quadTree1




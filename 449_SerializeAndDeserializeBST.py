# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Codec:
    #Runtime: 64 ms, faster than 66.63% of Python online submissions for Serialize and Deserialize BST.
    #Memory Usage: 19.5 MB, less than 70.97% of Python online submissions for Serialize and Deserialize BST.
    # BST: The right nodes >= root ; the left nodes<= root.
    # for BST: Preoder series  can locate each node
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:return ''
        left= self.serialize(root.left)
        right=self.serialize(root.right)
        res=str(root.val)
        if left:res+='_'+left
        if right:res+='_'+right
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        nlist= collections.deque(int(val) for val in data.split('_'))
        def build(minV,maxV):
            if nlist and minV<nlist[0]<maxV:
                val=nlist.popleft()
                root= TreeNode(val)
                root.left=build(minV,val)
                root.right=build(val,maxV)
            return root
        return build(float('-inf'),float('inf'))



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



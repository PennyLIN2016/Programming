# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    def sortedArrayToBST1(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            midPos = len(nums) / 2
            mid = nums[midPos]
            root = TreeNode(mid)
            root.left = self.sortedArrayToBST(nums[:midPos])
            root.right = self.sortedArrayToBST(nums[midPos+1:])
            return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def Convert_next(nums,start,end):
            if start> end:
                return None
            mid = (start+end+1)/2
            root = TreeNode(nums[mid])
            if start< mid:
                root.left = Convert_next(nums,start,mid-1)
            if mid < end:
                root.right = Convert_next(nums,mid+1,end)
            return root

        if not nums or len(nums)== 0:
            return None
        return Convert_next(nums,0,len(nums)-1)


if __name__ == '__main__':
    inputs = [-10,-3,0,5,9]

    k = Solution()
    r = k.sortedArrayToBST(inputs)
    print r






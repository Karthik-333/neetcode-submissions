# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            leftmax=dfs(node.left)
            rightmax=dfs(node.right)
            terminalpath=node.val+leftmax+rightmax
            val=max(node.val, node.val+leftmax, node.val+rightmax)
            res=max(res,val,terminalpath)  
            return val
        dfs(root)    
        return res      
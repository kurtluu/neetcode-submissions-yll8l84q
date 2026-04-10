# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inIdx = {val:i for i, val in enumerate(inorder)}
        preIdx = 0

        def dfs(left, right):
            nonlocal preIdx

            if left > right:
                return

            rootVal = preorder[preIdx]
            preIdx += 1

            root = TreeNode(rootVal)
            m = inIdx[rootVal]

            root.left = dfs(left, m - 1)
            root.right = dfs(m + 1, right)

            return root

        return dfs(0, len(inorder) - 1)
            



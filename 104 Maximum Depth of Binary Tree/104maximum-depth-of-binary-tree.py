# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     curr = root

    #     # while curr:
    #     #     if curr.left:
    #     #         curr = curr.left
    #     #     elif curr.right:
    #     #         curr = curr.right
    #     if curr:
    #         d = self.dfs(curr,1,1)
    #     # self.dfs(curr.right)
    #     return d

    # def dfs(self, curr, depth, ldepth):
    #     ldepth = max(depth, ldepth)
    #     if curr.left:
    #         self.dfs(curr.left, depth+1, ldepth)
    #     # fdepth = max(depth, fdepth)
    #     depth = 0
    #     if curr.right:
    #         self.dfs(curr.right, depth+1, ldepth)

    #     # return max(ldepth, rdepth)
    #     return ldepth
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



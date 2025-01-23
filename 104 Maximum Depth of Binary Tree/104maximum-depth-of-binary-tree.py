# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        """
        Let's do it in iterative BFS way
        """
        if root is None:
            return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                child = q.popleft()
                if child.left:
                    q.append(child.left)
                if child.right:
                    q.append(child.right)
            level += 1
        return level    



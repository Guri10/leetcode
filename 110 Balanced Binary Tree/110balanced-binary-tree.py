# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(root):
            if root is None:
                return [True, 0]
            
            leftHeight = checkHeight(root.left)
            rightHeight = checkHeight(root.right)

            balanced = leftHeight[0] and rightHeight[0] and (abs(leftHeight[1] - rightHeight[1]) <=1)

            return [balanced, 1 + max(leftHeight[1], rightHeight[1])]

        return checkHeight(root)[0]


    #     if root is None:
    #         return True       
    #     q = deque([root])
    #     while q:       
    #         for i in range(len(q)):
    #             child = q.popleft()
    #             leftHeight, rightHeight = 0,0
    #             if child.left:
    #                 leftHeight = self.treeHeight(child.left)
    #                 q.append(child.left)
    #             if child.right:
    #                 rightHeight = self.treeHeight(child.right)
    #                 q.append(child.right)
    #             # print(diff, abs(leftHeight - rightHeight))
    #             # diff = max(diff, abs(leftHeight - rightHeight))
    #             if abs(leftHeight - rightHeight) > 1:
    #                 return False     
    #     return True
 
    # def treeHeight(self, root):
    #     if root is None:
    #         return 0
        
    #     return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))
        
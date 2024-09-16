# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        temp = root
        node = root
        ans = []
        
        while True:
            if temp:
                stack.append(temp)
                # par = temp
                temp = temp.left
            # print(stack1)
            elif (len(stack)==0):
                break
            elif (temp == None):
                # ans.append(stack1.pop())
                # temp = par.right

                node = stack.pop()
                ans.append(node.val)
                temp = node.right
        return ans
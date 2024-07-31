class Solution:
    def maxDepth(self, s: str) -> int:
        '''
        stack = []
        max_reached =0
        c = 0
        for ele in s:
            if ele == "(":
                stack.append(ele)
                c+=1
                if c>max_reached:
                    max_reached = c
            elif ele == ")":
                stack.pop()
                c-=1
        return max_reached
        '''
        stack = []
        max_reached =0
        for ele in s:
            if ele == "(":
                stack.append(ele)
                if len(stack)>max_reached:
                    max_reached = len(stack)
            elif ele == ")":
                stack.pop()
        return max_reached

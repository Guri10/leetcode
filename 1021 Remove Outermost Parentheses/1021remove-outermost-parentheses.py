class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack1 =[]
        ans = ""
        i=0
        for ele in s:
            if ele == '(':
                # print(len(stack1))
                if (len(stack1))!=0:
                    ans += ele
                    # print("first")
                    # i+=1
                stack1.append(ele)
                # print('second')
            else:
                if len(stack1)==1:
                    stack1.pop()
                elif len(stack1)>1:
                    stack1.pop()   
                    ans += ele   
        return ans





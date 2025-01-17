class Solution:
    def isValid(self, s: str) -> bool:
        stk1 = []
        dic = {'(':')', '[':']', '{':'}'}
        for char in s:
            if char in '({[':
                stk1.append(char)
            # elif char in closing and len(stk1) != 0 :
            #     print('entered')
            #     if dic[stk1[-1]] == char:
            #         stk1.pop()
            #     else:
            #         return False
            # elif char in closing and len(stk1) == 0 :
            #     return False

            else:
                if len(stk1) != 0 and dic[stk1[-1]] == char:
                    stk1.pop()
                else:
                    return False
        
        return not stk1


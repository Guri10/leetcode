class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        
        for i in t:
            if i not in dic:
                return False
            dic[i] -= 1
            if not dic[i]:
                del dic[i]

        return not bool(dic)
        
     
     
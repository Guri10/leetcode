class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c = 0
        sPointer = 0
        tPointer = 0
        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                c+=1
                sPointer+=1
            tPointer+=1
        print(c)
        if c == len(s):
            return True
        else:
            return False
        

        
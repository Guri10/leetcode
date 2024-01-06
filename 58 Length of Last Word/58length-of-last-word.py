class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        le = 0
        # if len(s) == 1 and s!=' ':
        #     return 1

        start = len(s)-1
        while s[start] == ' ' and start > -1:
            start -= 1
        while s[start] != ' ' and start > -1:
            le += 1
            start -= 1
        
        return le

            



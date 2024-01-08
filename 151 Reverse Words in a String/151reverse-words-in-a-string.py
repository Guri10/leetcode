class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        word_start = None
        for i in range(len(s)):
            if s[i] != ' ' and word_start is None:
                word_start = i
                dic[word_start] = s[i]
            elif s[i] != ' ':
                dic[word_start] += s[i]
            else:
                word_start = None
        # print(dic)
        lis = sorted(dic.keys())
        # print(lis)
        d = []
        for i in range(len(lis)-1,-1,-1):
            d.append(dic[lis[i]])
        return ' '.join(d)


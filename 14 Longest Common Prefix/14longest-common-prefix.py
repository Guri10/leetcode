class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # result = ""
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i>=len(s) or s[i] != strs[0][i]:
        #             return result
        #     result += s[i]
        # return result
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

                
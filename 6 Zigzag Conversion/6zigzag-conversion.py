class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ""
        for row in range(numRows):
            increment = 2 * (numRows-1)
            for i in range(row, len(s), increment):
                res += s[i]
                if (0 < row < numRows-1) and ((i + increment - 2*row) < len(s)):
                    res += s[i + increment - 2*row]

        return res
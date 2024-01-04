class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 0:
            return 0

        dic = [1] * n  # Initialize all candy counts to 1

        # Forward pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dic[i] = dic[i - 1] + 1

        # Backward pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dic[i] = max(dic[i], dic[i + 1] + 1)

        res = sum(dic)
        return res

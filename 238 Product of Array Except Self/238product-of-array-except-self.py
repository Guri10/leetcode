class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix 
            prefix *= nums[i]
        # print(result)
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
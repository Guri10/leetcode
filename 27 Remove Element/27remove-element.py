class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for ele in nums:
            if ele != val:
                nums[k] = ele
                k+=1
        return k


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j=0,1
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i] = nums[j]
                j+=1
        return i+1
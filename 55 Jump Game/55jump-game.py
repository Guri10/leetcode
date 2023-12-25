class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump = -float('inf')
        for i in range(len(nums)):
            jump = max(jump, nums[i])
            if i == len(nums)-1:
                return True
            if jump == 0:
                return False
            jump = jump - 1

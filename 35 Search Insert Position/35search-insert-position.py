class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)-1
        mid = (right + left) // 2

        while left<=right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
                mid = (right + left) // 2
            elif nums[mid] > target:
                right = mid-1
                mid = (right + left) // 2
        return mid+1
        
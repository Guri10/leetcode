class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        left = 0
        right = k-1
        while (left < right):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        left = k
        right = len(nums)-1
        while (left < right):
            temp =  nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1


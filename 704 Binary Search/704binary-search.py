class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # if target == nums[0]:
        #     return 0

        
        while left<=right:
            mid = (left + right) // 2 
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
                # mid = (left + right) //2
                # mid = 
            elif target > nums[mid]:
                left = mid + 1
                # mid = (left + right) // 2
        return -1



        
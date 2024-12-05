class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub=0
        for i in range(len(nums)):
            sub = target - nums[i]
            # sub = abs(sub)

            for j in range(i+1,len(nums)):
                if nums[j] == sub:
                    return i,j
                
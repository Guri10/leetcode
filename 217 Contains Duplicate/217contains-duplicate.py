class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for ele in nums:
            if ele in dic:
                return True
            dic[ele] = 1
        return False
                


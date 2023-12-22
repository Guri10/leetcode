class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        maxi = 0
        maxi_ele = 0
        for ele in nums:
            if ele not in dic:
                dic[ele]=1
            else:
                dic[ele]+=1
        for key,value in dic.items():
            if value>len(nums)/2 and value>maxi:
                maxi = value
                maxi_ele = key
        return maxi_ele
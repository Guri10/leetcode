class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left=height[0]
        max_right=height[len(height)-1]
        res=0
        i=0
        j=len(height)-1
        while i<j:
            if max_left<=max_right:
                
                i+=1 
                res+= max(max_left-height[i],0)
                max_left=max(height[i],max_left)
                
            else:
            
                j-= 1 
                res+= max(max_right-height[j],0)
                max_right=max(height[j],max_right)
        return res
        
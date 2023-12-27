class Solution(object):
    def jump(self,nums):
        n = len(nums)
        if n <= 1:
            return 0

        # The max position one can reach from the current position
        max_reach = nums[0]
        # The number of steps one can still take before needing to jump again
        steps = nums[0]
        # Number of jumps needed
        jumps = 1

        for i in range(1, n):
            # If the current index is beyond the maximum reachable index, then jump
            if i > max_reach:
                jumps += 1
                max_reach = steps
            steps = max(steps, i + nums[i])

        return jumps


# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:   
        nums.sort()
        n = len(nums)
        res = float("inf")
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right :
                sums = nums[i] + nums[left] + nums[right]
                if sums == target:return target
                if abs(res-target) > abs(sums-target):
                    res = sums
                if sums > target:
                    right -= 1
                elif sums < target:
                    left += 1
        return res
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution:
    def search(self, nums, target):
	lo, hi, k = 0, len(nums) - 1, -1
	while lo <= hi:
	    m = (lo + hi) // 2
	    if m == len(nums) - 1 or nums[m] > nums[m+1]:
		k = m + 1
		break
	    elif m == 0 or nums[m] < nums[m-1]:
		k = m
		break
	    if nums[m] > nums[0]:
		lo = m + 1
	    else:
		hi = m - 1
	i = (bisect.bisect_left(nums[k:] + nums[:k], target) + k) % max(len(nums), 1)
	return i if nums and nums[i] == target else -1
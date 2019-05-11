# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b, m = *sorted((nums1, nums2), key=len), (len(nums1) + len(nums2) - 1) // 2
        self.__class__.__getitem__ = lambda self, i: m-i-1 < 0 or a[i] >= b[m-i-1]
        i = bisect.bisect_left(self, True, 0, len(a))
        r = sorted(a[i:i+2] + b[m-i:m-i+2])
        return (r[0] + r[1 - (len(a) + len(b)) % 2]) / 2
        
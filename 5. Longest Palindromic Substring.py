# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_len = 1
        n = len(s)
        start = 0
        for i in range(1,n):
            even = s[i-max_len:i+1]
            odd = s[i - max_len-1:i+1]
            #print(even,odd)
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
            elif i - max_len >=0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                
        #print(start,max_len)
        return s[start: start+max_len]
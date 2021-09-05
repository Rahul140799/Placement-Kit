# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists only of lowercase English letters.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        d = {}
        
        def recurse(s):
            if s in d:
                return d[s]
            
            if not s:
                return 0
            
            if len(s) == 1:
                return 1
            
            if s[0] == s[-1]:
                output = 2 + recurse(s[1:-1])
            else:
                output = max(recurse(s[1:]), recurse(s[:-1]))
            
            d[s] = output
            return output
        
        return recurse(s)
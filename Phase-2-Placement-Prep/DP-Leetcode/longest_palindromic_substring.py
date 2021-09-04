# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Example 3:

# Input: s = "a"
# Output: "a"

# Example 4:

# Input: s = "ac"
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.



class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def lps(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        

        st = ""
        
        for i in range(len(s)):

            lower_word = lps(i,i,s)
            if len(st) < len(lower_word):
                st = lower_word
            
            upper_word = lps(i,i+1,s)
            if len(st) < len(upper_word):
                st = upper_word        
        return st
        
#TC -> O(n^2)
#SC -> O(1)
    
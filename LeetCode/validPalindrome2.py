def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        if s == s[::-1]:
            return True
        
        while(left <= right):
            if s[left] != s[right]:
                break
            
            left += 1
            right -= 1
            
        left_track  = s[:left] + s[left+1:]
        right_track = s[:right] + s[right+1:]
        
        if (left_track == left_track[::-1]) or (right_track == right_track[::-1]):
            return True
        else:
            return False
        

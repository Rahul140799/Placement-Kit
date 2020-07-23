import re
class Solution:
    def reverseWords(self, s: str) -> str:
        temp = re.sub(' +', ' ',s)
        new = temp.strip(' ')
        arr = new.split(' ')
        st = ""
        for i in arr[::-1]:
            st += i + " "
        return st.rstrip(' ')

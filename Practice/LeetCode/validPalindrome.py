import string
def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i not in string.punctuation and i not in string.whitespace:
                arr.append(i)
        st = ""
        for i in arr:
            st+=i
        st = st.lower()
        rev = st[::-1]
        if rev == st:
            return True
        else:
            return False

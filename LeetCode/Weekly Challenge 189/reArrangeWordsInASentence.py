def arrangeWords(self, text: str) -> str:
        x = text.split()
        x.sort(key=len)
        st = ""
        for i in x:
            st = st + " " + i.lower()
        
        y = st.split()
        z = y[0][0].upper()
        new = y[0][0].replace(y[0][0],z)
        temp = new
        for i in y[0][1:]:
            temp += i
        out = temp
        for i in y[1:]:
            out = out + " " + i
        return out

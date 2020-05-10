def findComplement(self, num: int) -> int:

        x = bin(num).replace('0b','')
        print(x)

        st = ""
        for i in x:
            if i == '1':
                st += '0'
            if i == '0':
                st += '1'

        return int(st,2)

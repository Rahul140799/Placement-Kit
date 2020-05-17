def defangIPaddr(self, address: str) -> str:
        st = ""
        for i in address:
            if i != ".":
                st += i
            else:
                st += "[.]"
            
        return st
                

def plusOne(self, digits: List[int]) -> List[int]:
        st = ""
        for i in digits:
            st += str(i)
        res = int(st)+1
        return list(str(res))

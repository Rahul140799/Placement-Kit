def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        out = []
        res = []
        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if set(favoriteCompanies[i]).issubset(set(favoriteCompanies[j])) and i!=j:
                    out.append(i)
        temp = set(out)
        for i in range(len(favoriteCompanies)):
            if i not in temp:
                res.append(i)
        return res
        

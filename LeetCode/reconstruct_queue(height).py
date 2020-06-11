def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        temp = sorted(people, key = lambda x:-x[0]) #Sorting based on first element in descending order
        for i in temp:
            res.insert(i[1],i)                      #Insert into new array based on index, (i.e) i[1] into the i'th index
        return res
            

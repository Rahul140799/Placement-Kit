from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dict_list = defaultdict(list)
        degree = [0] * numCourses
        res = []
        
        for course,needed in prerequisites:
            dict_list[needed].append(course)
            degree[course] += 1
            
        for i in range(numCourses):
            if degree[i] == 0:
                res.append(i)
                
        for i in range(numCourses):
            if i == len(res):
                return []
            
            curr_course = res[i]
            for next_course in dict_list[curr_course]:
                degree[next_course] -= 1
                if degree[next_course] == 0:
                    res.append(next_course)
                    
        return res

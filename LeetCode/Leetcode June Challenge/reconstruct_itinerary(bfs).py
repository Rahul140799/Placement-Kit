def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[1])
        #print(tickets)
        
        graph = {}
        
        for u, v in tickets:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
        #print(graph)
        
        itinerary, stack = [], [("JFK")]
        while stack:
            curr = stack[-1]
            
            if curr in graph and len(graph[curr]) > 0:
                stack.append(graph[curr].pop(0))
                #print("stack:",stack)
            else:
                itinerary.append(stack.pop())
                #print("itinerary:",itinerary)
        return itinerary[::-1]
        

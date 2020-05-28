import sys
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

#creating 2 empty array for keeping track of visited nodes of graph and the queue for the sequence of access

visited = []   #when a node is visited , it is added to visited array
flag=0	         #setting up flag variable to tell when the element is found


def dfs(visited, graph, node,elementToSearch):
    
    if node not in visited:
        print (node)
        if node==elementToSearch:
            print ('element found')
            h= input ("Enter 1 to exit")
            sys.exit()
            
        else:		#if neighbours of the element not visited then it is added to the stack	
             visited.append(node)
             for neighbour in graph[node]:
                 dfs(visited, graph, neighbour,elementToSearch)
                 dfs(visited, graph, 'A',elementToSearch)
    
elementToSearch= input ("Enter the element to search: ")
dfs(visited, graph, 'A',elementToSearch)
print ('element not found')

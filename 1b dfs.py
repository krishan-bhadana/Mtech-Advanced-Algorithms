import sys
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []
flag=0

def dfs(visited, graph, node,elementToSearch):
    
    if node not in visited:
        print (node)
        if node==elementToSearch:
            print ('element found')
            h= input ("Enter 1 to exit")
            sys.exit()
            
        else:
             visited.append(node)
             for neighbour in graph[node]:
                 dfs(visited, graph, neighbour,elementToSearch)
                 dfs(visited, graph, 'A',elementToSearch)
    
elementToSearch= input ("Enter the element to search: ")
dfs(visited, graph, 'A',elementToSearch)
print ('element not found')


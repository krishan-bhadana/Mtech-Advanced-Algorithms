graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = [] 

def bfs(visited, graph, node, elementToSearch):
  visited.append(node)
  queue.append(node)
  flag=0

  while queue:
    s = queue.pop(0) 
    print (s, end = " ")
    if s==elementToSearch:
        print ('element found')
        flag=1
        break
    else:
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
  if flag==0:
      print ('not found')
      
elementToSearch= input ("Enter the element to search: ")
bfs(visited, graph, 'A',elementToSearch)
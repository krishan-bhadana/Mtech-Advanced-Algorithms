# Initialising a graph
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

#creating 2 empty array for keeping track of visited nodes of graph and the queue for the sequence of access
visited = []
queue = [] 

def bfs(visited, graph, node, elementToSearch):
  visited.append(node)   #when a node is visited , it is added to visited array
  queue.append(node)    #node added to queue
  flag=0		   #setting up flag variable to tell when the element is found

  while queue:
    s = queue.pop(0)     #getting first element of queue
    print (s, end = " ")
    if s==elementToSearch:
        print ('element found')
        flag=1
        break
    else:			#if neighbours of the element not visited then it is added to the queue			
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
  if flag==0:
      print ('not found')
      
elementToSearch= input ("Enter the element to search: ")
bfs(visited, graph, 'A',elementToSearch)

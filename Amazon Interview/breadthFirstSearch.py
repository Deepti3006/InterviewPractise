graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
visited =[]
queue =[]

def breathFirstSearch(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s= queue.pop(0)
        print(s)
        for neigbhour in graph[s]:
            if neigbhour not in visited:
                visited.append(neigbhour)
                queue.append(neigbhour)

breathFirstSearch(visited,graph,"A")
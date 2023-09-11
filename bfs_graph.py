from tabulate import tabulate


_graph = {
  "A":['F','C','B'],
  "B":['A','C','B'],
  "C":['A','B','D','E','F','G'],
  "D":['C','F','E','J'],
  "E":['C','D','G','J','K'],
  "F":['A','C','D'],
  "G":['B','C','E','K'],
  "J":['D','E','K'],
  "K":['E','G','J']
}
'''TO DO list 
   Current Node 
   , Queue 
   , Processoed Nodes Status Matrix 
   '''

_visited=[]
_queue=[]


def bfs(_visited,_graph,node):
    print("Current Nodes")
    _visited.append(node)
    _queue.append(node)
    
    while _queue:
        S = _queue.pop(0)
      
        print(S)

        for _adjacent in _graph[S]:
            if _adjacent not in _visited:
                _visited.append(_adjacent)
                _queue.append(_adjacent)
                
                print(_queue)
                
                print(_visited)
                

bfs(_visited,_graph,'A')
    
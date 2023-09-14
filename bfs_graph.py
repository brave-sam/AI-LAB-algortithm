from tabulate import tabulate

def bfs(graph):
    table = []
    headers = ["Current Node", "Queue", "Processed Nodes", "Status"]
    visited = {node: 1 for node in graph}
    start_node = next(iter(graph))
    queue = [start_node]
    visited[start_node] = 2
    processed_nodes = []
    
    while queue:
        current_node = queue.pop(0)
        processed_nodes.append(current_node)
        
        for neighbor in graph[current_node]:
            if visited[neighbor] == 1:
                queue.append(neighbor)
                visited[neighbor] = 2
        
        visited[current_node] = 3
        table.append([current_node, " ".join(queue), " ".join(processed_nodes), visited.copy()])
    
    print(tabulate(table, headers=headers, tablefmt="grid"))

graph = {
    "a": ["f", "c", "b"],
    "b": ["a", "c", "g"],
    "c": ["a", "b", "d", "e", "f", "g"],
    "d": ["c", "f", "e", "j"],
    "e": ["c", "d", "g", "j", "k"],
    "f": ["a", "c", "d"],
    "g": ["b", "c", "e", "k"],
    "j": ["d", "c", "j"],
    "k": ["e", "g", "j"],
}

bfs(graph)

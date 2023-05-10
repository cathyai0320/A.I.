from collections import deque

def BFS_Cathy(graph, initial, goal):
    # Check if the graph exists
    if hasattr(graph, 'graph'):
        return "Sorry, graph not found"
    
    # If any names passed as arguments do not exist on the graph 
    #then you should display an appropriate message (change the value of initial to value not found in the graph )
    if initial not in graph or goal not in graph:
        return f"Error: {initial} or {goal} is not in the graph data."
    
    # Queue to keep track of the nodes to visit
    queue = deque()
    queue.append(initial)
    
    # Dictionary to keep track of visited nodes and their parents
    visited = {initial: None}
    
    # Traverse the graph using BFS
    while queue:
        node = queue.popleft()
        if node == goal:
            # Build the path from end to start using the visited dictionary
            path = [goal]
            parent = visited[goal]
            while parent:
                path.append(parent)
                parent = visited[parent]
            return path[::-1]
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = node
                queue.append(neighbor)
    
    # If any of the passed arguments do not exist then 
    #an appropriate message should be returned.
    return "No path found"


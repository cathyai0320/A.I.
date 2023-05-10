'''
@author: Catherine Pequino
'''
import queue
from State import State
from Node import Node
from TreePlot import TreePlot
from collections import deque

def performUCSSearch():
    """
    This method performs uniform cost search
    """
    
    # create a priority queue
    queue = deque([])
    #since it is a graph, we created visited list
    visited = []
    #create root node
    initialState = State()
    root = Node(initialState)
    #adding to queu and visited list
    queue.append(root)
    visited.append(root.state.name)
    #check if there is something in queu to dequeue
    while len(queue)>0:
        
        #get first item in queue
        currentNode = queue.popleft()
        print(("--dequeu--"), currentNode.state.name)
        
        #check if this is goal state
        if currentNode.state.checkGoalState():
            print("reached goal state")
            #print the path
            print("-----------")
            print("Path")
            currentNode.printPath()
            break
        #get the child node
        childStates = currentNode.state.successorFunction()
        for childState in childStates:
            
            childNode = Node(State(childState))
            
            #check if node is not visited
            if childNode.state.name not in visited:
                
                #add to tree and queue
                currentNode.addChild(childNode)
                queue.append(childNode)
    #print tree
    print ("------------")
    print("Tree")
    root.printTree()
performUCSSearch()
      
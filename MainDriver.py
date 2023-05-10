# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:32:38 2023

@author: Catherine Pequino
"""

from GraphData import graph
from QueueBFS import BFS_Cathy

# Dolly needs to get introduced to you
#path = BFS_Cathy(graph, 'Dolly', 'Cathy')
#As output print the final path and the tree traversed, 
#you can use Graphviz to illustrate your results, or print out.
# Output: ['Dolly', 'Bob', 'Adam', 'Ema', 'ChatGPT']
#print(path)


# George needs to get introduced to Bob
path = BFS_Cathy(graph, 'George', 'Bob')
#As output print the final path and the tree traversed, 
#you can use Graphviz to illustrate your results, or print out.
# Output: ['George', 'Cathy', 'Adam', 'Bob']
print(path) 

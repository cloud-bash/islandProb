# 200. Number of Islands

from ast import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # We want ints, not strs.
        grid = matrixAsInts(grid)
        # Let's represent it as a graph.
        graph = asGraph(grid)
        # Count the number of connected components.
        components = len(getConnectedComponents(graph))
        return components

def getConnectedComponents(graph):
    adjs = getAdjacencyLists(graph)
    components = []
    while len(adjs) > 0:
        # 1. Pick a random unvisited vertex.
        # u is the vertex, vs is its adj list.
        u, vs = adjs.popitem()
        # 2. Make a new component out of it.
        # Our current component:
        component = {u}
        components.append(component)
        # Add u's adjs to the component.
        component.update(vs)
        # 3. Repeatedly add vertices connected to the component.
        changed = True
        while changed:
            changed = False
            for v in list(component):
                if v in adjs.keys():
                    ws = adjs.pop(v)
                    component.update(ws)
                    changed = True
    return components

# adjs = {
    # # A: {B},
    # # B: {F,A},
    # C: {E},
    # D: {E,H},
    # E: {C,D,G,H},
    # # F: {B},
    # G: {E,H},
    # H: {D,E,G},
# }

adjs = {
    'A': {'B'},
    'B': {'F','A'},
    'C': {'E'},
    'D': {'E','H'},
    'E': {'C','D','G','H'},
    'F': {'B'},
    'G': {'E','H'},
    'H': {'D','E','G'},
}



# adjs = {
#     1: {5,2},
#     2: {3,5,1},
#     3: {4,2},
#     4: {6,5,3},
#     5: {1,2,4},
#     6: {4},
# }



# ((0,0), (0,1))

#     1 - 1   0   0   0
#     |   |            
#     1 - 1   0   0   0
# 
#     0   0   1   0   0
# 
#     0   0   0   1 - 1

# {(1, 2),
 # (1, 5),
 # (2, 1),
 # (2, 3),
 # (2, 5),
 # (3, 2),
 # (3, 4),
 # (4, 3),
 # (4, 5),
 # (4, 6),
 # (5, 1),
 # (5, 2),
 # (5, 4),
 # (6, 4)}



# A 300x300 grid will have up to 90,000 nodes.
# Matrix multiplication will be done on up to 90000 nodes.
# Matrix mult is O(n^3) (naively, at least).
# So each matrix mult is on the order of 90000^3.


def asGraph(grid):
    ...

def getAdjacencyLists(graph):
    ...

def matrixAsInts(grid):
    gridAsNums = []
    for row in grid:
        rowAsNums = []
        for x in row:
            rowAsNums.append(int(x))
        gridAsNums.append(rowAsNums)
    return gridAsNums

# More-pythonic way:
def matrixAsInts(grid):
    return [[int(x) for x in row] for row in grid]


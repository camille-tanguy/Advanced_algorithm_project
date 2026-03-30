from graph import Graph
from min_span_tree import *
import random

###########graph representation######################

def transform_graph2adl(graph):
    
    '''this function is to transform an object of the 
    class Graph to the corresponding adjacency list'''
    
    graph_adl={}
    for (u, v), w in graph.weight.items():
        if u not in graph_adl:
            graph_adl[u]={v:w}
        else: 
            graph_adl[u][v]=w
    
    return graph_adl

###########two times of mst with dfs################

def dfs_2_mst(graph_mst, s):

    '''This function is described in Step 2 of
    Question 3 in the project description.'''

    stack=[s]
    visited={v:0 for v in graph_mst}
    
    two_mst_dfs=[]
    

    while stack:
        node = stack[-1]

        if visited[node] == 0:
            two_mst_dfs.append(node)
            visited[node] = 1

        # find next unvisited neighbor (iterate in reverse dict order so that
        # the first inserted neighbor is explored last, matching stack LIFO behavior)
        next_node = None
        for neighbor in reversed(list(graph_mst[node].keys())):
            if visited[neighbor] == 0:
                next_node = neighbor
                break

        if next_node is not None:
            stack.append(next_node)
        else:
            stack.pop()
            if stack: # record the backtrack
                two_mst_dfs.append(stack[-1])

    return two_mst_dfs

        
graph={0: {2: 16, 4: 1},
1: {3: 1, 4: 1},
2: {0: 16},
3: {1: 1},
4: {0: 1, 1: 1, 5:3},
5: {4:3}}

###########test code################
def test_dfs_2_mst():

    '''This is a naive way to test your dfs_2_mst function.
    If your result cannot pass this test, then propose a more
    sophisticated way to test your function and explain it
    in your report.
    '''
    
    res=[0, 4, 5, 4, 1, 3, 1, 4, 0, 2, 0]
    assert dfs_2_mst(graph, 0)==res
    
test_dfs_2_mst()

###########cycle construction################
def cycle_construct(list_two_mst):
    tsp_cycle=[]

    ###########complete the code################
    seen = set()
    for node in list_two_mst:
        if node not in seen:
            tsp_cycle.append(node)
            seen.add(node)
    tsp_cycle.append(tsp_cycle[0])  # close the cycle back to start

    return tsp_cycle

###########test code################
def test_cycle_construct():
    ex=[0, 4, 5, 4, 1, 3, 1, 4, 0, 2, 0]
    res=[0, 4, 5, 1, 3, 2, 0]
    assert cycle_construct(ex)==res

test_cycle_construct()

#####################total distance################

def total_distance(graph, cycle_list):
    
    '''calculate the total distance of all 
    neighboring vertices in cycle_list'''
    
    td=0

    ###########complete the code################
    for i in range(len(cycle_list) - 1):
        td += graph[cycle_list[i]][cycle_list[i+1]]

    return td

##################### Major algorithm ################
def tsp_algo(numVertices, weightRange):
    
    '''instrcutions:
    - create an object of the class Graph, which is a complete graph
    generated randomly with the number of vertices numVertices and
    the range of weight weightRange
    - calculate one mst by calling an algorithm in min_span_tree
    - call the functions in this file to calculate the result
    result: the total distance of cycle returned by the approximation 
    polynomial algorithm described in the project.
    '''
    
    ###########complete the code################
    # 1. Create a random complete undirected graph
    graph = Graph(numVertices=numVertices, weightRange=weightRange, directed=False)

    # 2. Compute the MST using Prim's algorithm
    mst = MST_Prim(graph)

    # 3. Convert MST (Graph object) to adjacency list dict
    mst_adl = transform_graph2adl(mst)

    # 4. DFS traversal that traverses each MST edge twice
    two_mst = dfs_2_mst(mst_adl, 0)

    # 5. Build the Hamiltonian cycle (keep first occurrences, close cycle)
    cycle = cycle_construct(two_mst)

    # 6. Compute total distance using the original complete graph's weights
    graph_adl = transform_graph2adl(graph)
    return total_distance(graph_adl, cycle)


def tsp_algo_with_trace(numVertices, weightRange, seed=None):
    """
    Same as tsp_algo but returns (graph, mst, two_mst, cycle, total_dist)
    for report. Set seed for reproducibility.
    """
    if seed is not None:
        random.seed(seed)

    graph = Graph(numVertices=numVertices, weightRange=weightRange, directed=False)
    mst = MST_Prim(graph)
    mst_adl = transform_graph2adl(mst)
    two_mst = dfs_2_mst(mst_adl, 0)
    cycle = cycle_construct(two_mst)
    graph_adl = transform_graph2adl(graph)
    total_dist = total_distance(graph_adl, cycle)

    return graph, mst, two_mst, cycle, total_dist


def run_example():
    """Run example with 6 vertices for report (reproducible with seed)."""
    graph, mst, two_mst, cycle, total_dist = tsp_algo_with_trace(6, 30, seed=42)

    print("TSP Algo Example (6 vertices, weightRange=30, seed=42) ===\n")

    print("1. Graph object (adjacency + weights):")
    print(graph)

    print("\n2. MST (minimum spanning tree):")
    print(mst)

    print("\n3. Two times of MST with DFS (list):")
    print("   ", two_mst)

    print("\n4. Corresponding cycle (first-occurrence + close):")
    print("   ", cycle)

    print("\n5. Final result (total distance):")
    print("   ", total_dist)


if __name__ == "__main__":
    run_example()
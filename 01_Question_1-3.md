## Question 1:
**You should formalize and model this problem by giving the inputs (the type of the graph) and the question.**

This model takes in input: 
- customer addresses
- battery of the drone 

The graph is a complete weighted undirected graph.
The question is: Is there a route starting from the warehouse, visiting all destinations exactly once, returning to the warehouse, whose total distance is ≤ B?

## Question 2:
**Now formalize the corresponding optimization version.**

Optimization Version

**Input**

- A **complete weighted graph** \( G = (V, E) \)
- A distinguished vertex \( s \in V \) representing the **warehouse**
- A weight function \( w : E \rightarrow \mathbb{R}_+ \) giving the distance between locations

**Question**

Find a **closed route** starting at \( s \), visiting every other vertex **exactly once**, and returning to \( s \), such that the **total distance is minimized**.

**Objective function**

\[
\min \sum_{i=0}^{n-1} w(v_i, v_{i+1})
\quad \text{with } v_n = v_0 = s
\]

where \( (v_0, v_1, \dots, v_{n-1}) \) is a **permutation of the vertices of \( V \)**.

## Question 3:

1. A minimal sapaning tree would be: 

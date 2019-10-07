# LeetCode(797. All Paths From Source to Target)题解

Given a directed, acyclic graph of `N` nodes.  Find all possible paths from node `0` to node `N-1`, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

```
Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

**Note:**

- The number of nodes in the graph will be in the range `[2, 15]`.
- You can print different paths in any order, but you should keep the order of nodes inside one path.

## 解题思路

给一个有向无环图，找出其中所有的源点到汇点的路径。

从原点出发，使用DFS，记录所有的路径即可，时间复杂度O(n)。

`Runtime: 196 ms, faster than 5.58% of Python3 online submissions for All Paths From Source to Target.`

`Memory Usage: 16.3 MB, less than 20.00% of Python3 online submissions for All Paths From Source to Target.`

```Python
class Solution(object):
    Path = []
    path = []
    Sta = 0
    End = -1
    G = []
    def findPath(self, node):
        if node == self.End:
            self.Path.append([i for i in self.path])
            return
        
        self.path.append("")
        for next_node in self.G[node]:
            self.path[-1] = next_node
            self.findPath(next_node)
        
        self.path = self.path[:-1]
        return
    
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.G = graph
        self.End = len(graph) - 1
      
        self.path = [self.Sta]
        self.findPath(self.Sta)
        import copy
        Paths = copy.deepcopy(self.Path)
        self.Path.clear()
        return Paths
```

BitBrave, 2019-10-07
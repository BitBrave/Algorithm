# LeetCode(802. Find Eventual Safe States)题解
------
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

    Example:
    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    Output: [2,4,5,6]
    Here is a diagram of the above graph.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png)

Note:

    graph will have length at most 10000.
    The number of edges in the graph will not exceed 32000.
    Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].

## 解题思路

在一个有向图中，如果从一个节点出发走过很多步之后到达了终点(出度为0的节点，无路可走了)，则认为这个节点是最终安全的节点。如果根本停不下来，那就是在一个环上，就是不安全节点。要在自然数K步内停止，到达安全节点，返回满足要求的排序好的所有安全节点的索引值。实质是在一个有向图中找出不在环路上的节点。

使用DFS，在遍历的过程中，可以这样想，一个节点要是走到了一个确定在环路上的节点，那么这个节点肯定无法达到最终状态，因此这个节点就可以判定为环路。同样，如果中途遍历的一个节点已经被判定为可以到达最终状态，那么就不需要后续判断了，直接返回这条路可达即可。

代码如下, 时间复杂度O(n), 空间复杂度O(n).

Runtime: 180 ms, faster than 53.05% of C++ online submissions for Find Eventual Safe States.
Memory Usage: 39.3 MB, less than 23.08% of C++ online submissions for Find Eventual Safe States.

```c++
class Solution {
    vector<vector<int>> G;
    vector<int> H; // 记录目前已经判定的节点,0表示还未判定，1表示可达停止态，2表示环路
public:
    bool isHoop(int i, int len){
        if(H[i] == 1) return false;
        if(H[i] == 2) return true;
        H[i] = 2;
        for(int k=0; k<len; k++){
            if(isHoop(G[i][k], G[G[i][k]].size())) return true;
        }
        H[i] = 1;
        return false;
    };
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        G = graph;
        int len = G.size();
        vector<int> res;
        H = vector<int>(len, 0);
        for(int i=0; i<len; i++){
            isHoop(i, G[i].size());
            if(H[i] == 1) res.push_back(i);
        }
        return res;
    }
};
```

BitBrave, 2019-08-29
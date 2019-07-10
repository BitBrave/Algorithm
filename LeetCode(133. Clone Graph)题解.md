# LeetCode(133. Clone Graph)题解
------
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Example:

![](https://assets.leetcode.com/uploads/2019/02/19/113_sample.png)

    Input:
    {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
    Node 1's value is 1, and it has two neighbors: Node 2 and 4.
    Node 2's value is 2, and it has two neighbors: Node 1 and 3.
    Node 3's value is 3, and it has two neighbors: Node 2 and 4.
    Node 4's value is 4, and it has two neighbors: Node 1 and 3.  

Note:

    The number of nodes will be between 1 and 100.
    The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
    Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
    You must return the copy of the given node as a reference to the cloned graph.

## 解题思路
给一个无向图，给出其copy版本，不能直接是原来的引用。

使用递归的办法，用Map记录当前节点是否已经遍历到，首先将当前节点为key，新建一个节点为Value，加入map，然后查看当前节点的邻居，如果在map遍历到，直接加入Value节点的邻居，如果没有遍历到，就进入下一层递归，返回之后将其加入Value节点的邻居。

代码如下：

Runtime: 20 ms, faster than 96.30% of C++ online submissions for Clone Graph.
Memory Usage: 16.9 MB, less than 11.74% of C++ online submissions for Clone Graph.

```C++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {}

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
    map<Node*, Node*> M;
    map<Node*, Node*>::iterator it_find;
public:
    Node* cloneGraph(Node* node) {
        if(node == NULL) return NULL;
        vector<Node*> &n = node->neighbors;
        int len = n.size();
        Node* cnode = new Node();
        cnode->val = node->val;
        M[node] = cnode;
        
        for(int i=0; i<len; i++){
            it_find = M.find(n[i]);
            if (it_find == M.end()) cloneGraph(n[i]);
            cnode->neighbors.push_back(M[n[i]]);
        }
        
        return cnode;
    }
};
```

BitBrave, 2019-07-10
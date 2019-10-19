# LeetCode(865. Smallest Subtree with all the Deepest Nodes)题解

Given a binary tree rooted at `root`, the *depth* of each node is the shortest distance to the root.

A node is *deepest* if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png)

```
Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
```

 

**Note:**

- The number of nodes in the tree will be between 1 and 500.
- The values of each node are unique.

## 解题思路

在二叉树中，节点的深度是节点离根节点的最短距离。现在给定一个二叉树，要求返回所有节点中深度最深的节点所在的最小子树。

这个题可以使用如下做法：首先是计算树的最大深度，花费O(n)，然后DFS遍历路径，记录达到最大深度的路径的节点的路径，时间O(n)，空间O(n)，但最终存储下来的是O(n2)。然后遍历这些路径，找出公共的节点，就是索引最靠后同时又在所有路径中都出现的节点，这就是最小子树的根节点，返回这个根节点即可。花费时间O(n)2。

因此，代码如下，时间复杂度O(n2)，空间复杂度O(n2)。

Runtime: 16 ms, faster than 9.05% of C++ online submissions for Smallest Subtree with all the Deepest Nodes.

Memory Usage: 21 MB, less than 7.14% of C++ online submissions for Smallest Subtree with all the Deepest Nodes.

```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    vector<vector<TreeNode*>> R;
    int deepest;
public:
    int dDFS(TreeNode* root){
        if(root == NULL) return 0;
        return max(dDFS(root->left), dDFS(root->right)) + 1;
    }
    void DFS(TreeNode* root, vector<TreeNode*> p){
        if(root == NULL){
            if(p.size() == deepest) R.push_back(p);
            return;
        }
        p.push_back(root);
        DFS(root->left, p);
        DFS(root->right, p);
        return;
    }
    
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        deepest = dDFS(root);
        DFS(root, vector<TreeNode*>());
        int len = R.size(), tl = R[0].size(), ret = 999;
        if(len == 2) return R[0][tl-1];
        
        for(int i=2; i<len; i+=2){
            for(int j=1; j<tl; j++){
                if(R[0][j] != R[i][j]) ret = min(ret, j-1);
            }
        }
        return R[0][ret];
    }
};
```

BitBrave，2019-10-18
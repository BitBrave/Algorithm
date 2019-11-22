# LeetCode(958. Check Completeness of a Binary Tree)题解

Given a binary tree, determine if it is a *complete binary tree*.

**Definition of a complete binary tree from Wikipedia:**
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png)**

```
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png)**

```
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
```

 

**Note:**

1. The tree will have between 1 and 100 nodes.

## 解题思路

给出一个二叉树，判断是不是完全二叉树（除了最后一层，每一层的二叉树节点是满的，最后一层的节点也是从左到右一次排列的）。

这个题可以使用BFS队列的方式做，也可以使用DFS的方式。因为考虑到空间复杂度的缘故，可以使用DFS。

设定一个Height函数，返回一个整数值，表示二叉树的最大深度，同时返回二叉树的类型type，如果是满二叉树就是0，完全二叉树就是1，否则就是-1。那么输入一个节点，返回以这个节点为根节点的二叉树的深度，至于Type的值，看左右子树的Type值，如果有一个-1或者两边的深度相差超过1就直接返回-1。否则就看深度，如果两边深度一样，那么左边必须是满二叉树，此时直接将右边的type值赋值给当前节点的type即可否则就是-1.如果右边深度少1，那么右子树必须是满二叉树，此时左边如果是满二叉树（Type=0）或者完全二叉树（Type=1），那么当前节点就是一个完全二叉树（Type=1），否则就返回-1.

代码如下，时间复杂度O(N)，空间复杂度O(1)。

`Runtime: 4 ms, faster than 88.77% of C++ online submissions for Check Completeness of a Binary Tree.`

`Memory Usage: 9.9 MB, less than 100.00% of C++ online submissions for Check Completeness of a Binary Tree.`

```c++
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
public:
    int Height(TreeNode* root, int &type){
        if(root == NULL){
            type = 0;
            return 0;
        }
        type = -1;
    
        int typel, typer;
        int l = Height(root->left, typel), r = Height(root->right, typer);
        if(l == r) type = (typel==0) ? typer : -1;
        else if(l == r + 1) type = (typer==0 and typel+1>0) ? 1 : -1;

        return 1 + max(l, r);
    }
    bool isCompleteTree(TreeNode* root) {
        int type;
        Height(root, type);
        return type != -1;
    }
};
```



BitBrave，2019-11-22
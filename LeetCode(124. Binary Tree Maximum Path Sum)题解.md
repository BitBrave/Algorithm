# LeetCode(124. Binary Tree Maximum Path Sum)题解
------
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

    Input: [1,2,3]

          1
         / \
        2   3

    Output: 6
Example 2:

    Input: [-10,9,20,null,null,15,7]

       -10
       / \
      9  20
        /  \
       15   7

    Output: 42

## 解题思路
给一个二叉树，从中找一条路径，其经过的节点之和最大。可以不经过根节点。最后返回对应的值。

这道题可以使用递归的办法，假设有一个函数，计算当前树的最大路径和。输入一个根节点，然后返回以这个根节点为起点的最大节点之和，和左子树中最大的路径之和。左边和右边子树最大和则可以通过递归函数完成，以根节点为起点的最大节点之和则可以通过左边和右边的子树根节点路径取最大即可。子树最大值之和可以用一个全局变量记录完成。

代码如下：

Runtime: 36 ms, faster than 55.38% of C++ online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 25.9 MB, less than 8.48% of C++ online submissions for Binary Tree Maximum Path Sum.

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
    int m = INT_MIN; // 目前记录的最大值
public:
    int maxPathSum_(TreeNode* root){
        if(root->left == NULL && root->right == NULL) {
            m = max(m, root->val);
            return root->val;
        };
        int l = 0, r = 0;
        if(root->left != NULL) l = maxPathSum_(root->left);
        if(root->right != NULL) r = maxPathSum_(root->right);
        if(root->left == NULL){
            m = max(m, max(root->val, root->val + r));
            return root->val + max(0, r);
        }
        else if(root->right == NULL){
            m = max(m, max(root->val, root->val + l));
            return root->val + max(0, l);
        }
        else{
            m = max(m, max(l, r));
            m = max(m, root->val + max(0, max(l+r, max(l, r))));
        }
        
        return root->val + max(0, max(l, r));
    }
    int maxPathSum(TreeNode* root) {
        if(root == NULL) return 0;
        maxPathSum_(root);
        
        return m;
    }
};
```

BitBrave, 2019-07-06




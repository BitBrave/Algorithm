# LeetCode(98. Validate Binary Search Tree)题解
------
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

    Example 1:

        2
       / \
      1   3

    Input: [2,1,3]
    Output: true
Example 2:

        5
       / \
      1   4
         / \
        3   6

    Input: [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

## 解题思路
给出1个二叉树，判断是不是一个二叉搜索树。

前向遍历下，二叉搜索树是一个递增序列，因此直接前向遍历树，如果发现数不是递增的就是错误的。

代码如下：

Runtime: 16 ms, faster than 87.95% of C++ online submissions for Validate Binary Search Tree.
Memory Usage: 20.9 MB, less than 19.46% of C++ online submissions for Validate Binary Search Tree.

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
    bool fowardT(TreeNode* root, double &last, bool &l){
        if(root == NULL) return true;
        if(!fowardT(root->left, last, l)) return false;
        if(root->val <= last && !l) return false;
        l = false;
        last = root->val;
        return fowardT(root->right, last, l);
    }
    bool isValidBST(TreeNode* root) {
        double last = INT_MIN;
        bool l = true;
        return fowardT(root, last, l);
    }
};
```

BitBrave，2019-06-13
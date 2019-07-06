# LeetCode(129. Sum Root to Leaf Numbers)题解
------
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

    Input: [1,2,3]
        1
       / \
      2   3
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.
Example 2:

    Input: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.


## 解题思路
给一个二叉树，每个节点的值为0-9，每个根节点到孩子节点的值组合起来是一个数。求出所有路径上的值的和。

这个题简单的分叉递归就可以了。每次当前再每次向下走的时候都意味着当前数字向左移一位，直接*10即可。

代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Sum Root to Leaf Numbers.
Memory Usage: 12.3 MB, less than 73.12% of C++ online submissions for Sum Root to Leaf Numbers.

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
    int sumNumbers_(TreeNode* root, int res){
        if(root->left == NULL && root->right == NULL) return res * 10 + root->val;
        int R = 0;
        if(root->right != NULL) R = sumNumbers_(root->right, res * 10 + root->val);
        if(root->left != NULL) R += sumNumbers_(root->left, res * 10 + root->val);
        return R;
    }
    int sumNumbers(TreeNode* root) {
        if(root == NULL) return 0;
        int res = 0;
        res = sumNumbers_(root, res);
        return res;
    }
};
```

BitBrave, 2019-07-06
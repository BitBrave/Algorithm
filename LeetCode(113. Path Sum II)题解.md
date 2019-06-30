# LeetCode(113. Path Sum II)题解
------
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

    Given the below binary tree and sum = 22,

           5
          / \
         4   8
        /   / \
       11  13  4
      /  \    / \
     7    2  5   1
Return:

    [
        [5,4,11,2],
        [5,8,4,5]
    ]

## 解题思路
给一个二叉树，和一个值，从二叉树中找出所有从根节点出发向下走到叶子节点的路径，其节点之和为给定的值。

可以使用递归的方法，使用vector记录一个路径，走到当前节点，看是否当前节点加上之前的和为给定的值。如果等于则存储，如果大于就放弃这条路，如果小于则加入，再继续向下走。

代码如下：

Runtime: 24 ms, faster than 39.82% of C++ online submissions for Path Sum II.
Memory Usage: 38.2 MB, less than 12.98% of C++ online submissions for Path Sum II.

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
    vector<vector<int>> res;
public:
    void pathSum_(TreeNode* root, int sum, vector<int> tmp, int lsum){
        if(root == NULL) return;
        tmp.push_back(root->val);
        lsum += root->val;
        if(lsum == sum && root->left == NULL && root->right == NULL){
            res.push_back(tmp);
            return;
        }
        pathSum_(root->left, sum, tmp, lsum);
        pathSum_(root->right, sum, tmp, lsum);
        return;
    }
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> tmp;
        int lsum = 0;
        pathSum_(root, sum, tmp, lsum);
        return res;
    } 
};
```

BitBrave, 2019-06-30
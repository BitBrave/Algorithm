# LeetCode(144. Binary Tree Preorder Traversal)题解
------

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

    Input: [1,null,2,3]
       1
        \
         2
        /
       3

    Output: [1,2,3]
    Follow up: Recursive solution is trivial, could you do it iteratively?


## 解题思路
前序遍历一棵树，存储数据的信息到vector中。

简单，很容易直接递归完事儿了。

代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Preorder Traversal.
Memory Usage: 9.3 MB, less than 40.98% of C++ online submissions for Binary Tree Preorder Traversal.

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
    vector<int> res;
    void preorderTraversal_(TreeNode* root){
        if(root == NULL) return;
        res.push_back(root->val);
        preorderTraversal_(root->left);
        preorderTraversal_(root->right);
        return;
    }
    vector<int> preorderTraversal(TreeNode* root) {
        preorderTraversal_(root);
        return res;
    }
};
```

当然，可以使用迭代的方式（使用栈），符合题意。

代码如下

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Preorder Traversal.
Memory Usage: 9.1 MB, less than 65.89% of C++ online submissions for Binary Tree Preorder Traversal.

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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root == NULL) return res;
        stack<TreeNode*> S;
        S.push(root);
        while(!S.empty()){
            root = S.top(); S.pop();
            res.push_back(root->val);
            if(root->right != NULL) S.push(root->right);
            if(root->left != NULL) S.push(root->left);
        }
        return res;
    }
};
```

BitBrave, 2019-07-11
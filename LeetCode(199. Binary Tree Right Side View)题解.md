# LeetCode(199. Binary Tree Right Side View)题解
------
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

    Input: [1,2,3,null,5,null,4]
    Output: [1, 3, 4]
Explanation:

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---

## 解题思路
给一个二叉树，返回最右边的元素。

可以使用BFS，每次遍历一层的元素，每次将最后一个元素记录下来即可。

代码如下：

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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(root == NULL) return res;
        
        queue<TreeNode*> Q;
        Q.push(root);
        while(!Q.empty()){
            int c = Q.size();
            while(c-- > 1){
                root = Q.front(); Q.pop();
                if(root->left != NULL) Q.push(root->left);
                if(root->right != NULL) Q.push(root->right);
            }
            root = Q.front(); Q.pop();
            if(root->left != NULL) Q.push(root->left);
            if(root->right != NULL) Q.push(root->right);
            res.push_back(root->val);
        }
        return res;
    }
};
```

BitBrave, 2019-07-24
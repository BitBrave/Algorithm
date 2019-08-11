# LeetCode(145. Binary Tree Postorder Traversal)题解
------
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

 Input: [1,null,2,3]
       1
        \
         2
        /
       3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?


## 解题思路
后续遍历一棵树，建议使用迭代的方式，而不是简单的递归。

这个题首先肯定是可以使用递归的。
代码如下

Runtime: 4 ms, faster than 61.32% of C++ online submissions for Binary Tree Postorder Traversal.
Memory Usage: 9.4 MB, less than 35.48% of C++ online submissions for Binary Tree Postorder Traversal.

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
    vector<int> res;
public:
    void postorderTraversal_(TreeNode* root){
        if(root == NULL) return;
        postorderTraversal_(root->left);
        postorderTraversal_(root->right);
        res.push_back(root->val);
        return;
    }
    vector<int> postorderTraversal(TreeNode* root) {
        postorderTraversal_(root);
        return res;
    }
};
```

而如果要迭代地做应该如何呢？可以使用stack，每次从左一直遍历向下，不断压栈，直到NULL，然后开始查看栈顶元素，如栈顶元素没有左右节点，就出栈，将出栈的放入res（结果数组），否则将左节点，右节点继续入栈，这里需要一个方式判别当前节点的孩子节点是否已经遍历过了。这里使用map，如果已经遍历过，就不再入栈了。

代码如下

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Postorder Traversal.
Memory Usage: 9.3 MB, less than 74.19% of C++ online submissions for Binary Tree Postorder Traversal.

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root == NULL) return res;
        stack<TreeNode*> S;
        map<TreeNode*, bool> M;
        M[NULL] = true;
        S.push(root);
        
        while(!S.empty()){
            if(M.find(S.top()->left) == M.end()){
                S.push(S.top()->left);
                continue;
            }
            if(M.find(S.top()->right) == M.end()){
                S.push(S.top()->right);
                continue;
            }
            res.push_back(S.top()->val);
            M[S.top()] = true;
            S.pop();
        }
        return res;
    }
};
```

BitBrave, 2019-08-11
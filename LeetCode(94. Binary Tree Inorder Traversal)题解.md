# LeetCode(94. Binary Tree Inorder Traversal)题解
------

## 解题思路
使用中序遍历法遍历一棵树。先左子树，再根节点，再右子树。

使用递归的代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Inorder Traversal.
Memory Usage: 9.2 MB, less than 54.89% of C++ online submissions for Binary Tree Inorder Traversal.

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
    void inorderTraversal_(TreeNode* root, vector<int> &res){
        if(root==NULL) return;
        
        inorderTraversal_(root->left, res);
        res.push_back(root->val);
        inorderTraversal_(root->right, res);
        return;
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorderTraversal_(root, res);
        return res;
    }
};
```

递归的办法很简单，但是有没有一种不使用递归，而是迭代的方法去得到中序遍历呢。

可以使用栈的方式：

a. 遇到一个节点，访问它，然后把它压栈，并去遍历它的左子树；

b. 当左子树遍历结束后，打印节点值，从栈顶弹出该节点并将其指向右儿子，继续a步骤；

c. 当所有节点访问完即最后访问的树节点为空且栈空时，停止。

非递归代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Inorder Traversal.
Memory Usage: 9.1 MB, less than 67.08% of C++ online submissions for Binary Tree Inorder Traversal.

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> S;
        while(root != NULL || !S.empty()){
            while(root != NULL){
                S.push(root);
                root = root->left;
            }
            if(!S.empty()){
                res.push_back(S.top()->val);
                root = S.top()->right;
                S.pop();
            }
        }
        return res;
    }
};
```
BitBrave, 2019-06-23
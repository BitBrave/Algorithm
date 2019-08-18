# LeetCode(236. Lowest Common Ancestor of a Binary Tree)题解
------
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    

Note:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.


## 解题思路
找出一个二叉树中两个节点的最低公共祖先节点。

可以首先建立一个链表，两次遍历整个二叉树，找到对应的节点的路径。然后从头到尾遍历两个链表，遇到分叉口就是最低祖先节点。时间复杂度O(n), 空间复杂度O(n).

代码如下：

Runtime: 20 ms, faster than 72.17% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 18.3 MB, less than 20.00% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.

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
    struct Node {
        TreeNode *root;
        Node *next;
        Node(TreeNode *t, Node *n) : root(t), next(n) {}
    };
    Node* findPath(TreeNode* root, TreeNode* r){
        if(root == NULL) return NULL;
        if(root->val == r->val) return new Node(root, NULL);
        Node *tail;
        tail = findPath(root->left, r);
        if(tail == NULL) tail = findPath(root->right, r);
        if(tail == NULL) return NULL;
        return new Node(root, tail);
    };
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        Node *phead = findPath(root, p), *qhead = findPath(root, q);
        TreeNode *last = NULL;
        
        while(phead != NULL && qhead != NULL && phead->root == qhead->root){
            last = phead->root;
            phead = phead->next;
            qhead = qhead->next;
        }
        return last;
    };
};
```

BitBrave, 2019-08-18
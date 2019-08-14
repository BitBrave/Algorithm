# LeetCode(701. Insert into a Binary Search Tree)题解
------
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

    Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

    Given the tree:
            4
           / \
          2   7
         / \
        1   3
And the value to insert: 5
You can return this binary search tree:

             4
           /   \
          2     7
         / \   /
        1   3 5
This tree is also valid:

             5
           /   \
          2     7
         / \   
        1   3
             \
             4

## 解题思路

给一个二叉搜索树，插入一个值。

可以使用递归的办法，从根节点开始，判断根节点和要插入之的大小，如果大于就相当于将该值插入右子树，数据规模减半，反之插入左子树，如果右子树或者左子树为空，就直接插入。

代码如下

Runtime: 80 ms, faster than 94.67% of C++ online submissions for Insert into a Binary Search Tree.
Memory Usage: 32.9 MB, less than 75.00% of C++ online submissions for Insert into a Binary Search Tree.

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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(val > root->val){
            if(root->right == NULL)
                root->right = new TreeNode(val);
            else insertIntoBST(root->right, val);
        }
        else{
            if(root->left == NULL)
                root->left = new TreeNode(val);
            else insertIntoBST(root->left, val);
        }
        
        return root;
    }
};
```

BitBrave, 2019-08-15
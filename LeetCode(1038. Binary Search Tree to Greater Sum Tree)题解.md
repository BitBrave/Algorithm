# LeetCode(\1038. Binary Search Tree to Greater Sum Tree)题解

Given the root of a binary **search** tree with distinct values, modify it so that every `node` has a new value equal to the sum of the values of the original tree that are greater than or equal to `node.val`.

As a reminder, a *binary search tree* is a tree that satisfies these constraints:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

 

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/05/02/tree.png)**

```
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```

 

**Note:**

1. The number of nodes in the tree is between `1` and `100`.
2. Each node will have value between `0` and `100`.
3. The given tree is a binary search tree.

## 解题思路

给一个BST（二叉搜索树），其中每个节点的值都不一样，现在对每个值进行改变，将每个节点的值改为原本二叉树中大于等于这个节点值的节点的值的和。（理解了好久才明白这个题意！）

这个题说白了就是，找到一个节点，然后统计BST中大于等于这个节点值的所有节点，把这些节点的值加起来更新为这个节点的值。而BST在中序遍历上就是一个递增的序列。因此我们可以使用一个倒着的中序遍历，然后把前面的值分别求和加到后面的值上即可。

代码如下，时间复杂度O(N)，空间复杂度O(1)。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Search Tree to Greater Sum Tree.`

`Memory Usage: 9.1 MB, less than 100.00% of C++ online submissions for Binary Search Tree to Greater Sum Tree.`

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
public:
    int inOrder(TreeNode* root, int val){
        if(root == NULL) return 0;
        int tmp = root->val, r = inOrder(root->right, val);
        root->val += r + val;
        return tmp + r + inOrder(root->left, root->val);
    }
    TreeNode* bstToGst(TreeNode* root) {
        inOrder(root, 0);
        return root;
    }
};
```

BitBrave，2019-11-22
# LeetCode(951. Flip Equivalent Binary Trees)题解

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is *flip equivalent* to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are *flip equivalent*.  The trees are given by root nodes `root1` and `root2`.

 

**Example 1:**

```
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
```

 ![](https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png)

**Note:**

1. Each tree will have at most `100` nodes.
2. Each value in each tree will be a unique integer in the range `[0, 99]`.

## 解题思路

给出两个二叉树，每个二叉树内，各个节点的值都是不一样的。现在有一种操作，选定一个节点，将节点的左右子树进行交换。问，对一些节点进行交换，是否可以将两个二叉树变成一样的（一样的结构和值）？

这个题是个很明显的递归问题。假设函数就是返回两个二叉树是否可以变成相同的。

- 首先看看两个根节点是否为空，如果都为空返回True，有一个为空返回Flase。都不为空进行下一步。
- 查看根节点的值是否一样，不一样就返回False，否则进行下一步。
- 将两个节点的左子树根节点作为参数同样运行这个函数，再将右子树根节点一起作为参数放入函数。查看返回结果，如果都是True，则返回True。否则就将一个节点的左子树和另一个节点右子树根节点一起，分别放入函数，看返回值，如果都为True，返回True，否则False。

代码如下，时间复杂度O(N)，空间复杂度O(1)。这里有可能会让人觉得函数在运行的时候，搜寻子树明明进行了四次调用，时间复杂度肯定高，但是可以观察到，如果到达下一层的时候，两个数值不一样，就直接返回，不会继续递归，因此函数是线性往下走的。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Flip Equivalent Binary Trees.`

`Memory Usage: 11.6 MB, less than 100.00% of C++ online submissions for Flip Equivalent Binary Trees.`

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
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if(root1 == NULL || root2 == NULL) return root1 == NULL and root2 == NULL;
        if(root1->val != root2->val) return false;
        return flipEquiv(root1->left, root2->left) and flipEquiv(root1->right, root2->right) or flipEquiv(root1->right, root2->left) and flipEquiv(root1->left, root2->right);
    }
};
```



BitBrave， 2019-11-21
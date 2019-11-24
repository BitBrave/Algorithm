# LeetCode(\1008. Construct Binary Search Tree from Preorder Traversal)题解

Return the root node of a binary **search** tree that matches the given `preorder` traversal.

*(Recall that a binary search tree is a binary tree where for every node, any descendant of `node.left` has a value `<` `node.val`, and any descendant of `node.right` has a value `>` `node.val`. Also recall that a preorder traversal displays the value of the `node` first, then traverses `node.left`, then traverses `node.right`.)*

 

**Example 1:**

```
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
```

 ![](https://assets.leetcode.com/uploads/2019/03/06/1266.png)

**Note:** 

1. `1 <= preorder.length <= 100`
2. The values of `preorder` are distinct.

## 解题思路

给一个BST的前序遍历结果的数组，元素都不相同，给出其二叉树结构。

分析给出的数组，第一个元素一定是二叉树的根节点，而左子树的节点值肯定都小于根节点值，右子树都大于根节点值。因此我们可以直接将数组中比第一个元素小的值都作为左子树，其余都是右子树节点。

一个简单的递归算法就可以了。

代码如下，时间复杂度O(n2)，空间复杂度O(1)。

`Runtime: 8 ms, faster than 33.01% of C++ online submissions for Construct Binary Search Tree from Preorder Traversal.`

`Memory Usage: 12 MB, less than 9.52% of C++ online submissions for Construct Binary Search Tree from Preorder Traversal.`

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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        return bstFromPreorder_(preorder, 0, preorder.size()-1);
    }
    TreeNode* bstFromPreorder_(vector<int>& A, int sta, int end){
        if(sta > end) return NULL; 
        if(sta == end) new TreeNode(A[sta]);
        int mid = sta + 1;
        while(mid <= end && A[mid] < A[sta]) mid++;
        TreeNode *root = new TreeNode(A[sta]);
        root->left = bstFromPreorder_(A, sta+1, mid-1);
        root->right = bstFromPreorder_(A, mid, end);
        return root;
    }
};
```



BitBrave，2019-11-24
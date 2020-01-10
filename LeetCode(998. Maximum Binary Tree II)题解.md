# LeetCode(\998. Maximum Binary Tree II)题解

We are given the `root` node of a *maximum tree:* a tree where every node has a value greater than any other value in its subtree.

Just as in the [previous problem](https://leetcode.com/problems/maximum-binary-tree/), the given tree was constructed from an list `A` (`root = Construct(A)`) recursively with the following `Construct(A)` routine:

- If `A` is empty, return `null`.
- Otherwise, let `A[i]` be the largest element of `A`. Create a `root` node with value `A[i]`.
- The left child of `root` will be `Construct([A[0], A[1], ..., A[i-1]])`
- The right child of `root` will be `Construct([A[i+1], A[i+2], ..., A[A.length - 1]])`
- Return `root`.

Note that we were not given A directly, only a root node `root = Construct(A)`.

Suppose `B` is a copy of `A` with the value `val` appended to it. It is guaranteed that `B` has unique values.

Return `Construct(B)`.

 

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-1.png)![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-2.png)**

```
Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A = [1,4,2,3], B = [1,4,2,3,5]
```

**Example 2:
![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-1.png)![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-2.png)**

```
Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: A = [2,1,5,4], B = [2,1,5,4,3]
```

**Example 3:
![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-1.png)![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-2.png)**

```
Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: A = [2,1,5,3], B = [2,1,5,3,4]
```

 

**Note:**

1. `1 <= B.length <= 100`

## 解题思路

与上一个题[最大二叉树构建](https://leetcode.com/problems/maximum-binary-tree/)相联系，给出一个A数组构建好的二叉树的根节点，和一个数K。然后B数组等于在A数组后加一个数K，返回一个通过B数组构建的二叉树的根节点。K和A数组内所有元素都不一样。

这个题其实很简单，使用递归即可解决。首先A数组和B数组构建的二叉树只有一个元素不一样，而在原始数组中K是放在最后面的，所以其肯定在二叉树的右边部分。

做法如下，判断K和当前节点的值大小，如果比当前节点大，那么就以K为值建立节点，节点的子树就是当前节点的树，然后返回和这个K值节点。如果小或者当前节点为NULL，那么就表示K值节点在右子树内，就递归调用节点的右子节点和这个数K的函数，然后返回值用作当前节点的右子节点。

代码如下，时间复杂度为二叉树的深度，一般为O(logn)，最差为O(n)。空间复杂度O(1).

`Runtime: 4 ms, faster than 88.16% of C++ online submissions for Maximum Binary Tree II.`

`Memory Usage: 11.1 MB, less than 100.00% of C++ online submissions for Maximum Binary Tree II.`

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
    TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
        if (root == NULL or val > root->val) {
            TreeNode *node = new TreeNode(val);
            node->left = root;
            return node;
        }
        root->right = insertIntoMaxTree(root->right, val);
        return root;
    }
};
```

BitBrave, 2020-01-10
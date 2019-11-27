# LeetCode(654. Maximum Binary Tree)题解

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1. The root is the maximum number in the array.
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.



Construct the maximum tree by the given array and output the root node of this tree.

**Example 1:**

```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```



**Note:**

1. The size of the given array will be in the range [1,1000].

## 解题思路

给出一个数组，构建一个最大值数组，即任意一个子树包括整个树，根节点的值都比其余节点的值要大。构建的方法就是首先选择数组中最大的值作为根节点，最大值左边的值放入左子树，右边的值放入右子树。

因此根据上述方法可以直接构建。代码如下，时间复杂度O(n2)，空间复杂度O(1)。

`Runtime: 72 ms, faster than 63.36% of C++ online submissions for Maximum Binary Tree.`

`Memory Usage: 28.5 MB, less than 86.11% of C++ online submissions for Maximum Binary Tree.`

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
    TreeNode* constructMaximumBinaryTree_(vector<int>& A, int sta, int end){
        if(sta > end) return NULL;
        int m = sta;
        for(int i=sta+1; i<=end; i++){
            if(A[m] < A[i]) m = i;
        }
        TreeNode* root = new TreeNode(A[m]);
        root->left = constructMaximumBinaryTree_(A, sta, m-1);
        root->right = constructMaximumBinaryTree_(A, m+1, end);
        return root;
    }
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return constructMaximumBinaryTree_(nums, 0, nums.size()-1);
    }
};
```

BitBrave， 2019-11-27
# LeetCode(337. House Robber III)题解
------
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

    Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

    Output: 7 
    Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

    Input: [3,4,5,1,3,null,1]

         3
        / \
       4   5
      / \   \ 
     1   3   1

    Output: 9
    Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

## 解题思路
给出一个二叉树，找出其中不相邻节点的值的最大和。

跟数组抢劫一样，使用DP即可。对于一个节点来说，如果当前节点计入，那么孩子节点就不能计入，而计算以孙子节点为根节点的树。反之若当前节点不计入，则计算以儿子节点为根节点的数，这二者取最大值即可。

最朴素的代码如下：

Runtime: 1852 ms, faster than 5.02% of C++ online submissions for House Robber III.
Memory Usage: 20.8 MB, less than 83.33% of C++ online submissions for House Robber III.

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
    int rob(TreeNode* root) {
        if(root == NULL) return 0;
        if(root->right == NULL && root->left == NULL) return root->val;
        
        if(root->left == NULL) 
            return max(root->val+rob(root->right->left)+rob(root->right->right), rob(root->right));
        if(root->right == NULL) 
            return max(root->val+rob(root->left->left)+rob(root->left->right), rob(root->left));
        return max(root->val+rob(root->left->left)+rob(root->left->right)+rob(root->right->left)+rob(root->right->right), rob(root->left)+rob(root->right));
    }
};
```

可以看到非常地耗时，这是因为计算一个节点的时候，需要不断计算孩子孙子节点，而做了大量无用功。可以用一个map记录下来算过的值，这样可以大大减少时间。

代码如下：

Runtime: 24 ms, faster than 46.56% of C++ online submissions for House Robber III.
Memory Usage: 24 MB, less than 16.67% of C++ online submissions for House Robber III.

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
    map<TreeNode*, int> M;
public:
    int rob(TreeNode* root) {
        if(root == NULL) return 0;
        if(M.find(root) != M.end()) return M[root];
        if(root->right == NULL && root->left == NULL){
            M[root] = root->val;
            return M[root];
        }
        
        if(root->left == NULL){
            M[root] = max(root->val+rob(root->right->left)+rob(root->right->right), rob(root->right));
            return M[root];
        }
            
        if(root->right == NULL){
            M[root] = max(root->val+rob(root->left->left)+rob(root->left->right), rob(root->left));
            return M[root]; 
        }
        M[root] = max(root->val+rob(root->left->left)+rob(root->left->right)+rob(root->right->left)+rob(root->right->right), rob(root->left)+rob(root->right));
        return M[root];
    }
};
```

BitBrave, 2019-08-8
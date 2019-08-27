# LeetCode(814. Binary Tree Pruning)题解
------
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

    Example 1:
    Input: [1,null,0,0,1]
    Output: [1,null,0,null,1]
    
    Explanation: 
    Only the red nodes satisfy the property "every subtree not containing a 1".
    The diagram on the right represents the answer.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)

    Example 2:
    Input: [1,0,1,0,0,0,1]
    Output: [1,null,1,null,1]

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)

    Example 3:
    Input: [1,1,0,1,1,0,1,0]
    Output: [1,1,0,1,1,null,1]

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)

Note:

    The binary tree will have at most 100 nodes.
    The value of each node will only be 0 or 1.

## 解题思路
除去二叉树中所有元素为0的子树。

这个使用遍历的办法可以达到，使用Map遍历遇到的节点，记录该节点及其子树是否全部为0组成，如果全部为0，那么久表示这颗树需要删除，否则就不用删除。

代码如下，时间复杂度O(n), 空间复杂度O(n):

Runtime: 8 ms, faster than 5.19% of C++ online submissions for Binary Tree Pruning.
Memory Usage: 11.1 MB, less than 7.14% of C++ online submissions for Binary Tree Pruning.

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
    map<TreeNode*, bool> M;
public:
    bool isAll0(TreeNode* root){
        if(M.find(root) != M.end()) return M[root];
        bool l = isAll0(root->left), r = isAll0(root->right);
        if(l && r){
            M[root] = true && root->val == 0;
            root->left = NULL;
            root->right = NULL;
            return M[root];
        }
        if(l) root->left = NULL;
        if(r) root->right = NULL;
        M[root] = false;
        return false;
    }
    TreeNode* pruneTree(TreeNode* root) {
        M[NULL] = true;
        isAll0(root);
        return root;
    }
};
```

BitBrave, 2019-08-27
# LeetCode(894. All Possible Full Binary Trees) 题解

A *full binary tree* is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with `N` nodes.  Each element of the answer is the root node of one possible tree.

Each `node` of each tree in the answer **must** have `node.val = 0`.

You may return the final list of trees in any order.

 

**Example 1:**

```
Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:
```

 ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png)

**Note:**

- `1 <= N <= 20`

##  解题思路

输入一个数，输出对应节点数的完全二叉树（由度只有0和2的节点组成的二叉树）。

设二叉树节点叶子节点数为a，则内部节点为a-1。有2*a-1=N。因此完全二叉树的左右子树也一定是一个完全二叉树，其节点数也一定是奇数。

知道了这个性质，就可以依次左边放置奇数个节点，右边放置奇数个节点，遍历所有的情况即可。

代码如下，时间复杂度O(n)=2 \* (O(1)+O(3)+O(i)+O(N-4)+O(N-2))+O(1) \* O(N-2)+O(3) \* O(N-4)+...+O(N-2) \* O(1)，O(1) = 1. 空间复杂度就是多个二叉树的存储。

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
    vector<TreeNode*> allPossibleFBT(int N) {
        if(N == 1) return vector<TreeNode*>({new TreeNode(0)});
        vector<TreeNode*> res;
        if(N & 1 == 0) return res;
        
        for(int i=1; i<=N-2; i+=2){
            vector<TreeNode*> left = allPossibleFBT(i), right = allPossibleFBT(N-i-1);
            for(TreeNode* l : left){
                for(TreeNode* r : right){
                    TreeNode* root = new TreeNode(0);
                    root->left = l;
                    root->right = r;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
};
```

BitBrave，2019-09-29
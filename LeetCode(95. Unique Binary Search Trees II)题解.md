# LeetCode(95. Unique Binary Search Trees II)题解
------
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

    Input: 3
    Output:
    [
    [1,null,3,2],
    [3,2,null,1],
    [3,1,null,null,2],
    [2,1,3],
    [1,null,2,null,3]
    ]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

        1         3     3      2      1
        \       /     /      / \      \
        3     2     1      1   3      2
        /     /       \                 \
        2     1         2                 3

## 题意理解
给定数N，生成所有的合适的BST树。

如何生成树呢？可以使用类似于DP的方法。当生成以i为根节点的树的时候，左边为1~i-1，右边为i+1~n，则左边可以生成一个向量组包括1~i-1的BST树，右边生成一个向量组包括i+1~n的向量组。要组成1~n的向量组。可以将左边取出一个来，右边取出一个来，然后加入i作为根节点即可。

代码如下

Runtime: 12 ms, faster than 99.00% of C++ online submissions for Unique Binary Search Trees II.
Memory Usage: 17.1 MB, less than 46.89% of C++ online submissions for Unique Binary Search Trees II.

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
    vector<TreeNode*> generateTrees_(int n1, int n2){
        vector<TreeNode*> res;
        if(n1==n2){
            res.push_back(new TreeNode(n1));
            return res;
        };
        if(n1>n2){
            res.push_back(NULL);
            return res;         
        }
        
        vector<TreeNode*> left, right;
        int llen, rlen;
        for(int i=n1-1; i<n2; i++){
            left = generateTrees_(n1, i); 
            right = generateTrees_(i+2, n2);
            llen = left.size(); 
            rlen = right.size();
            
            for(int a=0; a<llen; a++){
                for(int b=0; b<rlen; b++){
                    TreeNode* root = new TreeNode(i+1);
                    root->left = left[a];
                    root->right = right[b];
                    res.push_back(root);
                }
            }
        }
        return res;
    }
    vector<TreeNode*> generateTrees(int n) {
        if(n==0) return vector<TreeNode*>();
        return generateTrees_(1, n);
    }
};
```

BitBrave, 2019-06-23

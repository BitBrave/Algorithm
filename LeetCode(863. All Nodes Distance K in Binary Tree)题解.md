# LeetCode(863. All Nodes Distance K in Binary Tree)题解

We are given a binary tree (with root node `root`), a `target` node, and an integer value `K`.

Return a list of the values of all nodes that have a distance `K` from the `target` node.  The answer can be returned in any order.

 ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
```

 

**Note:**

1. The given tree is non-empty.
2. Each node in the tree has unique values `0 <= node.val <= 500`.
3. The `target` node is a node in the tree.
4. `0 <= K <= 1000`.

## 解题思路

给定一个二叉树和二叉树中的一个节点，找出树中离这个节点K距离的所有点。

这个题可以使用递归解决。

首先使用一个递归函数，输入根节点，目标节点，使用DFS寻找到根节点与目标节点的路径。得到路径之后，使用一个新的递归函数，输入一个节点，寻找以这个节点为根节点的情况下离根节点距离为L的节点，可以使用BFS。这时候，可以输入目标节点，长度K，或者目标节点的父节点的另一个孩子节点，长度K-2，爷爷节点的另一个孩子节点，长度N-3，····以此类推即可。

代码如下，时间复杂度O(n)，空间复杂度O(n)。

`Runtime: 8 ms, faster than 70.58% of C++ online submissions for All Nodes Distance K in Binary Tree.`

`Memory Usage: 15 MB, less than 100.00% of C++ online submissions for All Nodes Distance K in Binary Tree.`

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
    vector<TreeNode *> path;
    vector<int> res;
public:
    bool findPath(TreeNode* root, TreeNode* target){
        if(root == NULL) return false;
        path.push_back(root);
        
        if(root == target) return true;        
        
        if(findPath(root->left, target)) return true;
        else if(findPath(root->right, target)) return true;
        
        path.pop_back();
        return false;
    }
    void findK(TreeNode* root, int K){
        if(root == NULL or K < 0) return;
        if(K == 0){
            res.push_back(root->val);
            return;
        }
        
        findK(root->left, K-1);
        findK(root->right, K-1);
        return;
    } 
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        findPath(root, target);
        int len = path.size();
        
        if(len-K-1 >= 0) res.push_back(path[len-K-1]->val);
        for(int i=len-K; i<len-1; i++){
            if(i < 0) continue;
            
            if(path[i+1] == path[i]->left) findK(path[i]->right, K-len+i);
            else findK(path[i]->left, K-len+i);
        }
        
        if(K != 0)findK(path[len-1], K);
        return res;
    }
};
```

BitBrave，2019-10-10
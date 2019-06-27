# LeetCode(102. Binary Tree Level Order Traversal)题解
------
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
         3
        / \
       9  20
         /  \
        15   7
return its level order traversal as:

    [
    [3],
    [9,20],
    [15,7]
    ]

## 解题思路
实现二叉树的层序遍历。

用一个queue存储遍历的节点，用一个数count记录每一层入队列的数目。首先根节点入队列，count+1，然后以count为准进行循环出队列，每次出队列的时候，要把出队列的节点的孩子节点入队列。最后count为0时表示这一层数目全部出来了。然后再count更新为队列的size，表示下一层的数目。

代码如下：

Runtime: 8 ms, faster than 79.92% of C++ online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.9 MB, less than 58.24% of C++ online submissions for Binary Tree Level Order Traversal.

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> Q;
        int count;
        
        if(root != NULL) Q.push(root);
        while(!Q.empty()){
            count = Q.size();
            TreeNode* tmp;
            vector<int> item;
            while(count>0){
                count--;
                tmp = Q.front(); Q.pop();
                item.push_back(tmp->val);
                if(tmp->left != NULL) Q.push(tmp->left);
                if(tmp->right != NULL) Q.push(tmp->right);
            }
            res.push_back(item);
        }
        return res;
    }
};
```

BitBrave, 2019-06-27

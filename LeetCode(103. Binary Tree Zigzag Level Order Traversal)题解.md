# LeetCode(103. Binary Tree Zigzag Level Order Traversal)题解
------
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
         3
        / \
       9  20
         /  \
        15   7

return its zigzag level order traversal as:

    [
        [3],
        [20,9],
        [15,7]
    ]


## 解题思路
实现二叉树的层序遍历,同时要是曲折的，就是这一层从左到右，下一层从右到左，再从左到右····。

很简单，用一个queue存储遍历的节点，用一个数count记录每一层入队列的数目，同时用一个bool变量dir记录方向，true从左到右，false从右到左。首先根节点入队列，count+1，然后以count为准进行循环出队列，每次出队列的时候，要把出队列的节点的孩子节点入队列。最后count为0时表示这一层数目全部出来了，这一层用一个vector记录，如果dir为false，就将vector反转（reverse函数）。然后再count更新为队列的size，表示下一层的数目。

代码如下：

Runtime: 4 ms, faster than 93.83% of C++ online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 13.5 MB, less than 56.33% of C++ online submissions for Binary Tree Zigzag Level Order Traversal.

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> Q;
        int count;
        bool dir = false;
        
        if(root != NULL) Q.push(root);
        while(!Q.empty()){
            count = Q.size();
            dir = !dir;
            TreeNode* tmp;
            vector<int> item;
            while(count>0){
                count--;
                tmp = Q.front(); Q.pop();
                item.push_back(tmp->val);
                if(tmp->left != NULL) Q.push(tmp->left);
                if(tmp->right != NULL) Q.push(tmp->right);
            }
            if(!dir) reverse(item.begin(), item.end());
            
            res.push_back(item);
        }
        return res;
    }
};
```

BitBrave, 2019-06-27

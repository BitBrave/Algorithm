# LeetCode(99. Recover Binary Search Tree)题解
------
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

    Input: [1,3,null,null,2]

    1
    /
    3
     \
      2

    Output: [3,1,null,null,2]

    3
    /
    1
    \
    2
Example 2:

    Input: [3,1,4,null,null,2]

     3
    / \
    1   4
    /
    2

    Output: [2,1,4,null,null,3]

      2
     / \
    1   4
        /
        3
Follow up:

    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?

## 解题思路
给出一个BST树，其中有两个值交换了位置导致出错。需要在O(n)的时间内，O(1)的空间下纠正这个错误。

因为题目保证了只有两个值被交换，因此只要找出两处不和谐的地方，然后判断一下就可以了。可以利用中序遍历法（一个正确的BST的中序遍历下是递增的）找出局部降序点

使用函数从root节点出发，寻找局部降序点。

注意局部降序点有两种情况，一种是两个相邻的点交换了位置如（3，5，4）只有4和5交换，一种是不相邻的两个点交换了位置（3，8，5，6，7，4，9）8和4交换了位置。第一个的局部降序点是5，4。需要交换4和5。第二个的降序点是8，5和7，4，需要交换8和4.

因此，在使用函数寻找降序点的时候. 使用两个指针，首先找到第一个降序点，记录当前节点和上一个节点，如第一个记录4和5。然后继续寻找第二个。如果找到了第二个，就把之前记录的当前节点换成现在的当前节点。然后返回。如果找不到，表示是相邻的交换。直接返回即可。

代码如下：

Runtime: 16 ms, faster than 98.67% of C++ online submissions for Recover Binary Search Tree.
Memory Usage: 17.7 MB, less than 80.93% of C++ online submissions for Recover Binary Search Tree.

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
    TreeNode* back = NULL;
    TreeNode* fore = NULL;
    TreeNode* last = NULL;
    
public:
    void inorder(TreeNode* root){
        if(root == NULL) return;
        inorder(root->left);
        
        if(last != NULL && last->val > root->val){
            if(back == NULL){
                back = last;
                fore = root;
            }
            else fore = root;
        }
        
        last = root;
        
        inorder(root->right);
    }
    void recoverTree(TreeNode* root) {
        inorder(root);
        
        if(back != NULL) swap(back->val, fore->val);
        return;
    }
};
```

BitBrave, 2019-06-25
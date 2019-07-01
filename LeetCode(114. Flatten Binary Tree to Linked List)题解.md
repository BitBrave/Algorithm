# LeetCode(114. Flatten Binary Tree to Linked List)题解
------
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

## 解题思路
给出一个二叉树。要求将其平铺成一个链表。

可以看出，二叉树平铺成链表的方式是将二叉树按照前序遍历的方式全部按照右子树的方向向下连接。

因此，可以使用递归的方式，给出一个函数，输入二叉树，返回将二叉树转成链表的最后一个节点。处理方式如下：将当前树的左子树放到右边节点，运行同样的函数，输入左子树，返回的节点则指向当前子树的，再执行对应函数，输入右子树。

代码如下：

Runtime: 4 ms, faster than 96.31% of C++ online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 9.7 MB, less than 53.49% of C++ online submissions for Flatten Binary Tree to Linked List.

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
    TreeNode* flatten_(TreeNode* root){
        if(root->left == NULL && root->right == NULL) return root;
        if(root->left == NULL) return flatten_(root->right);
        TreeNode *a = flatten_(root->left);
        
        if(root->right == NULL) {
            root->right = root->left;
            root->left = NULL;
            return a;
        }
        TreeNode* b = flatten_(root->right);
        a->right = root->right;
        root->right = root->left;
        root->left = NULL;
        return b;
    }
    void flatten(TreeNode* root) {
        if(root == NULL) return;
        
        flatten_(root);
        return;
    }
};
```
PS: 太坑了，花了太多的时间。这里一定要注意，root->left = NULL 啊。不然一直会报堆错误。啊啊啊啊啊啊。
BitBrave, 2019-07-01
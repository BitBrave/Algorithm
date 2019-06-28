# LeetCode(105. Construct Binary Tree from Preorder and Inorder Traversal)题解
------
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    Return the following binary tree:

        3
       / \
      9  20
        /  \
       15   7

## 解题思路
给出一个树的前序和中序遍历，恢复这个树的结构，树中元素是不重复的。

对于二叉树来说，前序和中序遍历可以唯一地确定一个树的结构，如果元素没有重复的话。方法如下，首先看前序第一个一定根节点，然后在中序遍历里查看这个根节点的位置。位置左边的元素一定是中序遍历下的左子树，位置右边的元素一定是中序遍历下的右子树。那么确定根节点之后及左右子树后，在前序遍历中从根节点之后取中序遍历左子树序列长度的序列，一定是前序遍历下的左子树。这样就又得到了一个左子树的前序和中序遍历。问题缩小了。同样，右子树一样可以得到。

因此问题规模可以一直缩小，直到为空。当判断为空时，直接返回NULL。

代码如下：

Runtime: 16 ms, faster than 89.76% of C++ online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 16.5 MB, less than 82.31% of C++ online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

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
    TreeNode* build(vector<int>& preorder, int psta, int pend, vector<int>& inorder, int ista, int iend) {
        if(psta>pend) return NULL;
        
        TreeNode *root = new TreeNode(preorder[psta]);
        int pmid = psta, imid = ista;
        while(inorder[imid] != preorder[psta]) imid++;
        pmid = imid - ista + psta;
        root->left = build(preorder, psta+1, pmid, inorder, ista, imid-1);
        root->right = build(preorder, pmid+1, pend, inorder, imid+1, iend);
        return root;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int plen = preorder.size(), ilen = inorder.size();
        return build(preorder, 0, plen-1, inorder, 0, ilen-1);
    }
};
```

BitBrave, 2019-06-28
# LeetCode(106. Construct Binary Tree from Inorder and Postorder Traversal)题解
------
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    Return the following binary tree:

        3
       / \
      9  20
        /  \
       15   7

## 解题思路
给出一个树的中序和后序遍历，恢复这个树的结构，树中元素是不重复的。

对于二叉树来说，后序和中序遍历可以唯一地确定一个树的结构，如果元素没有重复的话。方法如下，首先看后序最后一个一定是根节点，然后在中序遍历里查看这个根节点的位置。位置左边的元素一定是中序遍历下的左子树，位置右边的元素一定是中序遍历下的右子树。那么确定根节点之后及左右子树后，在后序遍历中从开始节点之后取中序遍历左子树序列长度的序列，一定是后序遍历下的左子树。这样就又得到了一个左子树的前序和中序遍历。问题缩小了。同样，右子树一样可以得到。

因此问题规模可以一直缩小，直到为空。当判断为空时，直接返回NULL。

代码如下：

Runtime: 24 ms, faster than 55.53% of C++ online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 16.7 MB, less than 74.96% of C++ online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

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
    TreeNode* build(vector<int>& postorder, int psta, int pend, vector<int>& inorder, int ista, int iend) {
        if(psta>pend) return NULL;
        
        TreeNode *root = new TreeNode(postorder[pend]);
        int pmid, imid = ista;
        while(inorder[imid] != postorder[pend]) imid++;
        pmid = imid - ista + psta - 1;
        root->left = build(postorder, psta, pmid, inorder, ista, imid-1);
        root->right = build(postorder, pmid+1, pend-1, inorder, imid+1, iend);
        return root;
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int plen = postorder.size(), ilen = inorder.size();
        return build(postorder, 0, plen-1, inorder, 0, ilen-1);
    }
};
```

BitBrave, 2019-06-28
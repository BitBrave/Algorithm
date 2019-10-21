# LeetCode(889. Construct Binary Tree from Preorder and Postorder Traversal)题解

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals `pre` and `post` are distinct positive integers.

 

**Example 1:**

```
Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
```

 

**Note:**

- `1 <= pre.length == post.length <= 30`
- `pre[]` and `post[]` are both permutations of `1, 2, ..., pre.length`.
- It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

## 解题思路

根据二叉树的前序和后序遍历，返回二叉树，如果有多个答案就返回任意一个。

根据推断可知，知道一个二叉树的前序和后序遍历，并不能确定二叉树的架构，因为在遇到一个节点只有左子树或右子树时是无法确定的。因此为了得到答案，我们可以假定遇到这种情况时，都判定为左子树即可。

可以构造一个递归函数，输入一个数据的前序-后序遍历表，然后前序的第一个和后序的最后一个一定是根节点，取出这个节点，然后构建根节点的左右子树，有以下几种情况。

- 前序后序列表中只有一个数，表示只有一个节点，直接返回即可。
- 在后序列表中寻找前序列表中第二个数，如果是倒数第二个这个根节点只有左子树或者右子树，这时候直接判定为左子树，等于直接找到了左子树的根节点，然后递归到下一层。
- 如果不是倒数第二个，表示找到的是左子树的根节点，那么这个数在后序中与最后一个节点之间组成的是右子树，左边的是左子树，同样前序中对应长度的组成左子树和右子树的前序和后序遍历。直接递归到下一层即可。

这个如果每次都暴力寻找的话，每个节点要遍历所有的列表，时间总共要O(n2)，但是可以使用两个全局Map提前记录前序和后序的位置，这样最终的时间复杂度为O(n)，空间复杂度为O(n)。

代码如下。

`Runtime: 16 ms, faster than 17.26% of C++ online submissions for Construct Binary Tree from Preorder and Postorder Traversal.`

`Memory Usage: 13.9 MB, less than 16.67% of C++ online submissions for Construct Binary Tree from Preorder and Postorder Traversal.`

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
    map<int, int> post_map, pre_map;
    vector<int> Pre, Post;
public:
    TreeNode* cons(int pre_sta, int pre_end, int post_sta, int post_end){
        if(pre_sta > pre_end) return NULL;
        if(pre_sta == pre_end) return new TreeNode(Pre[pre_sta]);
        TreeNode* root = new TreeNode(Pre[pre_sta]);
        root->left = cons(pre_sta+1, pre_sta+1+post_map[Pre[pre_sta+1]]-post_sta, post_sta, post_map[Pre[pre_sta+1]]);
        
        root->right = cons(pre_sta+2+post_map[Pre[pre_sta+1]]-post_sta, pre_end, post_map[Pre[pre_sta+1]]+1, post_end-1);
        return root;
    }
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        int len = pre.size();
        Pre = pre;
        Post = post;
        for(int i=0; i<len; i++){
            pre_map[pre[i]] = post_map[post[i]] = i;
        }
        return cons(0, len-1, 0, len-1);
    }
};
```

BitBrave，2019-10-21
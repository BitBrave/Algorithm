# LeetCode(\979. Distribute Coins in Binary Tree Medium)题解

Given the `root` of a binary tree with `N` nodes, each `node` in the tree has `node.val` coins, and there are `N` coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/01/18/tree1.png)**

```
Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2019/01/18/tree2.png)**

```
Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2019/01/18/tree3.png)**

```
Input: [1,0,2]
Output: 2
```

**Example 4:**

**![img](https://assets.leetcode.com/uploads/2019/01/18/tree4.png)**

```
Input: [1,0,0,null,3]
Output: 4
```

 

**Note:**

1. `1<= N <= 100`
2. `0 <= node.val <= N`

## 解题思路

给出了一个二叉树，每个节点都有个数字代表当前节点有多少个金币，保证所有节点的金币数量之和等于节点个数。现在要求把金币平分到每个节点，使得每个节点都只放1个金币。问需要的移动次数是多少？

首先，给定了一个二叉树的状态，只要不做重复移动，那么可以证明，移动是无状态的。也就是说，最终的移动次数不会因为先给谁后给谁，或者先移动几个再移动几个，再或者把某些金币移动到近的节点把另外一些金币移动到远的节点而有所不同。

一开始我的思路就是分别统计左右子树缺少的金币个数，然后把每个节点和其子树总体的金币分配到位。累计所有节点和其子树所需要的移动次数就是结果。

但是这个题可以使用更简单的办法做。因为从叶子到跟寻找，对于每个节点，只能剩下一个。多了的值肯定要全给父亲，少的值全问父亲要，统计一下就好了。

因此我们建立一个DFS，输入根节点，返回这个二叉树的缺少或多余的金币，如果大于0说明多了，小于说明少了，等于则刚刚好。那么对于当前的节点来说，假设我们把左右都DFS完毕，那么这时候根据左边和右边的情况，假设我们已经将缺少或者多余的金币的需求都放在了左右子根节点上（就是我们只需要再移动一次就可以了）。我们还需要将金币进行移动，根据推算这个移动从次数就是abs(DFS(left))+abs(DFS(right))。可以检验不管是什么情况，最后都是这个表达式。而DFS返回的值应该为DFS(left)+DFS(right)+root->val-1，表示当前根节点所代表的子树需要从根节点的父节点拿多少金币或给出多少金币。

因此，我们在DFS的过程中，每次到达一个节点，都计算左子树上传或下载多少个金币，右子树需要上传或下载多少个金币，将二者相加即可。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 4 ms, faster than 91.60% of C++ online submissions for Distribute Coins in Binary Tree.`

`Memory Usage: 13.1 MB, less than 94.44% of C++ online submissions for Distribute Coins in Binary Tree.`

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
    int ret;
public:
    int DFS(TreeNode* root){
        if(root == NULL) return 0;
        int l = DFS(root->left), r = DFS(root->right);
        ret += abs(l) + abs(r);
        return root->val - 1 + l + r;
    }
    int distributeCoins(TreeNode* root) {
        ret = 0;
        DFS(root);
        return ret;
    }
};
```

BitBrave，2019-11-20
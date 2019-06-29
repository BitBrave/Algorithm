# LeetCode(109. Convert Sorted List to Binary Search Tree)题解
------
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

    Given the sorted linked list: [-10,-3,0,5,9],

    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

         0
        / \
      -3   9
      /   /
    -10  5

## 解题思路
给一个单调递增的链表序列，将其转变为BST。

一个简单的方法，可以将链表内的Val都拿出来形成一个数组，然后直接每次对半分开建立BST即可，这样空间复杂度O(n)，时间复杂度O(n)。不过为了省内存，可以直接在链表上操作，空间复杂度O(1)，但是时间复杂度会变成O(n2)。这里我选择第一种。

代码如下：

Runtime: 712 ms, faster than 5.11% of C++ online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 354.1 MB, less than 5.03% of C++ online submissions for Convert Sorted List to Binary Search Tree.

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* buildBST(vector<int> H, int sta, int end){
        if(sta>end) return NULL;
        int mid = (sta + end) / 2;
        TreeNode* root = new TreeNode(H[mid]);
        root->left = buildBST(H, sta, mid-1);
        root->right = buildBST(H, mid+1, end);
        return root;
    }
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> H;
        while(head != NULL){
            H.push_back(head->val);
            head = head->next;
        }
        return buildBST(H, 0, H.size()-1);
    }
};
```

BitBrave, 2019-06-29

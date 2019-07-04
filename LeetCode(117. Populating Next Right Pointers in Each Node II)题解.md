# LeetCode(117. Populating Next Right Pointers in Each Node II)题解
------

Given a binary tree

    struct Node {
        int val;
        Node *left;
        Node *right;
        Node *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

![](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

Example:



    Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

    Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.


Note:

    You may only use constant extra space.
    Recursive approach is fine, implicit stack space does not count as extra space for this problem.

## 解题思路
给出一个二叉树，将其按层次的方式从左节点指向右节点。要求是空间花费常量, 如果对应的层右边没有，则指向NULL。

可以直接使用队列进行层序遍历，每一层中左边指向右边，因为给出的说递归内的堆栈可以不计入常量空间的考量。那么队列的非递归方式肯定也是可以AC的。

代码如下：

Runtime: 400 ms, faster than 79.08% of C++ online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 66.9 MB, less than 13.93% of C++ online submissions for Populating Next Right Pointers in Each Node II.

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() {}

    Node(int _val, Node* _left, Node* _right, Node* _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* connect(Node* root) {
        if(root == NULL) return root;
        queue<Node*> Q;
        int c = 1;
        Q.push(root);
        while(!Q.empty()){
            c = Q.size() - 1;
            Node *last = Q.front(), *next; Q.pop();
            if(last->left != NULL) Q.push(last->left);
            if(last->right != NULL) Q.push(last->right);
            while(c>0){
                c--;
                next = Q.front(); Q.pop();
                if(next->left != NULL) Q.push(next->left);
                if(next->right != NULL) Q.push(next->right);
                last->next = next;
                last = next;
            }
        }
        return root;
    }
};
```

BitBrave 2019-07-04
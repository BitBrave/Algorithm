# LeetCode(142. Linked List Cycle II) 题解
------
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:

    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

Example 2:

    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.
![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

Example 3:

    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)
 

Follow-up:
Can you solve it without using extra space?



## 解题思路

给一个链表。判断有没有环，有环的话，找出这个环的交接点。

在不使用别的空间的情况下，首先使用双指针一个走一步一个走两步，如果最后会重合的话，说明有环，没有则算法结束返回NULL。然后还是双指针sp,fp,如果链表中存在环，那么fp和sp一定会相遇，当两个指针相遇的时候，我们设相遇点为c，此时fp和sp都指向了c，接下来令fp继续指向c结点，sp指向链表头结点head，此时最大的不同是fp的步数变成为每次走一步，令fp和sp同时走，每次一步，那么它们再次相遇的时候即为环的入口结点。

这里有一个链接，很详细：<https://blog.csdn.net/willduan1/article/details/50938210>

代码如下：

Runtime: 12 ms, faster than 84.65% of C++ online submissions for Linked List Cycle II.
Memory Usage: 9.7 MB, less than 70.60% of C++ online submissions for Linked List Cycle II.

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(head == NULL || head->next == NULL) return NULL;
        ListNode *fp = head->next->next, *sp = head->next;
        while(fp != NULL){
            if(sp == fp) break;
            sp = sp->next;
            if(fp->next != NULL) fp = fp->next->next;
            else return NULL;
        }
        if(fp == NULL) return NULL;
        sp = head;
        while(sp != fp){
            sp = sp->next;
            fp = fp->next;
        }
        return sp;
    }
};
```

BitBrave, 2019-07-07
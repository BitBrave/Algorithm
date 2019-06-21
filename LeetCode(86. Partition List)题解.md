# LeetCode(86. Partition List)题解
------
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5

## 解题思路
给定一个链表和一个值X，将链表中节点值小于X的都排在节点大于等于X的节点的前面。在此基础上，各个节点保持相应的原始次序。

使用两个指针A和B，分别记录小于X和大于等于X的节点的链表的开始。一开始都为NULL。

从左到右遍历链表，如果当前节点S的值小于X，然后判断A，如果A为NULL，则表示这是第一个小于X的节点。直接A = S，如果A不为空则A->next = S; A = A->next;

反之，如果当前节点S的值大于等于X，然后判断B，如果B为NULL，则表示这是第一个大于等于X的节点。直接B = S，如果B不为空则B->next = S; B = B->next;

最后遍历完成之后，如果AB都为空，返回NULL。如果A为空，B->next = NULL,返回B对应的头链表指针。如果B为空，A->next=NULL, 返回A对应的头指针。都不为空格则，A->next = B的头指针，B->next = NULL;

因此在使用A，B的时候，要记录下对应链表的头指针。

代码如下：

Runtime: 4 ms, faster than 98.82% of C++ online submissions for Partition List.
Memory Usage: 8.7 MB, less than 22.67% of C++ online submissions for Partition List.

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
    ListNode* partition(ListNode* head, int x) {
        if (head == NULL) return NULL;
        ListNode *A = NULL, *A1 = NULL, *B = NULL, *B1 = NULL;
        while (head != NULL) {
            if(head->val < x){
                if(A == NULL){
                    A = head;
                    A1 = A;
                }
                else {
                    A->next = head;
                    A = A->next;
                }
            }
            else {
                if(B == NULL){
                    B = head;
                    B1 = B;
                }
                else {
                    B->next = head;
                    B = B->next;
                }
            }
            head = head->next;
        }
        if(A == NULL){
            B->next = NULL;
            return B1;
        }
        if(B == NULL){
            A->next = NULL;
            return A1;
        }
        A->next = B1;
        B->next = NULL;
        return A1;
    }
};
```

BitBrave, 2019-06-21
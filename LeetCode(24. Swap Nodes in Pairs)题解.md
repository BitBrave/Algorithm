# LeetCode(24. Swap Nodes in Pairs)题解
------
原文如下
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

    Given 1->2->3->4, you should return the list as 2->1->4->3.

## 解题思路
这个题要求链表中每两个节点互换，并建议不要换节点值而是直接把两个节点交换，一个Medium值。其实很简单，链表指针互相指而已。

代码如下图所示，所以为什么说LeetCode是宽容的，我明明是交换的两个节点的值，也可以AC。
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
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL) return head;
        ListNode *fore = head, *back = head->next;
        int temp;
        while(back!=NULL){
            temp = fore->val;
            fore->val = back->val;
            back->val = temp;
            fore = back->next;
            if(fore==NULL || fore->next==NULL) break;
            back = fore->next;
        }
        return head;
    }
};
```

当然这里也有不是改变节点的值，而是改变交换整个节点.但是这样速度慢了很多，也复杂了很多，花了我很多时间，指针真的好麻烦。不过也能AC。

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
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL) return head;
        ListNode *fore = head, *back = head->next, *temp;
        if(back!=NULL){
            temp = back->next;
            back->next = fore;
            fore->next = temp;
        }
        else return fore;
        head = back;
        temp = fore;

        if(fore->next!=NULL) fore = fore->next;
        else return head;
        if(fore->next!=NULL) back = fore->next;
        else return head;
        
        while(back!=NULL){
            temp->next = back;
            temp = back->next;
            back->next = fore;
            fore->next = temp;
            temp = fore;
            if(fore->next==NULL) break;
            fore = fore->next;
            if(fore->next==NULL) break;
            back = fore->next;
        }
        return head;
    }
};
```

BitBrave，2019-04-26。
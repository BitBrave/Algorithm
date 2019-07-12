# LeetCode(143. Reorder List)题解
------
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

    Given 1->2->3->4, reorder it to 1->4->2->3. 
Example 2:

    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

## 解题思路
给一个链表，将其头尾依次取一个组成新的链表并返回。

用一个vector记录下所有的Node，然后嘿嘿嘿。

代码如下：

Runtime: 44 ms, faster than 96.64% of C++ online submissions for Reorder List.
Memory Usage: 13.1 MB, less than 14.66% of C++ online submissions for Reorder List.

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
    void reorderList(ListNode* head) {
        if(head == NULL || head->next == NULL) return;
        vector<ListNode*> V;
        int len = 0;
        while(head != NULL){
            V.push_back(head);
            head = head->next;
            len++;
        }
        for(int i=0; i<=len-3; i++){
            V[i]->next = V[len-1];
            V[len-1]->next = V[i+1];
            V[len-2]->next = NULL; 
            len--;
        }
        return;
    }
};
```

BitBrave, 2019-07-12

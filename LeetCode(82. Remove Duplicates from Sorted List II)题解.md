# LeetCode(82. Remove Duplicates from Sorted List II)题解
------
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

    Input: 1->2->3->3->4->4->5
    Output: 1->2->5
Example 2:

    Input: 1->1->1->2->3
    Output: 2->3

## 解题思路
给一个链表，删除其中所有重复的节点，对应节点全部删除

单次遍历即可，使用两个指针，一个指向当前节点的上一个值不同的节点，一个指向当前节点，查看下一个节点，如果与当前节点一样，就删除这两个节点，指针指向当前节点的下下个节点。如果不同，则当前节点指针都向前移动一个，直到指针为空。

初始化则用一个指针指向head，一个指向NULL，如果Head的下一个和Head一样，则指向Head的指向Head的下下个，以此类推，如果不一样，则用两个指针分别指向这两个。达到了上述的要求，递归下去即可。

代码如下：
Runtime: 8 ms, faster than 92.93% of C++ online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 9.4 MB, less than 8.37% of C++ online submissions for Remove Duplicates from Sorted List II

```C++
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
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL) return head;
        ListNode *back = NULL, *fore = head;
        int c = 0;
        while(fore->next!=NULL){
            if(fore->val != fore->next->val){
                if(c==0) break;
                fore = fore->next;
                c = 0;
                continue;
            }
            c = -1;
            fore = fore->next;
        }
        if(c==-1) return NULL;
        head = fore;
        back = fore->next;
        fore->next = NULL;
        while(back!=NULL){
            if(back->next==NULL) break;
            while(back->next!=NULL){
                if(back->val != back->next->val) {
                    if(c==0) break;
                    back = back->next;
                    c = 0;
                    continue;
                }
                c = -1;
                back = back->next;
            }
            if(c==-1) return head;
            fore->next = back;
            fore = back;
            back = back->next; 
            fore->next = NULL;
        }
        if(c==-1) return head;
        fore->next = back;
        return head;
    }
};
```

BitBrave, 2019-06-18
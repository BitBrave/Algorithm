# LeetCode(92. Reverse Linked List II)题解
------
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL

## 解题思路
一次遍历的过程中，将一个链表的从m到n位置之间的链表进行反转。

可以使用一个for循环的办法，用一个数C记录遍历到的位置。在C开始的时候返回的正常的节点下一个指针，在C在m和n之中的时候开始进行反向。

具体代码如下：

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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if(m == n) return head;
        int c = 1;
        ListNode *fore = head, *back = head, *Fore = NULL, *h;
        
        while(c < m){
            Fore = fore;
            fore = fore->next;
            c++;
        }
        back = fore->next;
        h = fore;
        while(c < n){
            fore->next = back->next;
            back->next = h;
            h = back;
            back = fore->next;
            c++;
        }
        if(Fore == NULL) return h;
        
        Fore->next = h;
        return head; 
    }
};
```

BitBrave, 2019-06-23
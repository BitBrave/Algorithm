# LeetCode(61. Rotate List)题解
------
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
    rotate 1 steps to the right: 2->0->1->NULL
    rotate 2 steps to the right: 1->2->0->NULL
    rotate 3 steps to the right: 0->1->2->NULL
    rotate 4 steps to the right: 2->0->1->NULL


## 解题思路
Medium， 给一个链表，再从给定的位置进行旋转。给定的K为旋转多少次，K等于1就将最后一个数移到最前面，2的话就在1的基础上重复这个操作。

方法很简单，首先遍历链表，得到长度Len，再将K变成K=K % Len，因为旋转长度的倍数次得到的结果还是本身。然后再遍历以此，走到第K个的时候，将其作为头指针，最后的指针指向最开始的头指针即可。

代码如下：

Runtime: 8 ms, faster than 94.78% of C++ online submissions for Rotate List.
Memory Usage: 9.1 MB, less than 55.71% of C++ online submissions for Rotate List.

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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL || head->next == NULL || k == 0) return head;
        
        int len = 1;
        ListNode *fore = head;
        
        while(fore->next != NULL){
            fore = fore->next;
            len++;
        }
        k = len - k % len;
        if(k == 0) return head;
        fore->next = head;
        fore = head;
        for(int i=1; i<k; i++) fore = fore->next;
    
        head = fore->next;
        fore->next = NULL;
        
        return head;
    }
};
```

BitBrave, 2019-06-03
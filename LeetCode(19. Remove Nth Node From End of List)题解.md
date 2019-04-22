# LeetCode(19. Remove Nth Node From End of List)题解
------
原文如下：

Given a linked list, remove the n-th node from the end of list and return its head.

**Example:**

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.
**Note:**

Given n will always be valid.

**Follow up:**

Could you do this in one pass?

## 题意理解
这个题Medium，要求给定一个链表的头指针，删除这个链表内倒数第n个节点。一般来说很简单，最直观的方式就是我遍历两遍，第一遍找出总长度，计算倒数第n个节点的在顺数第几个，第二次遍历直接删除。或者遍历一次，每一步都记录下节点的值，最后找到对应的第n个删除，再用剩下的额值重新建立一个链表。这两种方法一个是加大了时间，一个增加了空间。况且题目建议一次遍历即可。

那么如何做呢？可以使用递归的方式，利用函数天然的堆栈空间进行位置记录。具体采用如下策略：

    1 从head进入，传入当前节点地址，pos位置参数（引用实参），和需要删除的节点参数n
    2 进入递归函数，直接走到最后一个，将pos=1，开始返回
    3 通过n是否等于pos来判断是否当前节点是需要删除的，如果不等于则返回当前节点，如果等于则直接返回当前节点的递归回来的节点（当前节点的下一个节点）
    4 递归结束后直接返回删除对应位置节点之后的链表的head节点

代码如下，faster than 100% exampls。

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
    ListNode* recNode(ListNode* node, int &pos, int n){
        if(node->next == NULL){
            pos = 1;
            if(n == pos){
                pos = INT_MAX;
                return NULL;
            }
            return node;
        };
        
        ListNode* bnode = recNode(node->next, pos, n);
        
        pos = (INT_MAX==pos) ? pos : pos + 1;
        node->next = bnode;
        
        if(n == pos) {
            pos = INT_MAX;
            return bnode;
        };
        return node;    
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head == NULL) return NULL;
        int pos = INT_MAX;
        return recNode(head, pos, n);
    }
};
```

BitBrave，2019-04-22
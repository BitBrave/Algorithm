# LeetCode(25. Reverse Nodes in k-Group)题解
------
原文如下
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

    Given this linked list: 1->2->3->4->5

    For k = 2, you should return: 2->1->4->3->5

    For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

## 解题思路
这是一个Hard的题，要求给定一个链表和一个数K，将链表依次的K个节点反链接。比如1->2-3->4->5，K=2，得出的结果就是2->1->4->3->5.要求就是只能扩展常量内存，不要交换值，要交换节点。

其实很简单，主要是指针指来指去有点麻烦而已。既然内存是常量限制，而K是不定的，那么我能想到的就是使用递归了。假设这有一个函数reverse，输入一个头指针sta，一个尾指针end，可以将一个链表反向由sta->...->end变成end->...sta，那么直接在主函数内调用这个就可以了。但是要注意的是，sta和end在打的链表内各自还有指向与被指向的地方。所以要注意a->sta->...->end->b，变为a->end->...sta->b。

接下来介绍函数void reverse(ListNode* sta, ListNode* end)，其中sta是头指针，end是尾指针。函数的递归策略如下：

a）首先判断sta->next是否是end，如果是表示sta直接指向了end，这时候需要反转，通过一个temp指针实现sta->end->XXX到end->sta->XXX，然后直接返回。
b）如果sta和end之间还隔着很多节点，那么就运行递归函数reverse(sta->next, end)，但是为了处理方便，后面需要交换，所以令temp=sta->next; reverse(temp, end)
c）当b完成后，实际上此时的链表为sta->temp，end->...temp->XXX（原本格式为sta->temp->...end->XXX），需要转为end->...->temp->sta->XXX; 即将sta插入temp与XXX之间，直接运行sta->next = temp->next;temp->next = sta;即可。最后返回

而在主函数中，我们先将一次反转的end指针找到，所以利用K计数法，每K次运行一次reverse，注意第一次返回的end指针是头指针，总的函数需要返回这个，后面reverse返回的end指针前面连接了总的大链表的指针。

因此我们需要用一个s_sta来记录end需要反转的节点之前的节点，在进入reverse之前，大链表结构为s_sta->sta->...->end->XXX，reverse之后，大链表的结构为s_sta->sta, end->...->sta->XXX。此时同理，需要将大链表串联起来，直接使用s_sta->next = end，即可。然后令s_sta = sta; sta = s_sta->next; end = sta;开始新一轮的寻找end指针的循环。如果不到K次，直接end = end->next; 即可。

代码如下：
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
    void reverse(ListNode* sta, ListNode* end){
        ListNode* temp = sta->next;
        if(sta->next == end){
            sta->next = end->next;
            end->next = sta;
            return;
        }
        
        reverse(temp, end);
        sta->next = temp->next;
        temp->next = sta;
        return;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head==NULL || k<=1) return head;
        ListNode *sta = head, *end = head, *s_sta = NULL;
        int c = 1;
        while(end!=NULL){
            if(c % k == 0) {
                reverse(sta, end);
                if(s_sta!=NULL) s_sta->next = end;
                head = s_sta!=NULL ? head:end;
                s_sta = sta;
                sta = s_sta->next;
                end = sta;
                c = 1;
            }
            else{
                end = end->next;
                c++;
            }
        }
        return head;
    }
};
```

PS：在写解题报告的过程中，再次阅读代码会发现很多可以优化的地方，使得代码更有可读性，我写这个时候就发现不少可以优化的地方，看来写报告是一个不错的复盘的方式。

BitBrave，2019-04-28。
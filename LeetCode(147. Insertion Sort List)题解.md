# LeetCode(147. Insertion Sort List)题解
------
Sort a linked list using insertion sort.

![](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

    Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    It repeats until no input elements remain.

Example 1:

    Input: 4->2->1->3
    Output: 1->2->3->4
Example 2:

    Input: -1->5->3->4->0
    Output: -1->0->3->4->5

## 解题思路
实现链表的插入排序。

没什么好说的，民工题。每次插入从头到尾找到位置交换就可以了。

代码如下

Runtime: 52 ms, faster than 50.23% of C++ online submissions for Insertion Sort List.
Memory Usage: 9.5 MB, less than 67.84% of C++ online submissions for Insertion Sort List.

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
    ListNode* insertionSortList(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;
        
        ListNode *fore = head;
        ListNode *tmp;
        while(fore->next != NULL){
            tmp = head;
            if(tmp->val >= fore->next->val){
                ListNode* t = fore->next->next;
                head = fore->next;
                head->next = tmp;
                fore->next = t;
                continue;
            }
            if(tmp->next == fore->next){
                fore = fore->next;
                continue;
            }
            while(tmp->next != NULL && tmp->next != fore->next){
                if(tmp->next->val < fore->next->val){
                    tmp = tmp->next;
                    if(tmp->next == fore->next){
                        fore = fore->next;
                        break;
                    }
                    continue;
                }
                
                ListNode* t = tmp->next;
                tmp->next = fore->next;
                fore->next = fore->next->next;
                tmp->next->next = t;
                break;
            }
        }
        return head;
    }
};
```

指针真的，太恶心了。

BitBrave, 2019-07-11
# LeetCode(148. Sort List)题解
------

## 解题思路
对一个链表进行排序，使用常量空间，时间复杂度O(nlogn)。

使用归并排序就好了。首先遍历出其长度，再依次归并即可。

代码如下：

Runtime: 36 ms, faster than 99.77% of C++ online submissions for Sort List.
Memory Usage: 11.7 MB, less than 70.58% of C++ online submissions for Sort List.

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
    ListNode* mergeSort(ListNode* head, int l){
        if(l<=0) return NULL;
        if(l == 1) return head;
        int m = l/2;
        ListNode* mid = head;
        for(int i=0; i<m; i++) mid = mid->next;
        
        ListNode* left = mergeSort(head, m);
        ListNode* right = mergeSort(mid, l-m);
        // ---
        ListNode *merge, *M;
        int llen = m, rlen = l-m;
        if(left->val < right->val){
            merge = left;
            left = left->next;
            llen--;
        }
        else{
            merge = right;
            right = right->next;
            rlen--;
        }
        M = merge;
        while(llen > 0 && rlen > 0){
            if(left->val < right->val){
                merge->next = left;
                left = left->next;
                llen--;
            }
            else{
                merge->next = right;
                right = right->next;
                rlen--;
            }
            merge = merge->next;
        }
        while(llen > 0){
            merge->next = left;
            left = left->next;
            merge = merge->next;
            llen--;
        }
        while(rlen > 0){
            merge->next = right;
            right = right->next;
            merge = merge->next;
            rlen--;
        }
        merge->next = NULL;
        return M;
    }
    ListNode* sortList(ListNode* head) {
        ListNode* res = head;
        if(res == NULL) return res;
        int len = 0;
        while(res != NULL){
            res = res->next;
            len++;
        }
        return mergeSort(head, len);
    }
};
```

BitBrave, 2019-07-10
# LeetCode(23. Merge k Sorted Lists)题解
------
原文如下：
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

    Input:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    Output: 1->1->2->3->4->4->5->6

## 解题思路
这是一个Hard的题目，要求对N个局部有序的链表进行合并得到一个大的有序链表。刚刚看到这个题的时候有点怵，倒不是说解法有什么困难，主要是怕写出来的code超时。但是不得不说LeetCode是很宽容的，这个题用最简单的方法就可以完成，虽然速度，慢了点。这里假设有N个链表，每个链表长度为M。

## 解法1
可以这样做，每次取出两个两个链表，进行合并，两个都是局部有序的，因此只需要一次遍历就能完成，第一次花费O(2m)的时间，然后返回新的合并链表的头指针，重复这个过程第二次O(3m),第三次O(4m)....直到最后，总的时间复杂度为：O(2m)+O(3m)+O(4m)+ ...+O(nm) = O(n2m)。

代码如下，168ms，faster than 27%examples，Memory 10.7M, less than 99.8% examples.

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
    ListNode* merge2Lists(ListNode* a, ListNode* b){
        ListNode* head = NULL, *m = NULL;
        if(a==NULL) return b;
        if(b==NULL) return a;
        
        if(a->val <= b->val){
            head = a;
            m = head;
            a = a->next;
        }
        else{
            head = b;
            m = head;
            b = b->next;
        };
        
        while(a!=NULL && b!=NULL){
            if(a->val <= b->val){
                m->next = a;
                a = a->next;
            }
            else{
                m->next = b;
                b = b->next;
            }
            m = m->next;
        };
        
        if(a==NULL) m->next = b;
        if(b==NULL) m->next = a;
       
        return head;
        
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size()==0) return NULL;
        
        int len = lists.size();
        ListNode* m = lists[0];
        for(int i=1; i<len; i++){
            m = merge2Lists(m, lists[i]);
        };
        return m;
    }
};
```

## 解法2
因为担心时间问题，我还想了另外一种解法，就是使用heap(一种完全二叉树)，具体方式如下：c++的STL内heap的使用见[链接](https://blog.csdn.net/zsc2014030403015/article/details/45872737)

    将N个链表头指针根据存的值的大小建立一个最小堆。花费时间自顶向下则为O(nlogn)，自底向上则为O(n).[证明在此](https://www.jianshu.com/p/7cf64b02c0a4)
    每次堆头部的指针所指向的值肯定是所有链表内最小的，取出这个值，然后代替以其链表下一个值，若是对应链表内最后一个则取堆内最后一个位置的指针填充堆头位置，然后重新建立整理一下堆，每次整理花费O(logn)
    一共nm个链表节点，总的时间复杂度为O(n)/O(nlogn)+nm*O(logn)=O(nmlogn).

代码如下，注意pop_heap(&M[0],&M[tlen],cmp);函数不返回值，而是将根节点的值交换到数组的最后一个，运行完了之后时候直接在取出M[tlen-1\]即可。同理push_heap(&M[0],&M[tlen],cmp);也是一样，将需要插入的数放入M[tlen]后运行push_heap即可。
这样的code效果：24ms，faster than 99%examples，Memory 11.1M, less than 99.5% examples.

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
    static bool cmp(ListNode* a, ListNode* b){
        return a->val > b->val;
    }
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size()==0) return NULL;
        
        int len = lists.size(), tlen = 0;
        
        ListNode **M = new ListNode*[len];
        ListNode *head = NULL, *m = NULL;
        for(int i=0; i<len; i++){
            if(lists[i]!=NULL) M[tlen++]=lists[i];
        };
        if(tlen == 0) return NULL;

        make_heap(&M[0],&M[tlen],cmp);

        pop_heap(&M[0],&M[tlen],cmp);
        head = M[tlen-1];
        m = head;
        if(M[tlen-1]->next != NULL) {
            M[tlen-1] = M[tlen-1]->next;
            push_heap(&M[0],&M[tlen],cmp);
        }
        else tlen--;
        while(tlen>0){
            pop_heap(&M[0],&M[tlen],cmp);
            
            m->next = M[tlen-1];
            m = m->next;

            if(M[tlen-1]->next != NULL) {
                M[tlen-1] = M[tlen-1]->next;
                push_heap(&M[0],&M[tlen],cmp);
            }
            else tlen--;
        }
        
        return head;
    }
};
```

BitBrave, 2019-04-25, 完全是由自己做出来的，非常开心。
# LeetCode(817. Linked List Components)题解
------
Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

    Input: 
    head: 0->1->2->3
    G = [0, 1, 3]
    Output: 2
    Explanation: 
    0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

    Input: 
    head: 0->1->2->3->4
    G = [0, 3, 1, 4]
    Output: 2
    Explanation: 
    0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

    If N is the length of the linked list given by head, 1 <= N <= 10000.
    The value of each node in the linked list will be in the range [0, N - 1].
    1 <= G.length <= 10000.
    G is a subset of all values in the linked list.

## 解题思路
用一个与链表等长的数组，记录当前值是否在G内，然后遍历链表，用一个bool值记录当前节点的上一个是否是子集内的，如果是就true，否则false。然后查看当前值是否存在子集内，如果存在就继续向下走，bool设置为true，如果不存在，就考虑bool值是什么，如果是true，res+=1，否则继续，不管怎么样，bool设为false，因为这个值是不在子集内的。遍历结束是，看看bool值是什么，如果是false，表示最后的值是不在子集内的，就不管，否则就res+=1.

代码如下，时间复杂度O(n),空间复杂度O(n)(其实是O(1)，因为题目说不会超过10000个，就直接定为10000):

Runtime: 32 ms, faster than 97.50% of C++ online submissions for Linked List Components.
Memory Usage: 12.9 MB, less than 84.21% of C++ online submissions for Linked List Components.

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
    int numComponents(ListNode* head, vector<int>& G) {
        bool judge = false;
        int res = 0, len = G.size();
        
        vector<bool> V(10000, false);
        for(int i=0; i<len; i++) V[G[i]] = true;
        while(head != NULL){
            if(V[head->val]) judge = true;
            else{
                res += judge ? 1 : 0;
                judge = false;
            }
            head = head->next;
        }
        res += judge ? 1 : 0;
        return res;
    }
};
```

BitBrave, 2019-08-30
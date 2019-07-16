# LeetCode(138. Copy List with Random Pointer)题解
------
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Example 1:

![](https://discuss.leetcode.com/uploads/files/1470150906153-2yxeznm.png)

    Input:
    {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

    Explanation:
    Node 1's value is 1, both of its next and random pointer points to Node 2.
    Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
    
Note:

    You must return the copy of the given head as a reference to the cloned list.

## 解题思路
给一个链表，每个节点有两个指针，一个是正常的链表指针，一个是随机指针，指向不同的地方。现在要求返回一个这个链表的复制。不能是原有节点，只能是new的新的复制版本。

民工题，可以使用Map，，以原有指针节点为key，以对应的copy节点为value。初始化为空。然后从头结点开始。查看下一个节点在不在Map内，在就直接提出来，进行操作。如果不在就加入内部。

代码如下：

Runtime: 32 ms, faster than 82.63% of C++ online submissions for Copy List with Random Pointer.
Memory Usage: 22 MB, less than 76.79% of C++ online submissions for Copy List with Random Pointer.

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == NULL) return NULL;
        Node *nhead = new Node(), *tmp;
        map<Node*, Node*> M;
        M[head] = nhead;
        M[NULL] = NULL;
        map<Node*, Node*>::iterator iter;  
        
        nhead->val = head->val;
        nhead->next = NULL;
        nhead->random = NULL;
        tmp = nhead;
        while(head != NULL){
            iter = M.find(head->next);
            if(iter != M.end()) tmp->next = iter->second;
            else{
                M[head->next] = new Node(head->next->val, NULL, NULL);
                tmp->next = M[head->next];
            }
            
            iter = M.find(head->random);
            if(iter != M.end()) tmp->random = iter->second;
            else{
                M[head->random] = new Node(head->random->val, NULL, NULL);
                tmp->random = M[head->random];
            }
            head = head->next;
            tmp = tmp->next;
        }
        return nhead;
    }
};
```

BitBrave, 2019-07-16
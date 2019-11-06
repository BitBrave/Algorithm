# LeetCode(946. Validate Stack Sequences)题解

Given two sequences `pushed` and `popped` **with distinct values**, return `true` if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

**Example 1:**

```
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

**Example 2:**

```
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
```

 

**Note:**

1. `0 <= pushed.length == popped.length <= 1000`
2. `0 <= pushed[i], popped[i] < 1000`
3. `pushed` is a permutation of `popped`.
4. `pushed` and `popped` have distinct values.

## 解题思路

给出两个数组pushed和poped，每个数组内的元素互相之间是不相等的。现在要判断这两个数组是否可能是从一个栈的操作上得来的，即入栈的数放入pushed，出栈的数放入poped。如果是返回True，否则False。

这个题可以直接使用模拟实现，可以知道首先肯定是入栈，那么stack首先肯定是放入pushed，然后看poped，表示第一个出栈的，那么就在pushed数组内查找这个数字，pushed内这个数字之前的一定是入栈才能将这个数入栈，然后才能出栈。因此，将pushed内的数不断入栈，找到这个数之后，poped向后移动一个，栈就出栈一个，继续看poped下一个，如果等于pushed当前位置的，就继续向下走，不在就从上一个pushed走到的位置继续往后走，并入栈。如果走到最后，栈内为空，则表示是匹配的，返回True，否则False。

代码如下，时间复杂度O(n)，空间复杂度O(n)。

`Runtime: 12 ms, faster than 48.89% of C++ online submissions for Validate Stack Sequences.`

`Memory Usage: 9 MB, less than 100.00% of C++ online submissions for Validate Stack Sequences.`

```c++
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int len = pushed.size();
        stack<int> S;
        int i = 0, j = 0;
        while(i < len){
            if(pushed[i] == popped[j]){
                i++;
                j++;
            }
            else if(!S.empty() && S.top() == popped[j]){
                S.pop();
                j++;
            }
            else S.push(pushed[i++]);
        }
        while(!S.empty() && S.top() == popped[j++]) S.pop();
        return S.empty();
    }
};
```

BitBrave，2019-11-06
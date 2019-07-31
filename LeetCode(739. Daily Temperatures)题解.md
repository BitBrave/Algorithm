# LeetCode(739. Daily Temperatures)题解
------
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

## 解题思路
给一个每天温度的数组，对于每一天，找出下一个比当前温度大的元素，记录它们之间的天数。

这题最直接的思路就是对每个数直接搜索后面的数，比其大就记录下位置。时间复杂度O(n2)，空间复杂度O(1). 这样写code不会ac.

解法：使用递减栈Descending Stack，建一个长度和T相等的数组res，来记录天数，栈内存储温度位置。遍历数组，如果栈为空，直接入栈。如果栈不为空，且当前数字大于栈顶元素，表示目前的温度大于栈顶元素的温度，pop出栈顶元素，求出下标差，也就是升温的天数，把这个差值记录给栈顶元素在res中的位置。然后继续看新的栈顶元素，直到当前数字小于等于栈顶元素停止。然后将当前数字入栈。最后递减栈内所有元素对应的升温天数都是0. 最后返回res。

代码如下

Runtime: 188 ms, faster than 90.75% of C++ online submissions for Daily Temperatures.
Memory Usage: 16.1 MB, less than 52.78% of C++ online submissions for Daily Temperatures.

```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int len = T.size();
        vector<int> res(len, 0);
        stack<int> S;
        
        for(int i=0; i<len; i++){
            while(!S.empty() && T[S.top()]<T[i]){
                res[S.top()] = i - S.top();
                S.pop();
            } 
            S.push(i);
        }
        return res;
    }
};
```

BitBrave, 2019-07-31
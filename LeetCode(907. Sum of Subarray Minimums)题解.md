# LeetCode(907. Sum of Subarray Minimums)题解

Given an array of integers `A`, find the sum of `min(B)`, where `B` ranges over every (contiguous) subarray of `A`.

Since the answer may be large, **return the answer modulo 10^9 + 7.**

 

**Example 1:**

```
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
```

 

**Note:**

1. `1 <= A.length <= 30000`
2. `1 <= A[i] <= 30000`

## 解题思路

给一个数组，求出其中每个连续子树组内最小元素乘以子数组长度的值之和。

这个题做起来不是很难，但是今天有点烦躁，所以直接参考的网上的教程。rt.<https://www.cnblogs.com/grandyang/p/11273330.html>

<https://www.jianshu.com/p/8273168bab07>



代码如下.

`Runtime: 92 ms, faster than 69.07% of C++ online submissions for Sum of Subarray Minimums.`

`Memory Usage: 16.1 MB, less than 42.86% of C++ online submissions for Sum of Subarray Minimums.`

```c++
class Solution {
public:
    int sumSubarrayMins(vector<int>& A) {
        int len = A.size(), ret = 0, m = pow(10, 9) + 7;
        vector<int> left(len, 1), right(len, 1);
        stack<int> L, R;
        for(int i=0; i<len; i++){
            while(!L.empty() and A[L.top()]>A[i]) L.pop();
            left[i] = L.empty() ? i+1 : i-L.top();
            L.push(i);
            
            right[i] = len - i;
            while(!R.empty() and A[R.top()]>A[i]){
                right[R.top()] = i - R.top();
                R.pop();
            } 
            R.push(i);    
        }
        for(int i=0; i<len; i++){
            //cout<<left[i]<<right[i]<<endl;
            ret = (ret + left[i]*right[i]*A[i]) % m;
        }
        return ret;
    }
};
```

BitBrave，2019-11-18
# LeetCode(\978. Longest Turbulent Subarray)题解

A subarray `A[i], A[i+1], ..., A[j]` of `A` is said to be *turbulent* if and only if:

- For `i <= k < j`, `A[k] > A[k+1]` when `k` is odd, and `A[k] < A[k+1]` when `k` is even;
- **OR**, for `i <= k < j`, `A[k] > A[k+1]` when `k` is even, and `A[k] < A[k+1]` when `k` is odd.

That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the **length** of a maximum size turbulent subarray of A.

 

**Example 1:**

```
Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
```

**Example 2:**

```
Input: [4,8,12,16]
Output: 2
```

**Example 3:**

```
Input: [100]
Output: 1
```

 

**Note:**

1. `1 <= A.length <= 40000`
2. `0 <= A[i] <= 10^9`

## 解题思路

给一个数组，找出其中最长的起伏连续子数组，返回其长度。起伏就是数组内奇数位元素总是比相邻的偶数位置元素小，或者偶数位置元素总是比相邻奇数位置元素小。

这个题可以使用DP的方式，从左到右遍历数组，使用一个数记录遍历到当前位置，包括当前元素在内的最长连续合法子树组长度，因为合法子树组的元素内部直观来看肯定是元素一大一小一大一小之类的样子，因此只要判断下一个元素是否符合这个特征即可，如果符合就当前长度+1，如果不符合就从新开始一个即可。我们可以使用dir的异或操作控制方向，也可以两次遍历数组，第一次寻找奇数位大于偶数位的合法数组，第二次寻找偶数位大于奇数位的数组。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 128 ms, faster than 11.85% of C++ online submissions for Longest Turbulent Subarray.`

`Memory Usage: 13.3 MB, less than 100.00% of C++ online submissions for Longest Turbulent Subarray.`

```c++
class Solution {
public:
    int maxTurbulenceSize(vector<int>& A) {
        int len = A.size(), ret = 0;
        if(len <= 1) return len;
        bool dir = A[0] < A[1];
        int t = 1;
        for(int i=1; i<len; i++){
            if(A[i-1] == A[i]){
                ret = max(ret, t);
                t = 1;
                if(i+1 < len) dir = (A[i] < A[i+1]);
                continue;
            }
            if((A[i-1] > A[i]) ^ dir){
                dir = !dir;
                t += 1;
            }
            else{
                ret = max(t, ret);
                t = 2;
            }
        }
        return max(ret, t);
    }
};
```

 

分别遍历两次数组的代码。

`Runtime: 116 ms, faster than 24.88% of C++ online submissions for Longest Turbulent Subarray.`

`Memory Usage: 13.3 MB, less than 100.00% of C++ online submissions for Longest Turbulent Subarray.`

```c++
class Solution {
public:
    int maxTurbulenceSize(vector<int>& A) {
        int len = A.size(), ret = 0;
        if(len <= 1) return len;
        int t = 1;
        // odd
        for(int i=1; i<len; i++){
            if((A[i-1]==A[i]) or ((A[i-1]>A[i]) ^ (i&1))){
                ret = max(ret, t);
                t = 0;
            }   
            t += 1;
        }
        ret = max(ret, t);
        t = 1;
        // even
        for(int i=1; i<len; i++){
            if((A[i-1]==A[i]) or ((A[i-1]<A[i]) ^ (i&1))){
                ret = max(ret, t);
                t = 0;
            }   
            t += 1;
        }
        return max(ret, t);
    }
};
```

 


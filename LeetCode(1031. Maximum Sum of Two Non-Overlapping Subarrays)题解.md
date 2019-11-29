

# LeetCode(\1031. Maximum Sum of Two Non-Overlapping Subarrays)题解

Given an array `A` of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths `L` and `M`. (For clarification, the `L`-length subarray could occur before or after the `M`-length subarray.)

Formally, return the largest `V` for which `V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1])` and either:

- `0 <= i < i + L - 1 < j < j + M - 1 < A.length`, **or**
- `0 <= j < j + M - 1 < i < i + L - 1 < A.length`.



**Example 1:**

```
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
```

**Example 2:**

```
Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
```

**Example 3:**

```
Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
```

 

**Note:**

1. `L >= 1`
2. `M >= 1`
3. `L + M <= A.length <= 1000`
4. `0 <= A[i] <= 1000`

## 解题思路

给出一个非负数元素组成的数组，给定两个长度值，要求选出两个不相重的连续子数组，其和值为所有的符合条件的数组中最大的，要求返回这个和。

这个题可以依次从左到右选定一个长度的子树组，然后选择另外的数组，这个过程中保存最大值。等于就是暴力枚举。至于求解和值，可以使用一个登长的数组记录数组元素从左到右元素的依次加和。

这个居然花了我蛮多时间，我果然还是太菜了。

`Runtime: 16 ms, faster than 18.19% of C++ online submissions for Maximum Sum of Two Non-Overlapping Subarrays.`

`Memory Usage: 8.8 MB, less than 54.54% of C++ online submissions for Maximum Sum of Two Non-Overlapping Subarrays.`

```c++
class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& A, int L, int M) {
        int len = A.size(), ret = 0;
        vector<int> S(len+1);
        S[0] = 0;
        for(int i=0; i<len; i++) S[i+1] += S[i] + A[i];
        for(int i=L-1; i<len; i++){
            // before
            for(int j=M-1; j<i+1-L; j++) ret = max(ret, S[i+1]-S[i+1-L]+S[j+1]-S[j+1-M]);
            // after
            for(int j=i+M; j<len; j++) ret = max(ret, S[i+1]-S[i+1-L]+S[j+1]-S[j+1-M]);
        }
        return ret;
    }
};
```

BitBrave，2019-11-29
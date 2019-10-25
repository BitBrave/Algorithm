# LeetCode(\795. Number of Subarrays with Bounded Maximum)题解

We are given an array `A` of positive integers, and two positive integers `L` and `R` (`L <= R`).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least `L` and at most `R`.

```
Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
```

**Note:**

- L, R and `A[i]` will be an integer in the range `[0, 10^9]`.
- The length of `A` will be in the range of `[1, 50000]`.

## 解题思路

给一个正数数组A，以及两个L和R。现在从A中取出不同的子数组（子数组必须元素在A内连续），子数组内的元素之和必须在[L,R]区间内，问有多少种这样的子数组。

这个题可以使用简单的遍历，首先想如果A中某个位置的元素大于R，那么这个元素就将A分割成了两个子数组，在左边和右边分别找就可以了，更深入之后可以假设从左到右遍历，遇到一个值就这样判断：

我们维护一个值k记录一个位置，表示当前遍历到位置i-1时，和k之间的元素之和都小于等于R，同时记录这个结果值S，维护一个结果值ret，初始化S=i=k=ret=0。

- 我们寻找元素中连续子数组之和小于等于R的子数组个数。那么遍历到i时——

- 计算S+A[i]，如果小于等于R，就ret += i-k+1，i++。否则表示这个序列和不满足，就不断S -= S[k]，然后k++直到S + A[i]小于等于R，然后再执行ret += i-k+1，i++。如果直到k==i时都不满足，则直接k=i+1，i++，S=0。
- 这样走到最后，计算出数组中所有元素和小于等于R的连续子数组个数ret，这时候，再计算A中连续子树组元素之和小于L的个数，初始化S=i=k=0。
- 计算S+A[i]，如果小于L，就ret -= i-k+1，i++。否则表示这个序列和不满足，就不断S -= S[k]，然后k++直到S + A[i]小于L，然后再执行ret += i-k+1，i++。如果直到k==i时都不满足，则直接k=i+1，i++，S=0。
- 这样走到最后，就可以得到所有元素和在[L, R]的连续子数组的个数了。

代码如下，时间复杂度O(n)，因为从初始化开始k和i数一直在不断增大，最多增加N次，同时空间复杂度O(n)。

`Runtime: 36 ms, faster than 86.26% of C++ online submissions for Number of Subarrays with Bounded Maximum.`

`Memory Usage: 12.3 MB, less than 66.67% of C++ online submissions for Number of Subarrays with Bounded Maximum.`

```c++
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        int S = 0, k = 0, ret = 0, len = A.size();
        // <=R
        for(int i=0; i<len; i++){
            while(k<=i && S+A[i]>R) k++;
            ret += i - k + 1;
        }
        // <L
        S = k = 0;
        for(int i=0; i<len; i++){
            while(k<=i && S+A[i]>=L) k++;
            ret -= i - k + 1;
        }
        return ret;
    }
};
```

同时也可以优化到一个循环里去，如下。

```c++
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        int SL = 0, SR = 0, kr = 0, kl = 0, ret = 0, len = A.size();
        for(int i=0; i<len; i++){
            while(kr<=i && SR+A[i]>R) kr++;    // <=R   
            while(kl<=i && SL+A[i]>=L) kl++; // <L
            
            ret += kl - kr;
        }
        return ret;
    }
};
```

BitBrave,2019-10-25

- A[i]>R，表示这个元素不符合条件，i++，S=0，k=i+1
- A[i]==R，表示这个元素更好符合条件，但是只能组成一个单数组。i++，S=0，k=i+1，ret += 1
- A[i]<R，表示这个数组符合条件，并且可以和前面的元素组合形成多个子数组。计算Sum(A[k..i])的和，
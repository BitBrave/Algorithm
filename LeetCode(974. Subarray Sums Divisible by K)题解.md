# LeetCode(\974. Subarray Sums Divisible by K)题解

Given an array `A` of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by `K`.

 

**Example 1:**

```
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

 

**Note:**

1. `1 <= A.length <= 30000`
2. `-10000 <= A[i] <= 10000`
3. `2 <= K <= 10000`

## 解题思路

给一个数组，找出其中的连续子数组的数目，每个子数组元素之和可以被K整除。

这个最简单的办法就是遍历所有的子数组，然后判断是否可以被K整除，整体时间复杂度为O(n2)，肯定ETL了。

这个题需要分析一下，思考一下整除的条件是什么，就是余数为0，而数学中有这样一个性质。如果两个数对于一个除数同余，那么两个数只差一定能整除这个除数。即若a<=b，a%K==b%K，那么(b-a)%K=0。

因此这里我们可以采用如下解法：从左到右遍历数组，用一个Map记录数组中当前遍历的所有元素之和对于K的余数出现的次数，然后后续如果出现相同的余数，那么就代表前面有多个子连续数组之间的元素和是可以被整除的。

代码如下，时间复杂度O(n)，空间复杂度O(K)。

`Runtime: 76 ms, faster than 28.15% of C++ online submissions for Subarray Sums Divisible by K.`

`Memory Usage: 14 MB, less than 58.33% of C++ online submissions for Subarray Sums Divisible by K.`

```c++
class Solution {
public:
    int subarraysDivByK(vector<int>& A, int K) {
        int res = 0, s = 0, len = A.size();
        unordered_map<int, int> M;
        M[0] = 1;
        for (int i=0; i<len; i++) {
            s = (s + A[i]) % K;
            if (s < 0) s += K;
            if (M.find(s) == M.end()) M[s] = 1;
            else {
                res += M[s];
                M[s]++;
            }
        }
        return res;
    }
};
```

BitBrave, 2020-01-03
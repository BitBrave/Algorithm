# LeetCode(910. Smallest Range II)题解

Given an array `A` of integers, for each integer `A[i]` we need to choose **either x = -K or x = K**, and add `x` to `A[i] **(only once)**`.

After this process, we have some array `B`.

Return the smallest possible difference between the maximum value of `B` and the minimum value of `B`.

**Example 1:**

```
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
```

**Example 2:**

```
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
```

**Example 3:**

```
Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
```

**Note:**

1. `1 <= A.length <= 10000`
2. `0 <= A[i] <= 10000`
3. `0 <= K <= 10000`

## 解题思路

给一个数组A和整数K，对A数组中每个数进行+K或-K的操作，最终形成一个新的数组B。求一个特定的数组B，其中最大的元素和最小的元素之间的差值在所有可以由A形成的B数组中最小。

（这题花了我好多时间）

想了很多，但是都没成功。这里放上网上查到的东西。真的是佩服。其实首先就是将+ -变成加或者不加，就是首先将A全体减去K，然后题目就变成了A中一些数加上2*K，一些不变，然后求最小的最大减去最小的差值。

不妨先把所有元素排序并减去`K`。这样，原问题就转化为，需要选出一部分元素加上`2*K`，另一部分元素不变。显然，为了缩小最大值和最小值的差值，应该选择较小的元素加上`2*K`。

可以证明，需要加上`2*K`的元素是数组中从左侧（最小的元素）开始的连续元素。这一点可以这样说明：

- 假如最优解中有至少一个元素增加了`2*K`（`B[i] = A[i] + 2*K`），且它的左侧有一个不变的元素（`B[j] = A[j]`），那么由于`A[j] < A[i]`，令`B[j] = A[j] + 2*K`不会使`B`数组的最大值变化，但却有可能使`B`数组的最小值增大，情况不会变的更糟；
- 假如最优解中有至少一个元素不变（`B[i] = A[i]`），且它的右侧有一个增加了`2*K`的元素（`B[j] = A[j] + 2*K`），那么由于`A[j] > A[i]`，令`B[j] = A[j]`不会使`B`数组的最小值变化，但却有可能使`B`数组的最大值减小，情况也不会变的更糟

综上，总存在一个只有从左侧开始的连续元素才加了`2*K`的最优解。我觉得这个证明的思路很像贪心；这大概也可以算是一种贪心算法？

所以我们可以把元素扫描一遍，对于每个元素，计算“当它是增加的最末一个元素”时的差值，并在这些差值里求最小值。对于`A[i]`，这个差值为`max(A[N-1], A[i] + 2*K) - min(A[i+1], A[0] + 2*K)`。



代码如下，时间复杂度O(NlogN)，空间复杂度O(1)。

`Runtime: 32 ms, faster than 52.49% of C++ online submissions for Smallest Range II.`

`Memory Usage: 9.8 MB, less than 100.00% of C++ online submissions for Smallest Range II.`

```c++
class Solution {
public:
    int smallestRangeII(vector<int>& A, int K) {
        int len = A.size(), ret;
        K = abs(K);
        sort(A.begin(), A.end());
        
        ret = A[len-1] - A[0];
        for(int i=0; i<len-1; i++){
            ret = min(ret, max(A[i]+2*K, A[len-1]) - min(A[0]+2*K, A[i+1]));
        }
        
        return ret == INT_MAX ? 0 : ret;
    }
};
```

BitBrave，2019-11-11
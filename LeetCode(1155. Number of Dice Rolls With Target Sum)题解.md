# LeetCode(\1155. Number of Dice Rolls With Target Sum)题解

You have `d` dice, and each die has `f` faces numbered `1, 2, ..., f`.

Return the number of possible ways (out of `fd` total ways) **modulo `10^9 + 7`** to roll the dice so the sum of the face up numbers equals `target`.

 

**Example 1:**

```
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
```

**Example 2:**

```
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
```

**Example 3:**

```
Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
```

**Example 4:**

```
Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
```

**Example 5:**

```
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
```

 

**Constraints:**

- `1 <= d, f <= 30`
- `1 <= target <= 1000`

## 解题思路

给三个数d，f和target。可以理解为现在有d堆石子，每一堆有f个石子。现在从每堆石子中选一些石子，最后总的数目为target，问一共有多少种选择方案。

这个题可以使用DP问题求解。设定一个(d) \* (target+1)的二维数组D。其中D(i,t)表示选定序号0~i的石子堆时，选定方案中石子总和为t的方案数，每一堆必须至少选一个。那么最后的题目的答案就是D(d, target)。

那么如何填充这个数组呢，首先是普遍的状态转移方程。

- D(i, t) = D(i-1, t-1) + D(i-1, t-2) + ... + D(i-1, t-f)。表示D(i, t)的解就是我之前的方案基础上，在第i堆石子上选0,1,2···f个石子，来组成新的和为t的方案。因此这里不能出现负数，如果t比较小，表示一堆石子其实就可以满足方案，那么不能在第i堆中选超过t的石子，因此t-f>=0.

其次就是基础赋值计算了，比如，如果t=0，表示不选石子，那么不管多少堆石子（堆数>=1），最后的答案都只是0种，不存在解决方案。因此D(i,0)=0 (i=0,1,2,...,d-1)。同时如果i=0，表示只有一堆石子，那么target小于等于f时，对应的方案只有一种，如果大于f就为0，因为不存在解决方案。

注意需要取余数。

代码如下，时间复杂度O(d\*f\*target)，时间复杂度O(d\*target)。

`Runtime: 36 ms, faster than 37.21% of C++ online submissions for Number of Dice Rolls With Target Sum.`

`Memory Usage: 10.7 MB, less than 100.00% of C++ online submissions for Number of Dice Rolls With Target Sum.`

```c++
class Solution {
public:
    int numRollsToTarget(int d, int f, int target) {
        vector<vector<int>> ret(d, vector<int>(target+1, 0));
        int mft = min(target, f), mod = pow(10, 9) + 7;
        for (int j=1; j<=mft; j++) ret[0][j] = 1;

        for (int i=1; i<d; i++) {
            for (int t=1; t<=target; t++){
                mft = min(t, f);
                ret[i][t] = 0;
                for (int j=1; j<=mft; j++) ret[i][t] = (ret[i][t] + ret[i-1][t-j]) % mod;
            }
        }
        return ret[d-1][target];
    }
};
```

这个算法是可以优化的，观察可以知道二维数组是每次更新只用到了上一行，同时求和也只用到了上一行的固定位置的的数，因此时间复杂度可以降到O(d\*target)，空间复杂度降到O(target)。这里给出优化时间复杂度的算法。代码如下。

`Runtime: 8 ms, faster than 93.92% of C++ online submissions for Number of Dice Rolls With Target Sum.`

`Memory Usage: 10.7 MB, less than 100.00% of C++ online submissions for Number of Dice Rolls With Target Sum.`

```c++
class Solution {
public:
    int numRollsToTarget(int d, int f, int target) {
        vector<vector<int>> ret(d, vector<int>(target+1, 0));
        int mft = min(f, target), mod = pow(10, 9) + 7;
        for (int j=1; j<=mft; j++) ret[0][j] = 1;

        for (int i=1; i<d; i++) {
            long lsum = 0;
            for (int t=1; t<=target; t++){
                if (t > f) lsum = (lsum - ret[i-1][t-f-1] + ret[i-1][t-1] + mod) % mod;
                else lsum = (lsum + ret[i-1][t-1]) % mod;
                
                ret[i][t] = lsum;
            }
        }
        return ret[d-1][target];
    }
};
```

BitBrave，2019-12-17
# LeetCode(\264. Ugly Number II)题解

Write a program to find the `n`-th ugly number.

Ugly numbers are **positive numbers** whose prime factors only include `2, 3, 5`. 

**Example:**

```
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
```

**Note:** 

1. `1` is typically treated as an ugly number.
2. `n` **does not exceed 1690**.

## 解题思路

寻找第N个丑陋数，丑陋数的定义就是1和因子只有2,3,5,的整数。

最暴力的解法就是从1开始不断遍历，判断当前数是不是丑陋数，直到找到第N个。但是这样会超时，因为有很多冗余的操作，很多数不是丑陋数。

这个题给出了很多hint，通过分析可以发现丑陋数的出现是可以计算出来的：假设我们现在从1开始已经依次从小到大有了M个丑陋数，那么如何计算出第M+1个丑陋数呢？我们可以把当前所有元素都分别乘2、乘3、乘5，然后取所有的值中，比当前第M个丑陋数大的最小的值。

但是其实我们不必将所有的数都乘上2,3,5，只需要找到最小的乘以2，3,5的大于当前丑陋数的几个数，然后取乘之后的三个值中的最小的值即可。然后将最小值对应地原始的丑陋数所在位置更新一下即可。

代码如下，时间复杂度O(N)，空间复杂度O(N)。

`Runtime: 8 ms, faster than 75.06% of C++ online submissions for Ugly Number II.`

`Memory Usage: 9.8 MB, less than 100.00% of C++ online submissions for Ugly Number II.`

```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> ret(n, 1);
        int i2 = 0, i3 = 0, i5 = 0;
        for(int i=1; i<n; i++){
            ret[i] = min(ret[i2]*2, min(ret[i3]*3, ret[i5]*5));
            if(ret[i] == ret[i2]*2) i2++;
            if(ret[i] == ret[i3]*3) i3++;
            if(ret[i] == ret[i5]*5) i5++;
        }
        return ret[n-1];
    }
};
```

BitBrave，2019-12-04
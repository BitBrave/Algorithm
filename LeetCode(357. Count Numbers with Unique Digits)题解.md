# LeetCode(\357. Count Numbers with Unique Digits)题解

Given a **non-negative** integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

**Example:**

```
Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
```

## 解题思路

给出一个数n，求所有的在\[0, 10^n\)之间的每个位置上的数都不一样的数的个数。

这个题是一个简单的DP问题，当然也可以思考为一个数学的推理组合问题。n就是表示数的位数，我们首先计算书长度为K的所有数字中有多少个每个位置都不一样的数。首先K=1，有10种选择，K等于2时，十位上有9中选择，然后十位上选定之后个位上也就只有9种选择了。相应的K=3时，千位上9种，十位上9种，然后各位只能有8种，以此类推，K个数字时，如果K=1，那么合法数个数为10。K>1时，合法数个数为，9\*9\*8\*...\*(9-K+2)。最后将1到K为的数加起来即可。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Count Numbers with Unique Digits.`

`Memory Usage: 8.2 MB, less than 83.33% of C++ online submissions for Count Numbers with Unique Digits.`

```c++
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int ret = 0, mul = 9;
        n = min(10, n);
        if(n == 0) return 1;
        ret = 10;
        for(int i=2; i<=n; i++){
            mul *= 9 - i + 2;
            ret += mul;
        }
        return ret;
    }
};
```

BitBrave，2019-12-12
# LeetCode(\343. Integer Break)题解

Given a positive integer *n*, break it into the sum of **at least** two positive integers and maximize the product of those integers. Return the maximum product you can get.

**Example 1:**

```
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

**Example 2:**

```
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

**Note**: You may assume that *n* is not less than 2 and not larger than 58.

## 解题思路

给出一个数，将其拆分为不同的数之和，同时保证所有的数的乘积最大。

这个题是一个典型的DP问题，优化之后可以在O(1)的时间内计算出来。因为我们只需要将所有的值都化为3\*3\*3\*...就可以得到最大值，当然最后如果是余下4就不再变为1和3了。

如何证明这个是最优的呢，我们可以假设目前有一个最优的解，a,b,c,...。其中肯定不存在为1的数（原因不证自明），如果其中存在数大于4，比如b那么可以证明3*(b-3)>b。因此可以进一步划分出3来，出现矛盾。因此，最优解中的元素一定是小于等于4.

而4元素和2元素其实是一样的，一个4可以化为两个2.因此我们要比较的就是将数按照3拆分和按2拆分的区别了。这就需要比较2^(n/2)和3^(n/3)。这是一个数学比较，可以发现后者更大。

因此直接将数按照3进行分割就可以了。

代码如下，时间复杂度O(1)，空间复杂度O(1)。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Integer Break.`

`Memory Usage: 8.2 MB, less than 100.00% of C++ online submissions for Integer Break.`

```c++
class Solution {
public:
    int integerBreak(int n) {
        if(n <= 4) return n/2 * (n-n/2);
        int c = n / 3, m = n % 3;
        if(m == 1){
            m = 4;
            c--;
        }
        else if(m == 0) m = 1;
        return pow(3, c)
    }
};
```

BitBrave，2019-12-06
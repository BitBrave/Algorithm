# LeetCode(\\1017. Convert to Base -2)题解

Given a number `N`, return a string consisting of `"0"`s and `"1"`s that represents its value in base `**-2**` (negative two).

The returned string must have no leading zeroes, unless the string is `"0"`.

 

**Example 1:**

```
Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
```

**Example 2:**

```
Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
```

**Example 3:**

```
Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
```

 

**Note:**

1. `0 <= N <= 10^9`

## 解题思路

给一个数，写出按照-2进制表示的数的字符串。

这个题稍微分析一下就可以，-2进制和2进制其实没有太大的区别，把-2进制的奇数位和前面一个偶数位都设为1就和2进制的对应奇数位设置为1一样。我们首先依次查看数N的最后一个数，然后看如果对应的进制为是偶数，那就和2进制没什么分别，如果是奇数，就当前为设为1。同时样判断进位。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 4 ms, faster than 58.15% of C++ online submissions for Convert to Base -2.`

`Memory Usage: 8.3 MB, less than 100.00% of C++ online submissions for Convert to Base -2.`

```c++
class Solution {
public:
    string baseNeg2(int N) {
        if (N == 0) return "0";
        if (N == 1) return "1";
        string ret = "";
        bool even = true;
        int a = 0, b = 0;
        while(N > 0){
            a = (N & 1) + b;
            b = 0;
            N = N >> 1;
            
            if (a == 0) ret = "0" + ret;
            else if (a == 1) {
                if (even == true) ret = "1" + ret;
                else {
                    ret = "1" + ret;
                    b = 1;
                }
            } 
            else if (a == 2) {
                ret = "0" + ret;
                b = 1;
            }
            even = !even;
        }
        if (b == 1){
            if (even) ret = "1" + ret;
            else ret = "11" + ret;
        } 
        return ret;
    }
};
```

BitBrave，2019-12-14
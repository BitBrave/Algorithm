# LeetCode(69. Sqrt(x))题解
------
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

    Input: 4
    Output: 2
Example 2:

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since 
                the decimal part is truncated, 2 is returned.

## 解题思路

求一个数的平方根，如果是小数就返回整数部分。

超简单，直接使用STL就可以。

代码如下：

Runtime: 4 ms, faster than 93.46% of C++ online submissions for Sqrt(x).
Memory Usage: 8.3 MB, less than 51.55% of C++ online submissions for Sqrt(x).

```c++
class Solution {
public:
    int mySqrt(int x) {
        return sqrt(x);
    }
};
```

或者可以自己写一个。

代码如下：

Runtime: 84 ms, faster than 5.82% of C++ online submissions for Sqrt(x).
Memory Usage: 8.3 MB, less than 51.24% of C++ online submissions for Sqrt(x).

```c++
class Solution {
public:
    int mySqrt(int x) {
        int res = 1;
        while(x / res >= res) res++;
        return res - 1;
    }
};
```

BitBrave, 2019-06-06
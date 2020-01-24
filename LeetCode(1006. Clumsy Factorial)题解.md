# LeetCode(\1006. Clumsy Factorial)题解

Normally, the factorial of a positive integer `n` is the product of all positive integers less than or equal to `n`. For example, `factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1`.

We instead make a *clumsy factorial:* using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, `clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1`. However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is *floor division* such that `10 * 9 / 8` equals `11`. This guarantees the result is an integer.

`Implement the clumsy` function as defined above: given an integer `N`, it returns the clumsy factorial of `N`.

 

**Example 1:**

```
Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1
```

**Example 2:**

```
Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
```

 

**Note:**

1. `1 <= N <= 10000`
2. `-2^31 <= answer <= 2^31 - 1` (The answer is guaranteed to fit within a 32-bit integer.)



## 解题思路

给一个数N，然后每个序列N,N-1,N-2,...,1，使用*/+-这几个运算符依次填充到序列中，按照序列运算的优先级计算，给出最后的结果。

这个题可以直接计算就好，为了可以有效递归，我们可以首先计算N，N-1，N-2的值，然后剩下的数就是依次4个计算之后进行相加。

代码如下，时间复杂度O(N)，空间复杂度O(1)。

`Runtime: 8 ms, faster than 11.39% of C++ online submissions for Clumsy Factorial.`

`Memory Usage: 8.8 MB, less than 20.00% of C++ online submissions for Clumsy Factorial.`

```c++
class Solution {
public:
    int clumsy_(int N) {
        if (N < 4) return min(1, N);
        return N - (N-1) * (N-2) / (N-3) + clumsy_(N-4);
    }
    int clumsy(int N) {
        if (N <= 2) return N;
        else if (N == 3) return 6;
        return N * (N-1) / (N-2) + clumsy_(N-3);
    }
};
```

BitBrave，2020-01-24
# LeetCode(\991. Broken Calculator)题解

On a broken calculator that has a number showing on its display, we can perform two operations:

- **Double**: Multiply the number on the display by 2, or;
- **Decrement**: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number `X`.

Return the minimum number of operations needed to display the number `Y`.

 

**Example 1:**

```
Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
```

**Example 2:**

```
Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
```

**Example 3:**

```
Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
```

**Example 4:**

```
Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.
```

 

**Note:**

1. `1 <= X <= 10^9`
2. `1 <= Y <= 10^9`

## 解题思路

这个题的意思就是，给你两个数，X和Y，现在针对X进行两个操作，加倍或者-1，可以使得X变成Y的最少的操作次数是多少？

这个题从X变成Y有很多条路径，很难进行计算。但是我们可以换个思路，最优的方案中，从X变成Y和从Y按照相反的操作变为X是一样的次数。而Y的变化经过分析之后得到，变换是唯一的。

对应的，如果对Y操作，那就是Y可以除以2或者+1。那么：

- Y如果小于X，Y只能+1.
- Y等于X，算法结束。
- Y>X时，如果Y为奇数，Y只能+1。如果为偶数，Y可以+1，+1两次之后除以2，但是不管如何，都比Y直接除2再+1的操作次数要多。因此Y只能除以2。
- 以上

代码如下，时间复杂度为因为不断的除2操作，所以为O(log(Y-X))，空间复杂度O(1)。

`Runtime: 4 ms, faster than 56.60% of C++ online submissions for Broken Calculator.`

`Memory Usage: 8.3 MB, less than 40.00% of C++ online submissions for Broken Calculator.`

```c++
class Solution {
public:
    int brokenCalc(int X, int Y) {
        if(Y <= X) return X - Y;
        if(Y & 1) return brokenCalc(X, Y + 1) + 1;
        return brokenCalc(X, Y / 2) + 1;
    }
};
```

或者使用非递归模式

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Broken Calculator.`

`Memory Usage: 8.1 MB, less than 100.00% of C++ online submissions for Broken Calculator.`

```C++
class Solution {
public:
    int brokenCalc(int X, int Y) {
        int ret = 0;
        while(Y > X){
            ret++;
            if(Y & 1) Y++;
            else Y /= 2;
        }
        return ret + abs(X - Y);
    }
};
```

BitBrave，2019-12-2
# LeetCode(70. Climbing Stairs)题解
------
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

## 解题思路

Easy, 给一个N代表N个阶梯，一次可以爬一步或者两步，请问一共有多少种爬楼梯的方式。

这是一个典型的DP，假设有一个数组，D，D[i]表示到达第i步阶梯有几种方式，那么往回看就有，D[i] = D[i-1] + D[i-2]，表示最后一步是通过走一步和走两步的总数的，这就是最优子结构。D[0] = D[1] = 1; 再看一下，这其实就是斐波那契数列！！！但是千万不要写递归，这样绝对会超时的。因为有太多的子树。

代码如下：

Runtime: 4 ms, faster than 85.73% of C++ online submissions for Climbing Stairs.
Memory Usage: 8.2 MB, less than 79.25% of C++ online submissions for Climbing Stairs.

```c++
class Solution {
public:
    int climbStairs(int n) {
        int fore = 0, back = 1;
        for(int i=0; i<n; i++){
            fore = back + fore;
            swap(fore, back);
        }
        return back;
    }
};
```

BitBrave, 2019-06-06
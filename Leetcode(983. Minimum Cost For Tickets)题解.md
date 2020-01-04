# Leetcode(\983. Minimum Cost For Tickets)题解

In a country popular for train travel, you have planned some train travelling one year in advance. The days of the year that you will travel is given as an array `days`. Each day is an integer from `1` to `365`.

Train tickets are sold in 3 different ways:

- a 1-day pass is sold for `costs[0]` dollars;
- a 7-day pass is sold for `costs[1]` dollars;
- a 30-day pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel. For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of `days`.

 

**Example 1:**

```
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
```

**Example 2:**

```
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
```

 

**Note:**

1. `1 <= days.length <= 365`
2. `1 <= days[i] <= 365`
3. `days` is in strictly increasing order.
4. `costs.length == 3`
5. `1 <= costs[i] <= 1000`

## 解题思路

在一个因火车旅行而闻名的国家，一个人将一年中要旅行的日子以数组天数给出。每天是编号1到365之间的整数。火车票以3种不同的方式出售：1天车票的售价为costs[0]美元；7天的车票售价为成本costs[1]美元；30天的车票售价为costs[2]美元。通票允许连续几天旅行。例如，如果我们在第2天获得7天通行证，那么我们可以旅行7天：第2、3、4、5、6、7和8天。在给定的日期列表中，返回需要旅行的最少美元数。注意给出的旅行的天数编号是递增的。

这个题在知道了用DP解决的时候，我还是想了好久，最后给出了一个我看来很复杂的解法，但是还是失败了。于是看了网上的解法，这里给出自己的理解。

方法是我们用一个366长度的数组dp，dp\[i\]表示1到i天中旅行的最少花费。那么因为旅行的天数序列肯定小于等于365的，所以直接返回dp\[365\]即可。

那么如何填充这个数组呢，也就是状态转移方程是什么，dp\[i\]是怎么计算得来的。

我们可以这样想，如果第i天不旅行也就是数组中没有给出这一天，那么这一天不用花钱，dp\[i\] = dp\[i-1\]。如果旅行，那么第i天使用的票只有三种方式，1天，7天和30天。这三种票的方式要么现场买，要么前面几天里买好了第i天是连续着享受的，而前面要花费少的话，就是尽可能提前已经买了的。因此我们选dp\[i-1\]+costs\[0\],dp\[i-7\]+costs\[1\], dp\[i-30\]+costs\[2\] 中的较小值就可以了。

注意数组越界问题，主要是左边越界，越界时要取0.

代码如下，时间复杂度O(366)，空间复杂度O(365)。

`Runtime: 4 ms, faster than 79.28% of C++ online submissions for Minimum Cost For Tickets.`

`Memory Usage: 8.8 MB, less than 75.00% of C++ online submissions for Minimum Cost For Tickets.`

```c++
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        vector<int> dp(366, 0);
        for (int d : days) dp[d] = INT_MAX;
        //dp[0] = 0;

        for (int i=1; i<366; i++) {
            if (dp[i] == 0) dp[i] = dp[i-1];
            else {
                dp[i] = min(dp[i - 1] + costs[0], min(dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2]));
            }
        }
        return dp[365];
    }
};
```

还有一种方法是时间复杂度O(n)，就是判断给定的天数里面相差的条件，直接填充dp\[i\]，只不过代码复杂一点，这里就不写了。链接在此<https://blog.csdn.net/mike_learns_to_rock/article/details/86669196>

BitBrave，2020-1-4
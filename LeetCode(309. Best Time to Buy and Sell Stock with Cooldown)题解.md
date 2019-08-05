# LeetCode(309. Best Time to Buy and Sell Stock with Cooldown)题解
------
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

    Input: [1,2,3,0,2]
    Output: 3 
    Explanation: transactions = [buy, sell, cooldown, buy, sell]

## 解题思路
给一个数组P，每个元素表示当天的股票交易价格。现在每天可以买入和卖出一只股票，但卖出必须在买入之后，同一时间内最多只能持有一只股票。且卖出之后必须至少隔一天才能买入。求出能得到的最大的收益。

这个题很明显的可以使用DP进行解决。有时候DP有一个状态转移方程，很难想出来。这个可以用状态图。参考<https://www.cnblogs.com/jdneo/p/5228004.html>

这里我用了一个稍微改变的。使用与数组等长的数组A，B。A[i]表示在第i天持有股票的情况下得到的最大收益，B[i]表示在第i天不持有股票的情况下得到的最大收益。最终的结果就是B[P.size-1]。

那么如何来填充这个数组呢？首先是A[i],持有股票可以由两种情况产生，今天买了股票，或者前几天买了但还没卖。这样因为买股票必须隔一天，即max(B[i-2]-P[i], A[i-1]). 然后是B[i]，不持有股票同样是两种情况，今天卖了股票，或者前几天就卖了的。即max(A[i-1]+P[i], B[i-1]).

注意要初始化，A[0]=-P[0], B[0]=0. A[1]=max(-P[0], -P[1]), B[1]=max(0, P[1]-P[0]). 随后就使用状态转移即可。
最终得到结果。时间复杂度和空间复杂度均为O(n)

代码如下：

Runtime: 4 ms, faster than 76.60% of C++ online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 8.6 MB, less than 98.95% of C++ online submissions for Best Time to Buy and Sell Stock with Cooldown.

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        if(len<=1) return 0;
        vector<int> A(len, 0), B(len, 0);
        A[0] = -prices[0]; B[0] = 0;
        A[1] = max(-prices[0], -prices[1]); B[1]=max(0, prices[1]-prices[0]);
        for(int i=2; i<len; i++){
            A[i] = max(B[i-2]-prices[i], A[i-1]);
            B[i] = max(B[i-1], A[i-1]+prices[i]);
        }
        return B[len-1];
    }
};
```

BitBrave, 2019-08-05
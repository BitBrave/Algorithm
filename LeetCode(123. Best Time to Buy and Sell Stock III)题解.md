# Leetcode(123. Best Time to Buy and Sell Stock III)题解
------
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

    Input: [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
                Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

## 解题思路
给一个数组记录一个股票每天的价格，每个元素代表当天的股价。现在要求最多发生两次交易（可以少于两次），求得可以得到的最大收益。

这个题可以使用DP的方式得到。我们将数组拆分为两半。左边发生最多1次交易，右边发生最多一次交易,发生一次交易的算法可以用DP在O(n)内得到。然后二次的收益相加计算。每次分两半一共需要总的时间为O(n2). 最后选择最大分割方法。

这其实是可以优化的。我们用两个数组分别记录左边到右边发生最多1次交易的情况下得到的收益，数组分别长n+1. Left[i]表示从第1到i天内最多一次交易下的最大收益，i=0表示左边不交易。Right[j]表示从第j+1天到n天内最多一次交易下的最大收益，j=n表示右边不交易。这两个数组可以使用简单的DP得到。选择Max(Left[i]+Right[i]). 总的时间复杂度为O(n).

代码如下：

Runtime: 8 ms, faster than 83.96% of C++ online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 9.8 MB, less than 41.95% of C++ online submissions for Best Time to Buy and Sell Stock III.

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0, n = prices.size();
        if(n <= 1) return res;
        
        int premin = prices[0], m = 0;
        vector<int> Left(n+1, 0), Right(n+1, 0);
    
        for(int i=1; i<n; i++){
            Left[i+1] = max(m, prices[i]-premin);
            premin = min(premin, prices[i]);
            m = max(m, Left[i+1]);
        }
        premin = prices[n-1], m = 0;
        for(int i=n-2; i>=0; i--){
            Right[i] = max(m, premin - prices[i]);
            premin = max(premin, prices[i]);
            m = max(m, Right[i]);
        }
        res = Left[0]+Right[0];
        for(int i=1; i<n; i++) res = max(res, Left[i]+Right[i]);
        return res;
    }
};
```

BitBrave, 2019-07-04
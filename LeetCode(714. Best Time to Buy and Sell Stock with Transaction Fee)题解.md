# LeetCode(714. Best Time to Buy and Sell Stock with Transaction Fee)题解
------

## 解题思路

给出一系列的股票交易价格，每次股票交易会有交易fee，求买卖股票能获得的最大的收益。

可以使用DP，使用res[i][0]表示第i天未持有股票下的最大收益，而res[i][1]表示第i天持有股票下的最大收益。则状态转移方程如下：

res[i][0] = max(res[i-1][0], res[i-1][1]+prices[i]);
res[i][1] = max(res[i-1][1], res[i-1][0]-prices[i]-fee);

时间复杂度O(n), 空间复杂度O(n).

代码如下：

Runtime: 224 ms, faster than 5.37% of C++ online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage: 50.9 MB, less than 5.88% of C++ online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int len = prices.size();
        if(len == 0) return 0;
        vector<vector<int>> res(len, vector<int>(2, 0));
        res[0][1] = -prices[0] - fee;
        for(int i=1; i<len; i++){
            res[i][0] = max(res[i-1][0], res[i-1][1]+prices[i]);
            res[i][1] = max(res[i-1][1], res[i-1][0]-prices[i]-fee);
        }
        return res[len-1][0];
    }
};
```

优化，这里可以进行优化，可以看到，res中每次值只与上一个值状态有关，使用res0表示res[i]0, 使用res1表示res[i][1]. 优化如下。

时间复杂度O(n), 空间复杂度O(1).

代码如下：

Runtime: 140 ms, faster than 64.38% of C++ online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage: 14.9 MB, less than 100.00% of C++ online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int len = prices.size();
        if(len == 0) return 0;
        int res0 = 0, res1 = -prices[0] - fee;
        int tmp;
        for(int i=1; i<len; i++){
            tmp = max(res0, res1+prices[i]);
            res1 = max(res1, res0-prices[i]-fee);
            res0 = tmp;
        }
        return res0;
    }
};
```

BitBrave，2019-08-22
# LeetCode(322. Coin Change)题解
------
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

    Input: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1
Example 2:

    Input: coins = [2], amount = 3
    Output: -1
    Note:
    You may assume that you have an infinite number of each kind of coin.

## 解题思路

给一串数表示每个硬币的面值，每个硬币假设有无限个，从中找出可以组成给定面值的最小的硬币个数，返回其数目，否则返回-1.

这个题明显用DP求解。但是状态转移方程有点难想，还是那句话，先从最简单的着手。假设硬币的面额有n种，第i种的面额为n[i]。需要凑齐的面额为m。

我们用一个数组D[n][m]来进行状态方程的转移记录，初始化都为inf。其中D[i][j]表示在n[1-i]中凑齐面额为j的需要的最小的硬币数。如果凑不齐，就令D[i][j]=inf。那么最终结果就是D[n][m]。

如何书写状态转移方程呢？假设要填充D[i][j], 那么有如下几种情况：

不选择n[i]硬币，D[i][j] = D[i-1][j].

选择了一枚或者多枚n[i]硬币，D[i][j] = D[i][j-n[i]].

那么D[i][j] = min(D[i-1][j], D[i][j-n[i]]).

优化策略

这里可以看到，每次更新D[i][j]的时候，其实只用到了i-1行的数据，因此，可以将D[n][m]变为一个D[2][m]的数组。

更进一步，D[i][j]更新使用的D[i-1][j]只表示上一个状态，因此，可以将D[2][m]直接变为D[m]初始化D[0]=0, 表示0面额需要0个硬币。

最终时间复杂度O(mn)，空间复杂度O(m)

代码如下:

Runtime: 48 ms, faster than 65.50% of C++ online submissions for Coin Change.
Memory Usage: 12.6 MB, less than 82.35% of C++ online submissions for Coin Change.

```c++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int len = coins.size();
        if(len == 0) return amount == 0 ? 0:-1;
        vector<int> res(amount+1, INT_MAX);
        res[0] = 0;
        for(int i=0; i<len; i++){
            for(int j=0; j<=amount; j++){
                if(j-coins[i]>=0) res[j] = min(res[j], 1 + (res[j-coins[i]]==INT_MAX ? INT_MAX-1 : res[j-coins[i]]));
            }
        }
        return res[amount] == INT_MAX ? -1 : res[amount];
    }
};
```

BitBrave, 2019-08-19

# LeetCode(\1140. Stone Game II)题解

Alex and Lee continue their games with piles of stones. There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`. The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first. Initially, `M = 1`.

On each player's turn, that player can take **all the stones** in the **first** `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

 

**Example 1:**

```
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
```

 

**Constraints:**

- `1 <= piles.length <= 100`
- `1 <= piles[i] <= 10 ^ 4`

## 解题思路

给一堆石子，每堆石子有对应的石子数，A和L轮流选X堆，A先选。然后1<=X<=2M，然后更新M=max(M, X)，初始化M=1。两个人都使用最优的办法，那么问A能得到最多的石子是多少。

这个题我觉得难度挺大的，是网上参考了解法解决的。

### 解法一：记忆化递归，DFS

我们假设一个函数dfs(i，M)来表示第一个选的人从第i堆石子开始，可选堆数为1和2M时，能得到的最大石子数。那么第二个先选的人就只能得到第i堆开始的剩余石子总数-函数返回值了。对于A来说，我们直接调用dfs(0,1)即可。那如何构建dfs呢，首先从第i堆开始选，我们可以遍历1到2M，假设依次选定X堆，那么能得到的最大数就是max(sum[i:]-dfs(i+X, max(X, M)))。这就可以将问题变为子问题了。

同时，因为子问题有很多重复的，因此我们可以记住一些子问题的固定解，避免重复计算。使用一个map，索引为i，开始选石子的堆数位置，然后val也是一个map，索引是此时的M值，然后val是对应的结果。

代码如下，时间复杂度O(n3)，空间复杂度O(n2)，因为M的值肯定不会超过n/2（n为石子堆数），因为如果等于n/2时，选的人肯定就直接将剩下的石子全部拿了。

`Runtime: 52 ms, faster than 9.79% of C++ online submissions for Stone Game II.`

`Memory Usage: 10.3 MB, less than 100.00% of C++ online submissions for Stone Game II.`

```c++
class Solution {
    int len;
    vector<int> acum;
    vector<int> p;
    unordered_map<int, unordered_map<int, int>> M;
public:
    int dfs(int sta, int m){
        if (sta >= len) return 0;
        if(M.find(sta) != M.end() and M[sta].find(m) != M[sta].end()) return M[sta][m];
        M[sta][m] = 0;
        for(int x=1; x<=2*m; x++){
            M[sta][m] = max(M[sta][m], acum[len]-acum[sta]-dfs(sta+x, max(m, x)));
        }
        return M[sta][m];
    }
    
    int stoneGameII(vector<int>& piles) {
        len = piles.size();
        acum = vector<int>(len + 1, 0);
        p = piles;
        
        for (int i=0; i<len; i++) acum[i+1] += acum[i] + piles[i];
        
        return dfs(0, 1);
    }
};
```

### 解法二：动态规划

一般来说，解决同样一个问题，递归总是要比非递归函数花费更多的时间。将上面的记忆化递归也就是自顶向下改变成自底向上，就可以变成DP问题了。

我们设定一个二维数组D，其中D\[i\]\[j\]表示从第i堆石子开始选，初始化为m=j的时候，第一个选的人能得到的最多的石子。那么状态转移方程则如下。

D\[i\]\[j\] = max(D\[i, j\], acum\[len\]-acum\[i\]-D\[i+x]\[max(m,i)\]); 1<= x <=m; 注意判断是否越界，如果i+x或者max(m,i)越界，就直接break。

分析可知，我们是直接从最后边计算，当M=1时。结果则直接返回D\[0\]\[1\]即可。

代码如下，时间复杂度O(n3)，空间复杂度O(n2)，因为M的值肯定不会超过n/2（n为石子堆数），因为如果等于n/2时，选的人肯定就直接将剩下的石子全部拿了。

`Runtime: 12 ms, faster than 54.62% of C++ online submissions for Stone Game II.`

`Memory Usage: 9 MB, less than 100.00% of C++ online submissions for Stone Game II.`

```c++
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int len = piles.size();
        vector<int> acum = vector<int>(len + 1, 0);
        vector<vector<int>> D(len+1, vector<int>(len+1, 0));
        
        for (int i=0; i<len; i++) acum[i+1] += acum[i] + piles[i];
            for (int j=len; j>=0; j--){
                for (int i=len-1; i>=0; i--){
                for(int x=1; x <= 2*j; x++){
                    if (i+x > len) break;
                    else D[i][j] = max(D[i][j], acum[len]-acum[i]-D[i+x][max(j, x)]);
                }
            }
        }
        
        return D[0][1];
    }
};
```



BitBrave，2019-12-14
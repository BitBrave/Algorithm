# LeetCode(64. Minimum Path Sum)题解
------
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

    Input:
    [
    [1,3,1],
    [1,5,1],
    [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.

## 解题思路
Medium，给一个矩阵D，每个值非负，从左上走到右下，只能向下或向右，求出最短的路线的值（走过的点的值之和）。

还是使用DP，用一个矩阵M，给一个m*n大小，每个位置记录走到当前位置有的最短值。则位置i，j处的最优子结构为：M[i][j] = D[i][j] + min(M[i-1][j] + M[i][j-1]).

这里同样可以使用一个m*2的数组降低内存，更丧心病狂的就是直接在给定的矩阵上改变就行了，不用申请新的内存。

代码如下：

Runtime: 8 ms, faster than 97.16% of C++ online submissions for Minimum Path Sum.
Memory Usage: 10.4 MB, less than 93.98% of C++ online submissions for Minimum Path Sum.

```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = grid.size();
        if(row == 0) return 0;
        int col = grid[0].size();
        if(col == 0) return 0;
        
        for(int i=1; i<row; i++) grid[i][0] += grid[i-1][0]; // col
        for(int j=1; j<col; j++) grid[0][j] += grid[0][j-1]; // row
        
        for(int i=1; i<row; i++){
            for(int j=1; j<col; j++) grid[i][j] += min(grid[i][j-1], grid[i-1][j]);
        }
        return grid[row-1][col-1];
    }
};
```

BitBrave, 2019-06-04
# LeetCode(63. Unique Paths II)题解
------
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?


![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

    Input:
    [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
    Output: 2
    Explanation:
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

## 解题思路
Medium，是在62题基础之上的一个变种，就是矩阵中有的点不能通行。然后求出从左上角到有下角的路线数目。

还是使用DP，用一个矩阵M，给一个m*n大小，每个位置记录走到当前位置有多少种方式。则位置i，j处的最优子结构为：M[i][j] = M[i-1][j] + M[i][j-1]。只不过在检查寻求的时候，判断一下当前位置给定矩阵的[i][j]是否为1，如果为1则M[i][j]=0.

这里同样可以使用一个m*2的数组降低内存，更丧心病狂的就是直接在给定的矩阵上改变就行了，不用申请新的内存。

代码如下：

Runtime: 4 ms, faster than 93.38% of C++ online submissions for Unique Paths II.
Memory Usage: 9.3 MB, less than 45.32% of C++ online submissions for Unique Paths II.

```c++
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int row = obstacleGrid.size();
        if(row == 0) return 0;
        int col = obstacleGrid[0].size();
        if(col == 0) return 0;
        int i, j;
        
        for(j=0; j<col && obstacleGrid[0][j]!=1; j++) obstacleGrid[0][j] = 1;
        for(;j<col; j++) obstacleGrid[0][j] = 0;
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0];
        for(i=0; i<row && obstacleGrid[i][0]!=1; i++) obstacleGrid[i][0] = 1;
        for(;i<row; i++) obstacleGrid[i][0] = 0;
    
        for(i=1; i<row; i++){
            for(j=1; j<col; j++)
                obstacleGrid[i][j] = (1-obstacleGrid[i][j]) * (INT_MAX - obstacleGrid[i-1][j] < obstacleGrid[i][j-1] ? INT_MAX : obstacleGrid[i-1][j] + obstacleGrid[i][j-1]);
        }
        return obstacleGrid[row-1][col-1];
    }
};
```

BitBrave, 2019-06-04
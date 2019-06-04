# LeetCode(62. Unique Paths)题解
------
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


![Above is a 7 x 3 grid. How many possible unique paths are there?](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

Note: m and n will be at most 100.

Example 1:

    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right
Example 2:

    Input: m = 7, n = 3
    Output: 28

## 解题思路
Medium，给一个m*n的矩阵，从左上角只能向下或向右，求出有几种路径。

一个典型的DP问题，用一个矩阵M，给一个m*n大小，每个位置记录走到当前位置有多少种方式。则位置i，j处的最优子结构为：M[i][j] = M[i-1][j] + M[i][j-1]

优化，因为只需要邻居位置，因此使用一个2维数组即可。这里选m或n都可以，但是如果要继续优化的话，可以选一个较小的。节省内存。

代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Unique Paths.
Memory Usage: 8.7 MB, less than 31.75% of C++ online submissions for Unique Paths.

```c++
class Solution {
public:
    int uniquePaths(int m, int n) {
        if(m==1 || n==1) return 1;
        vector<vector<int>> res(m, vector<int>(2, 1));
        for(int j=1; j<n; j++){
            for(int i=1; i<m; i++) res[i][1] = res[i-1][1] + res[i][0];
            for(int i=0; i<m; i++) res[i][0] = res[i][1];
        }
        return res[m-1][1];
    }
};
```
```c++
class Solution {
public:
    int uniquePaths(int m, int n) {
        if(m==1 || n==1) return 1;
        if(m<=n){
            vector<vector<int>> res(m, vector<int>(2, 1));
            for(int j=1; j<n; j++){
                for(int i=1; i<m; i++) res[i][1] = res[i-1][1] + res[i][0];
                for(int i=0; i<m; i++) res[i][0] = res[i][1];
            }
            return res[m-1][1];
        }
        else{
            vector<vector<int>> res(2, vector<int>(n, 1));
            for(int i=1; i<m; i++){
                for(int j=1; j<n; j++) res[1][j] = res[1][j-1] + res[0][j];
                for(int j=0; j<n; j++) res[0][j] = res[1][j];
            }
            return res[1][n-1];
        }
        return 0;
    }
};
```

BitBrave, 2019-06-04
# LeetCode(200. Number of Islands)题解
------
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    Input:
    11110
    11010
    11000
    00000

    Output: 1
Example 2:

    Input:
    11000
    11000
    00100
    00011

    Output: 3

## 解题思路
给一个二维数组，0代表水，1代表陆地，在横纵上被水围住的1组成一个小岛。找出矩阵中的所有小岛，返回对应小岛数。

这个可以使用DFS解决，每次遍历矩阵，第一次遇到1就将其变为0，然后DFS将与其相邻的都变为0.然后直到结束。

代码如下：

Runtime: 12 ms, faster than 93.21% of C++ online submissions for Number of Islands.
Memory Usage: 10.7 MB, less than 86.51% of C++ online submissions for Number of Islands.

```c++
class Solution {
public:
    void DFS(vector<vector<char>>& grid, int i, int j, int row, int col){
        if(grid[i][j] == '0') return;
        grid[i][j] = '0';
        if(i>0) DFS(grid, i-1, j, row, col);
        if(j>0) DFS(grid, i, j-1, row, col);
        if(i<row-1) DFS(grid, i+1, j, row, col);
        if(j<col-1) DFS(grid, i, j+1, row, col);
        return;
    }
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size(), col;
        if(row == 0) return 0;
        col = grid[0].size();
        int res = 0;
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(grid[i][j] == '1'){
                    DFS(grid, i ,j, row, col);
                    res++;
                }
            }
        }
        return res;
    }
};
```

BitBrave, 2019-07-29
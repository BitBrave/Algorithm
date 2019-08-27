# LeetCode(807. Max Increase to Keep City Skyline)题解
------
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:

    Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    Output: 35
    Explanation: 
    The grid is:
    [ [3, 0, 8, 4], 
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0] ]

    The skyline viewed from top or bottom is: [9, 4, 8, 7]
    The skyline viewed from left or right is: [8, 7, 9, 3]

    The grid after increasing the height of buildings without affecting skylines is:

    gridNew = [ [8, 4, 8, 7],
                [7, 4, 7, 7],
                [9, 4, 8, 7],
                [3, 3, 3, 3] ]

Notes:

    1 < grid.length = grid[0].length <= 50.
    All heights grid[i][j] are in the range [0, 100].
    All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

## 解题思路
一个二维的城市群，每个值表示该位置上的建筑物高，现在要尽可能增加每个建筑的高度，但是不能超过其所在位置的上下左右的天际线的高度。求出可以增加高度的总和。

理解题意之后，就是对每个值进行增加，但是不能超过所在的行的最大值，和所在的列的最大值。这样就直接遍历操作即可，没有什么技巧。

代码如下，时间复杂度O(n2)，空间复杂度O(n):

Runtime: 8 ms, faster than 75.14% of C++ online submissions for Max Increase to Keep City Skyline.
Memory Usage: 9.2 MB, less than 93.55% of C++ online submissions for Max Increase to Keep City Skyline.

```c++
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int rl = grid.size(), cl = grid[0].size();
        int res = 0;
        vector<int> row(rl, 0), col(cl, 0);
        
        for(int i=0; i<rl; i++)
            for(int j=0; j<cl; j++) row[i] = max(row[i], grid[i][j]);
        for(int j=0; j<cl; j++)
            for(int i=0; i<rl; i++) col[j] = max(col[j], grid[i][j]);
        
        for(int i=0; i<rl; i++){
            for(int j=0; j<cl; j++){
                res += min(row[i], col[j]) - grid[i][j];
            }
        }
        return res;
    }
};
```

BitBrave, 2019-08-27
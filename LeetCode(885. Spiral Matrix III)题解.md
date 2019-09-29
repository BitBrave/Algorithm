# LeetCode(885. Spiral Matrix III)题解

On a 2 dimensional grid with `R` rows and `C` columns, we start at `(r0, c0)` facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

Eventually, we reach all `R * C` spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.

 

**Example 1:**

```
Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
```

  ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png)

**Example 2:**

```
Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
```

 ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png)

**Note:**

1. `1 <= R <= 100`
2. `1 <= C <= 100`
3. `0 <= r0 < R`
4. `0 <= c0 < C`

## 解题思路

在具有R行和C列的二维网格上，我们从（r0，c0）面向东开始。在这里，网格的西北角位于第一行和第一列，网格的东南角位于最后一行和最后一列。现在，我们以顺时针螺旋形状行走，以访问此网格中的每个位置。每当我们要移出网格边界时，我们都会继续走出网格边界（但稍后可能会返回到网格边界）。最终，我们到达了网格的所有R * C空间。返回以访问网格的顺序表示网格位置的坐标列表。返回这样走的顺序。

这个题需要思考的难度倒是没有多大，主要是有点麻烦。

首先就是如何进行遍历，一开始是给定的原点，然后就是顺时针螺旋遍历。分析可以发现，若不考虑原点，第一次是向右向下走一步，然后向上向右走两步，然后向左向下走三步，向上向右走4步···。即依次递增。而出界的情况可以判断。我们可以取max(R, C)*2的循环圈数，就一定可以遍历完整个数组，对于遍历到的每个位置，判断是否在原数组内，在就加入，否则放弃。

代码如下，时间复杂度O(n2)，空间复杂度O(n2)。

`Runtime: 52 ms, faster than 97.29% of C++ online submissions for Spiral Matrix III.`

`Memory Usage: 13.7 MB, less than 42.86% of C++ online submissions for Spiral Matrix III.`

```C++
class Solution {
public:
    bool isValid(int R, int C, int r, int c){
        return r<R and c<C and r>=0 and c>=0;
    }
    vector<vector<int>> spiralMatrixIII(int R, int C, int r0, int c0) {
        int len = max(R, C) * 2;
        vector<vector<int>> res;
        res.push_back(vector<int>({r0, c0}));
        
        for(int i=1; i<=len; i++){
            // 向右向下走
            int j;
            for(j=1; j<=i; j++){
                if(isValid(R, C, r0, c0+j)) res.push_back(vector<int>({r0, c0+j}));
            }
            c0 = c0 + j - 1;
            for(j=1; j<=i; j++){
                if(isValid(R, C, r0+j, c0)) res.push_back(vector<int>({r0+j, c0}));
            }
            
            // 向左向上走
            r0 = r0 + j - 1;
            i++;
            for(j=1; j<=i; j++){
                if(isValid(R, C, r0, c0-j)) res.push_back(vector<int>({r0, c0-j}));
            }
            c0 = c0 - j + 1;
            for(j=1; j<=i; j++){
                if(isValid(R, C, r0-j, c0)) res.push_back(vector<int>({r0-j, c0}));
            }
            r0 = r0 - j + 1;
        }
        return res;
    }
};
```

BitBrave, 2019-09-29
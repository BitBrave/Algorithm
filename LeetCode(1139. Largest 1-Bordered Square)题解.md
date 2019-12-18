# LeetCode(\1139. Largest 1-Bordered Square)题解

Given a 2D `grid` of `0`s and `1`s, return the number of elements in the largest **square** subgrid that has all `1`s on its **border**, or `0` if such a subgrid doesn't exist in the `grid`.

 

**Example 1:**

```
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
```

**Example 2:**

```
Input: grid = [[1,1,0,0]]
Output: 1
```

 

**Constraints:**

- `1 <= grid.length <= 100`
- `1 <= grid[0].length <= 100`
- `grid[i][j]` is `0` or `1`

## 解题思路

给一个由0和1组成的数组，找出其中由1圈成的最大的正方形的面积。

这个题可以使用DP完成，从上到下，从左到右对每一个元素，我们分别计算以这个元素为正方形右下角时的最大正方形面积。分别找出元素对应的向上的列和向左的行的连续1组成的元素，然后计算对应边长的合法正方形面积。

这个题的DP思想体现在哪里呢？按照上述办法计算时，我们需要计算指定元素为右下角时的最大正方形，这需要O(N2)时间，全部计算一遍就需要O(N4)，但是我们分别维护两个等大的DP数组，记录元素对应向上数的连续1的个数，元素对应向左数的行的连续1的个数。而这是DP可以计算的，总共花费O(n2)时间，最后计算上述答案时只需要O(n3)时间。

代码如下，时间复杂度O(n3)，空间复杂度O(n2)。

`Runtime: 16 ms, faster than 73.07% of C++ online submissions for Largest 1-Bordered Square.`

`Memory Usage: 10.8 MB, less than 100.00% of C++ online submissions for Largest 1-Bordered Square.`

```c++
class Solution {
public:
    int largest1_(vector<vector<int>>& Row, vector<vector<int>>& Col, int r, int c){
        int ret = 1;
        int m = min(Row[r][c], Col[r][c]);
        for (int i=1; i<m; i++) {
            if (min(Col[r][c-i], Row[r-i][c]) > i) ret = max(ret, (i+1) * (i+1));
        }
        return ret;
    }
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        int rlen = grid.size(), clen = grid[0].size(), ret = 0;
        vector<vector<int>> Row(rlen+1, vector<int>(clen+1,0)), Col(rlen+1, vector<int>(clen+1,0));
        
        for (int r=0; r<rlen; r++) {
            for (int c=0; c<clen; c++) {
                if (grid[r][c]==0) {
                    continue;
                }
                Row[r+1][c+1] = Row[r+1][c] + 1;
                Col[r+1][c+1] = Col[r][c+1] + 1;
                
                ret = max(ret, largest1_(Row, Col, r+1, c+1));
            }
        }
        return ret;
    }
};
```

 

BitBrave，2019-12-18
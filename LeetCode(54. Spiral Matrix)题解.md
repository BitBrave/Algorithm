# LeetCode(54. Spiral Matrix)题解
------
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

    Input:
    [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
Example 2:

    Input:
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

## 解题思路

Medium，将一个二维矩阵顺时针螺旋输出成一个一维数组。

方法很简单，直接遍历即可，先遍历行，在遍历最后一列，再遍历最底下一行，再遍历第一列，再将范围缩小2，重复上述过程即可。注意边界值。

代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Spiral Matrix.
Memory Usage: 8.7 MB, less than 42.46% of C++ online submissions for Spiral Matrix.

```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int row = matrix.size();
        if(row == 0) return res;
        int col = matrix[0].size();
        if(col == 0) return res;
        int li=0, lj=0;
        while(li<row-1 & lj<col-1){
            for(int i=lj; i<col; i++) res.push_back(matrix[li][i]);
            for(int i=li+1; i<row; i++) res.push_back(matrix[i][col-1]);
            for(int i=col-2; i>=lj; i--) res.push_back(matrix[row-1][i]);
            for(int i=row-2; i>li; i--) res.push_back(matrix[i][lj]);
            row--;
            col--;
            li++;
            lj++;
        }
        if(li==row-1){
            for(int i=lj; i<col; i++) res.push_back(matrix[li][i]);
        }
        else if(li==col-1){
            for(int i=li; i<row; i++) res.push_back(matrix[i][lj]);
        }
        return res;
    }
};
```

BitBrave, 2019-05-30
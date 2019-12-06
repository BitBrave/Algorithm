# LeetCode(\304. Range Sum Query 2D - Immutable)题解

Given a 2D matrix *matrix*, find the sum of the elements inside the rectangle defined by its upper left corner (*row*1, *col*1) and lower right corner (*row*2, *col*2).

![Range Sum Query 2D](https://leetcode.com/static/images/courses/range_sum_query_2d.png)
The above rectangle (with the red border) is defined by (row1, col1) = **(2, 1)** and (row2, col2) = **(4, 3)**, which contains sum = **8**.

**Example:**

```
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```



**Note:**

1. You may assume that the matrix does not change.
2. There are many calls to *sumRegion* function.
3. You may assume that *row*1 ≤ *row*2 and *col*1 ≤ *col*2.

## 解题思路

给出一个二维数组，构建一个类，建立一个函数，给出左上角和右下角坐标，要求每次返回数组的对应区域的元素之和。

这个题因为说明了构建数组是一次操作，后续多次是查询区域和操作，所以我们可以首先构建数组的和。使用D来表示和，D\[i\]\[j\]表示从(0,0)到(i,j)的所有元素之和。那么后续每次查询都可以在O(1)的时间内完成。直接返回D\[i\]\[j\]-D[i\]\[b\]-D[a]\[j\]+D[a\][b]，其中ij是右下角，ab左上角。

代码如下，时间复杂度分为两部分，构建花费O(n2)，后续每次查询花费O(1)，空间复杂度O(n2)。

`Runtime: 24 ms, faster than 80.82% of C++ online submissions for Range Sum Query 2D - Immutable.`

`Memory Usage: 16.5 MB, less than 100.00% of C++ online submissions for Range Sum Query 2D - Immutable.`

```c++
class NumMatrix {
    vector<vector<int>> D;
public:
    NumMatrix(vector<vector<int>>& matrix) {
        int row = matrix.size(), col;
        //D = vector<vector<int>>(0, vector<int>(0));
        if(row == 0) return;
        col = matrix[0].size();
        D.push_back(vector<int>(col+1, 0));
        for(int i=0; i<row; i++){
            D.push_back(vector<int>(col+1));
            D[i+1][0] = D[i][0] + matrix[i][0];
            for(int j=0; j<col; j++) D[i+1][j+1] = matrix[i][j] + D[i+1][j] + D[i][j+1] - D[i][j]; 
        }
        return;
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        if(D.size() == 0) return 0;
        return D[row2+1][col2+1] - D[row2+1][col1] - D[row1][col2+1] + D[row1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
```

BitBrave，2019-12-06
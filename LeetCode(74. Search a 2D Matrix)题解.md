# LeetCode(74. Search a 2D Matrix)题解
------
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

    Input:
    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 3
    Output: true
Example 2:

    Input:
    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
        ]
    target = 13
    Output: false

## 解题思路
Medium，给一个矩阵，矩阵中每一行是升序排列，每一行的第一个数比上一行的所有数都大。然后给出一个数判断这个数在不在矩阵内。

方法很简单，考虑矩阵按行展开，就是一个升序的数组，直接在其中使用二分法就可以找到。唯一考虑的就是将一个数转为矩阵内对应的坐标。时间复杂度O（logn），空间复杂度O（1）。

代码如下：

Runtime: 4 ms, faster than 99.89% of C++ online submissions for Search a 2D Matrix.
Memory Usage: 9.9 MB, less than 57.72% of C++ online submissions for Search a 2D Matrix.

```c++
class Solution {
public:
    bool searchList(vector<vector<int>>& matrix, int target, int col, int left, int right){
        if(left > right) return false;
        int mid = (left + right) / 2;
        int m1 = mid / col, m2 = mid % col;
        if(target == matrix[m1][m2]) return true;
        if(target > matrix[m1][m2]) return searchList(matrix, target, col, mid+1, right);
        if(target < matrix[m1][m2]) return searchList(matrix, target, col, left, mid-1);
        
        return false;
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size();
        if (row == 0) return false;
        int col = matrix[0].size();
        return searchList(matrix, target, col, 0, row * col - 1);
    }
};
```

BitBrave, 2019-06-10
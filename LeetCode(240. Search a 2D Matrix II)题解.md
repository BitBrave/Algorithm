# LeetCode(240. Search a 2D Matrix II)题解
------
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
Example:

    Consider the following matrix:

    [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    Given target = 5, return true.

    Given target = 20, return false.

## 解题思路
矩阵从左到右数字递增，从上到下递增。找出一个数是否存在。

最简单的方法就是暴力搜索，时间复杂度O(n2)。但是这肯定是最差的，应当有更好的办法。

可以利用到局部有序的特性。设置一个范围，设置宽col为初始数组宽,row为初始数组高.上下左右设置i=0,j=0。查看要找的数，如果大于A[row-1][col-1]或者小于A[i][j]就返回false。然后查看是否大于A[i][col],如果大于，说明i行都不匹配，i+1，如果小于，说明col列不匹配，col-1.

直到i>与row或者col<j时，返回false，或者走到中间发现匹配的，返回true。时间复杂度O(n)

代码如下：

Runtime: 56 ms, faster than 97.85% of C++ online submissions for Search a 2D Matrix II.
Memory Usage: 12.7 MB, less than 100.00% of C++ online submissions for Search a 2D Matrix II.

```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size() - 1, col;
        if(row < 0) return false;
        col = matrix[0].size() - 1;
        if(col < 0) return false;
        int i=0, j=0;
        while(i<=row && j<=col){
            if(target > matrix[i][col]) i++;
            else if(target < matrix[i][col]) col--;
            else return true;
        }
        return false;
    }
};
```

BitBrave, 2019-08-12
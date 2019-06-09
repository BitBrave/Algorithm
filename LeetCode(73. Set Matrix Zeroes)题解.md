# LeetCode(73. Set Matrix Zeroes)题解
------
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

    Input: 
    [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
    Output: 
    [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]
Example 2:

    Input: 
    [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
    Output: 
    [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
    ]
Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?


## 解题思路
Medium，给一个矩阵，将其中0所在的行和列进行归零然后返回. 要求尽量使用少的内存。

可以使用一个集合记录需要转为0的行和列，最后再统一置0。这样内存消耗O(m+n)，或者可以将需要置0的先置为别的不会与数组重复的数，然后再统一转化。这样需要O(1)的空间复杂度。

我选择后者试试。

代码如下：

Runtime: 48 ms, faster than 87.23% of C++ online submissions for Set Matrix Zeroes.
Memory Usage: 11.6 MB, less than 30.67% of C++ online submissions for Set Matrix Zeroes.

```c++
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int row = matrix.size(), col = matrix[0].size();
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(matrix[i][j] == 0){
                    for(int k=0; k<col; k++) matrix[i][k] = matrix[i][k] != 0 ? 0XFFFF : 0;
                    for(int k=0; k<row; k++) matrix[k][j] = matrix[k][j] != 0 ? 0XFFFF : 0;
                }
            }
        }
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                matrix[i][j] = matrix[i][j] == 0XFFFF ? 0 : matrix[i][j];
            }
        }
        return;
    }
};
```

BitBrave, 2019-06-09
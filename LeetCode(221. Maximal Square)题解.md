# LeetCode(221. Maximal Square)题解
------
    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    Output: 4

## 解题思路
从二维数组中找出最大的全由1组成的正方形面积。

这种求极值的题一般都使用DP。这里注意，使用DP的时候，有时候可以在中间状态求得最优值。这里我们用相同大小的二维数组来D记录转移状态。其中D[i][j]表示matrix中matrix[i][j]为左下角的情况下最大的全1组成的正方形的边长。那么状态转移方程就可以如下：

对于matrix[i][j],如果为0，则D[i][j]=0；

如果为1，那么首先是新的高，应该是1+min(D[i-1][j], D[i-1][j-1]), 而宽应该为1+min(D[i][j-1], D[i-1][j-1])。这二者应该取最小值，得新的全1正方形的长度应该为1+min(D[i-1][j], D[i][j-1], D[i-1][j-1]).

在上述过程中，每次计算都记录res值，最后返回res值即可。

这里状态转移方程可以看出，使用一个X*2的矩阵就可以，可以节省内存。

代码如下

Runtime: 16 ms, faster than 96.13% of C++ online submissions for Maximal Square.
Memory Usage: 10.6 MB, less than 85.19% of C++ online submissions for Maximal Square.

```C++
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int row = matrix.size(), col, res = 0;
        if(row == 0) return res;
        col = matrix[0].size();
        if(col == 0) return res;
        
        vector<vector<int>> D(2, vector<int>(col+1, 0));
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(matrix[i][j] == '0') D[1][j+1] = 0;
                else D[1][j+1] = 1 + min(D[0][j], min(D[1][j], D[0][j+1]));
                res = max(res, D[1][j+1]*D[1][j+1]);
            }
            for(int j=1; j<=col; j++) D[0][j] = D[1][j];
        }
        return res;
    }
};
```

BitBrave, 2019-08-17
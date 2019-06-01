# LeetCode(59. Spiral Matrix II)题解
------
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

    Input: 3
    Output:
    [
    [ 1, 2, 3 ],
    [ 8, 9, 4 ],
    [ 7, 6, 5 ]
    ]

## 解题思路

Medium，就是建立一个n*n的二维矩阵。顺时针由外而内插入1到n*2这些数。可以直接首先插入第一行，然后最后一列，然后最后一行，然后第一列，然后数组的整体减少2.直到最后达到只剩一行或一列，直接插入即可。

代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Spiral Matrix II.
Memory Usage: 9.1 MB, less than 29.22% of C++ online submissions for Spiral Matrix II.

```c++
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int> > res(n, vector<int>(n));
        int l = 0, c = 1;
        
        while(l<n-1){
            // first row
            for(int j=l; j<n; j++) res[l][j] = c++;
            // last col
            for(int i=l+1; i<n; i++) res[i][n-1] = c++;
            // last row
            for(int j=n-2; j>=l; j--) res[n-1][j] = c++;
            // first col
            for(int i=n-2; i>l; i--) res[i][l] = c++;
            
            l++;
            n--;
        }
        if(l==n-1) res[l][l] = c;
        
        return res;
    }
};
```

BitBrave, 2019-06-01
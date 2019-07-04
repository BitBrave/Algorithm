# LeetCode(120. Triangle)题解
------
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

    [
           [2],
          [3,4],
         [6,5,7],
        [4,1,8,3]
    ]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

    Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

## 解题思路
给一个三角形T，从顶到底找一个最短的路径，只能从相邻的往下走。要求额外空间不能超过O(n).

这里可以使用DP的办法。首先不要考虑空间的限制。观察三角形，0行一个数，1行两个数，2行三个数，···，n行n+1个数。我们用一个二维数组来记录，D[i][j]表示当前走到第i行中以第j个数为终点的最短路径值，其中j的取值范围为0-i。因此可以有如下最优子结构。

如果j=0，D[i][j] = D[i-1][0] + T[i][0]

如果j=i，D[i][j] = D[i-1][i-1] + T[i][i]

其它情况， D[i][j] = min(D[i-1][j-1], D[i-1][j]) + T[i][j]

初始情况D[0][0] = T[0][0]

观察最优子结构，可以发现每次只用到了上一行相邻的位置元素。因此我们可以把矩阵缩小到2*n，达到O(n)的空间复杂度。

代码如下：

Runtime: 8 ms, faster than 76.88% of C++ online submissions for Triangle.
Memory Usage: 9.6 MB, less than 93.97% of C++ online submissions for Triangle.

```c++
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        if(n == 0) return 0;
        
        vector<vector<int>> D(2, vector<int>(n, 0));
        D[0][0] = triangle[0][0];
        for(int i=1; i<n; i++){
            D[1][0] = D[0][0] + triangle[i][0];
            D[1][i] = D[0][i-1] + triangle[i][i];
            //cout<<D[1][0]<<" "<<D[1][i]<<endl;
            for(int j=1; j<i; j++) {
                D[1][j] = min(D[0][j-1], D[0][j]) + triangle[i][j];
                //cout<<D[1][j]<<endl;
            }
            for(int j=0; j<=i; j++) D[0][j] = D[1][j];
        }
        return *min_element(D[0].begin(),D[0].end());
    }
};
```

BitBrave, 2019-07-04

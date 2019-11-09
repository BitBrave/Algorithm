#  LeetCode(931. Minimum Falling Path Sum)题解

Given a **square** array of integers `A`, we want the **minimum** sum of a *falling path* through `A`.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

**Example 1:**

```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
```

- `[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]`
- `[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]`
- `[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]`

The falling path with the smallest sum is `[1,4,7]`, so the answer is `12`.

**Note:**

1. `1 <= A.length == A[0].length <= 100`
2. `-100 <= A[i][j] <= 100`

## 解题思路

给定一个二维数组A，每个元素都是整数，现在从第一行选定一个位置下降到最后一行，每个值表示选定这个位置的代价。选路的时候，下一行的位置和上一行的位置列之间相差最多一个。现在计算返回一条最短路径。

这个明显就是DP。我们维护一个和A同等大小的数组，DP\[i\]\[j\]表示第i行以第j列位置为终点的最短路径代价。最后只需要遍历最后一行的数据，选择最小的即可。

那么初始状态为，DP\[0\]\[i\] = A\[0\]\[i\].

转移方程为，DP\[\i]\[j\] = A\[i\]\[j\]+min(DP\[\i-1]\[j-1\], DP\[\i-1]\[j\], DP\[\i-1]\[j+1\]).

可知，转移只用到了上一层结果，因此可以使用一个2*col的数组记录。

代码如下，数组大小N2，时间复杂度O(N2)，空间复杂度O(N)。

`Runtime: 8 ms, faster than 99.60% of C++ online submissions for Minimum Falling Path Sum.`

`Memory Usage: 9.7 MB, less than 100.00% of C++ online submissions for Minimum Falling Path Sum.`

```C++
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& A) {
        int row = A.size(), col = A[0].size();
        vector<vector<int>> ret(2, vector<int>(col + 2, INT_MAX));
        
        for(int j=0; j<col; j++) ret[0][j+1] = A[0][j];
        for(int i=1; i<row; i++){
            for(int j=0; j<col; j++){
                ret[1][j+1] = A[i][j] + min(ret[0][j], min(ret[0][j+1], ret[0][j+2]));
            }
            for(int j=0; j<col+2; j++) ret[0][j] = ret[1][j];
        }
        return *min_element(ret[0].begin(), ret[0].end());
    }
};
```

BitBrave，2019-11-09
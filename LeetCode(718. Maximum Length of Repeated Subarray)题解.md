# LeetCode(718. Maximum Length of Repeated Subarray)题解
------
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

    Input:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    Output: 3
    Explanation: 
    The repeated subarray with maximum length is [3, 2, 1].
    

Note:

    1 <= len(A), len(B) <= 1000
    0 <= A[i], B[i] < 100

## 解题思路

求出两个数组的最长公共子串的长度。

这种求极值的问题一般都用DP，可以使用D[i][j]表示A中前i个数字和B中前j个数字的最长公共长度，当然，前提是A[i]=B[i]. 如果等于D[i][j] = D[i-1][j-1] + 1. 否则赋值为0. 在这个过程中，时刻更新res.

这个告诉我们，DP不一定非得在最后才能求出来，有时候在中间状态中就能找到。

为了节省内存，可以使用一个X*2的矩阵。

代码如下：

Runtime: 264 ms, faster than 6.24% of C++ online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 9.2 MB, less than 100.00% of C++ online submissions for Maximum Length of Repeated Subarray.

```c++
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int lenA = A.size(), lenB = B.size(), res = 0;
        vector<vector<int>> D(2, vector<int>(lenB + 1, 0));
        for(int i=0; i<lenA; i++){
            for(int j=0; j<lenB; j++){
                if(A[i] != B[j]) D[1][j+1] = 0;
                else D[1][j+1] = D[0][j] + 1; 
                res = max(res, D[1][j+1]);
            }
            for(int j=0; j<lenB; j++) D[0][j+1] = D[1][j+1];
        }
        return res;
    }
};
```

BitBrave, 2019-08-16
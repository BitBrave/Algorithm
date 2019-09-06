# Leetcode(835. Image Overlap)题解

Two images `A` and `B` are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the *overlap* of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does **not** include any kind of rotation.)

What is the largest possible overlap?

**Example 1:**

```
Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
```

**Notes:** 

1. `1 <= A.length = A[0].length = B.length = B[0].length <= 30`
2. `0 <= A[i][j], B[i][j] <= 1`

## 解题思路

给两个二值数组，可以上下左右移动，求出其1值重叠的最大的大小。

民工题，保持一个数组不变，每次移动变换另一个数组，进行比较即可。

代码如下，时间复杂度$O(n^4)$，空间复杂度$O(n^2)$:

`Runtime: 36 ms, faster than 74.91% of C++ online submissions for Image Overlap. Memory Usage: 9.2 MB, less than 86.67% of C++ online submissions for Image Overlap.`

```c++
class Solution {
    vector<vector<int>> A_;
    vector<vector<int>> B_;
public:
    int Overlap(int r, int c, int row, int col, bool pre) {
        int res = 0;
        if(pre){
            for(int i=r; i<row; i++)
                for(int j=c; j<col; j++)
                   res += A_[i][j] & B_[i][j];
        }
        else{
            for(int i=0; i<=r; i++)
                for(int j=0; j<=c; j++)
                   res += A_[i][j] & B_[i][j];
        }
        return res;
    }
    void Fill(vector<vector<int>>& A, int r, int c, int row, int col, bool pre){
        if(pre){
            for(int i=0; i<row-r; i++){
                for(int j=0; j<col-c; j++){
                    A_[i+r][j+c] = A[i][j];
                }
            }
        }
        else{
            for(int i=0; i<=r; i++){
                for(int j=0; j<=c; j++){
                    A_[i][j] = A[row-1-r+i][col-1-c+j];
                }
            }
        }
        return;
    }
    int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
        int row = A.size(), col = A[0].size(), res = 0;
        A_ = vector<vector<int>>(row, vector<int>(col, 0));
        B_ = B;
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                Fill(A, i, j, row, col, true);
                res = max(res, Overlap(i, j, row, col, true));
            }
        }
        fill(A_.begin(), A_.end(), vector<int>(col, 0));
        for(int i=row-1; i>=0; i--){
            for(int j=col-1; j>=0; j--){
                Fill(A, i, j, row, col, false);
                //cout<<i<<" "<<j<<" "<<Overlap(i, j, row, col, false)<<endl;
                res = max(res, Overlap(i, j, row, col, false));
            }
        }
        return res;
    }
};
```

BitBrave，2019-09-06
# LeetCode(801. Minimum Swaps To Make Sequences Increasing)题解
------
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:

    Input: A = [1,3,5,4], B = [1,2,3,7]
    Output: 1
    Explanation: 
    Swap A[3] and B[3].  Then the sequences are:
    A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
    which are both strictly increasing.
Note:

    A, B are arrays with the same length, and that length will be in the range [1, 1000].
    A[i], B[i] are integer values in the range [0, 2000].

## 解题思路

要求交换最少的次数，将两个数组变为递增数组。

这个使用DP，dp[i][0]表示不交换i，使得[0, i]严格递增的最小swap数。dp[i][1]表示交换i，使得[0, i]严格递增的最小swap数。

可以逐步判定。但是因为给定数据的特殊性，因此可以简化为下面的代码，很容易读懂。

代码如下，时间复杂度O(n), 空间复杂度O(n):

Runtime: 16 ms, faster than 18.40% of C++ online submissions for Minimum Swaps To Make Sequences Increasing.
Memory Usage: 10.7 MB, less than 10.00% of C++ online submissions for Minimum Swaps To Make Sequences Increasing.

```c++
class Solution {
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        int len = A.size();
        vector<vector<int>> res(len, vector<int>(2, 2000));
        res[0][0] = 0;
        res[0][1] = 1;
        for(int i=1; i<len; i++){
            if(A[i]>A[i-1] && B[i]>B[i-1]){
                res[i][0] = min(res[i-1][0], res[i][0]);
                res[i][1] = min(res[i-1][1]+1, res[i][1]);
            }
            
            if(A[i]>B[i-1] && B[i]>A[i-1]){
                res[i][0] = min(res[i-1][1], res[i][0]);
                res[i][1] = min(res[i-1][0]+1, res[i][1]);
            }
        }
        return min(res[len-1][0], res[len-1][1]);
    }
};

or

class Solution {
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        int len = A.size();
        vector<vector<int>> res(len, vector<int>(2, 2000));
        res[0][0] = 0;
        res[0][1] = 1;
        for(int i=1; i<len; i++){
            if(A[i]>A[i-1] && B[i]>B[i-1]){
                res[i][0] = res[i-1][0];
                res[i][1] = res[i-1][1]+1;
            }
            
            if(A[i]>B[i-1] && B[i]>A[i-1]){
                res[i][0] = min(res[i-1][1], res[i][0]);
                res[i][1] = min(res[i-1][0]+1, res[i][1]);
            }
        }
        return min(res[len-1][0], res[len-1][1]);
    }
};
```

根据目前的代码可以看到，每次使用只使用了相邻的数据，因此可以将空间优化到常量空间。

代码如下，时间复杂度O(n), 空间复杂度O(1):

Runtime: 12 ms, faster than 68.53% of C++ online submissions for Minimum Swaps To Make Sequences Increasing.
Memory Usage: 9.1 MB, less than 90.00% of C++ online submissions for Minimum Swaps To Make Sequences Increasing.

```c++
class Solution {
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        int len = A.size();
        int res0 = 0, res1 = 1;
        int t0, t1;
        for(int i=1; i<len; i++){
            t0 = 2000;
            t1 = 2000;
            if(A[i]>A[i-1] && B[i]>B[i-1]){
                t0 = res0;
                t1 = res1 + 1;
            }
            
            if(A[i]>B[i-1] && B[i]>A[i-1]){
                t0 = min(t0, res1);
                t1 = min(t1, res0+1);
            }
            res0 = t0;
            res1 = t1;
        }
        return min(res0, res1);
    }
};
```

BitBrave, 2019-08-26
# LeetCode(279. Perfect Squares)题解
------
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

    Input: n = 12
    Output: 3 
    Explanation: 12 = 4 + 4 + 4.
Example 2:

    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.
## 解题思路
给定一个数，用最少的可以开方的数的平方之和来填充这个数。

这个题和322. Coin Change很相似。都用DP来做。对n进行开方，找出比n小但离得最近的平方数m，那么这个题就变成了从1-m中找出一些（可以重复）数，其平方和等于n，和找硬币是一样的操作。

解法可参考我的322. Coin Change的解法。 在此不再赘述。

代码如下

Runtime: 160 ms, faster than 20.52% of C++ online submissions for Perfect Squares.
Memory Usage: 11.2 MB, less than 76.92% of C++ online submissions for Perfect Squares.

```c++
class Solution {
public:
    int numSquares(int n) {
        int m = int(sqrt(n)) + 1;
        vector<int> res(n+1, INT_MAX);
        res[0] = 0;
        for(int i=1; i < m; i++){
            for(int j=1; j<=n; j++){
                if(j-i*i >= 0) res[j] = min(res[j], res[j-i*i]==INT_MAX ? INT_MAX : (res[j-i*i]+1));
            }
        }
        return res[n];
    }
};
```

BitBrave, 2019-08-20
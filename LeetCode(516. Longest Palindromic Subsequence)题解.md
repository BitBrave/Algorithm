## LeetCode(\516. Longest Palindromic Subsequence)题解

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

**Example 1:**
Input:

```
"bbbab"
```

Output:

```
4
```

One possible longest palindromic subsequence is "bbbb".



**Example 2:**
Input:

```
"cbbd"
```

Output:

```
2
```

One possible longest palindromic subsequence is "bb".

## 解题思路

给定字符串s，找到s的最长回文子序列的长度。假设s的最大长度为1000。

这个可以使用DP问题，回文子序列是是可以由不连续的字符组成的，我们可以首先计算长度为1的子序列中最长的回文字符串长度，然后计算长度为2的，然后长度为3,4,5，···直到len(s)，最后返回最长的长度即可。

我们使用一个len(s)\*len(s)的二维数组DP记录状态转移子数组的值。其中DP\[i\]\[j\]表示字符串s中i到j位置的最长的合法字符串。那么就有。

- 如果i>j，DP\[i\]\[j\]=0。
- 如果i==j，DP\[i\]\[j\]=1。
- 如果s[i\]==s\[j\]，DP\[i\]\[j\] = max(DP\[i\]\[j-1\], DP\[i+1\]\[j\], DP\[i+1\]\[j-1\]+2)
- 如果s[i\]!=s\[j\]，DP\[i\]\[j\] = max(DP\[i\]\[j-1\], DP\[i+1\]\[j\])

最后返回 DP\[0\]\[len(s)-1\]即可。

注意这个经过分析数组更新是每次都沿着对角线平行的方向，更新的时候只使用了前两斜线的数据，因此可以将空间复杂度降到O(n)，只是数组变化有点麻烦而已。

代码如下，时间复杂度O(n)，空间复杂度O(n2)。

`Runtime: 128 ms, faster than 8.56% of C++ online submissions for Longest Palindromic Subsequence.`

`Memory Usage: 69.3 MB, less than 100.00% of C++ online submissions for Longest Palindromic Subsequence.`

```c++
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int len = s.size();
        if(len <= 1) return len;
        vector<vector<int>> D(len, vector<int>(len, 0));
        for(int i=0; i<len; i++) D[i][i] = 1;
        for(int k=1; k<len; k++){
            for(int i=k; i<len; i++){
                if(s[i-k]==s[i]) D[i-k][i] = 2 + D[i-k+1][i-1];
                else D[i-k][i] = max(D[i-k][i-1], D[i-k+1][i]);
            }
        }
        return D[0][len-1];
    }
};
```

BitBrave，2019-12-13
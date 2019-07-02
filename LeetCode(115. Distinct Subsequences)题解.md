# LeetCode(115. Distinct Subsequences)题解
------
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

    Input: S = "rabbbit", T = "rabbit"
    Output: 3
Explanation:

    As shown below, there are 3 ways you can generate "rabbit" from S.
    (The caret symbol ^ means the chosen letters)

    rabbbit
    ^^^^ ^^
    rabbbit
    ^^ ^^^^
    rabbbit
    ^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

    As shown below, there are 5 ways you can generate "bag" from S.
    (The caret symbol ^ means the chosen letters)

    babgbag
    ^^ ^
    babgbag
    ^^    ^
    babgbag
    ^    ^^
    babgbag
    ^  ^^
    babgbag
        ^^^

## 解题思路
给出字符串S，和T，判断S中有几个子字符串是T中的。

可以使用DP的方法求解。使用一个二维数组D,DP[i][j]表示S前i个字符中有几个子字符串是和T前j个字符匹配的。

初始化D[0][0]=1, D[0][1-T.size()] = 0, D[0-S.size()][0] = 0;

然后对于D[i][j]操作如下：

1 S[i-1] != T[j-1]; 表示不匹配，那么直接等于之前的情况，D[i][j] = D[i-1][j]
2 S[i-1] == T[j-1]; 表示匹配，那么有两种情况，一是最后的匹配用上了S[i-1]，一是没用上。因此D[i][j] = D[i-1][j] + D[i-1][j-1];

上述观察只用到了相邻的值，因此，可以直接使用一个S.size()*2数组. 降低空间复杂度。因为S.size()>T.size(),因此最好使用2*T.size()数组。

代码如下

Runtime: 16 ms, faster than 29.32% of C++ online submissions for Distinct Subsequences.
Memory Usage: 8.8 MB, less than 79.23% of C++ online submissions for Distinct Subsequences.

```c++
class Solution {
public:
    int numDistinct(string s, string t) {
        int slen = s.size(), tlen = t.size();
        vector<vector<int>> D(2, vector<int>(tlen + 1, 0));
        D[0][0] = 1;
        for(int i=0; i<slen; i++){
            for(int j=0; j<tlen; j++){
                D[1][j+1] = D[0][j+1];
                if(INT_MAX - D[1][j+1] >=  (s[i] == t[j] ? D[0][j] : 0)) D[1][j+1] += (s[i] == t[j] ? D[0][j] : 0);
                else D[1][j+1] = INT_MAX;
            } 
            for(int j=1; j<tlen+1; j++) D[0][j] = D[1][j];
        }
        return D[1][tlen];
    }
};
```

BitBrave, 2019-07-02
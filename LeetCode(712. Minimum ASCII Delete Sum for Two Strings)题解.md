# LeetCode(712. Minimum ASCII Delete Sum for Two Strings)题解
------
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
    Input: s1 = "sea", s2 = "eat"
    Output: 231
    Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
    Deleting "t" from "eat" adds 116 to the sum.
    At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
    Input: s1 = "delete", s2 = "leet"
    Output: 403
    Explanation: Deleting "dee" from "delete" to turn the string into "let",
    adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
    At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
    If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

    0 < s1.length, s2.length <= 1000.
    All elements of each string will have an ASCII value in [97, 122].

## 解题思路
从两个字符串中删除最少的字符值Ascall值之和最小的字符，使得两个字符串相等。

这个题明显只能使用DP，构建一个DP[s1.size()+1][s2.size()+1]的矩阵，DP[i][j]表示字符串s1[1，i]和s2[1，j]之间的最优解。那么这个状态转移方程就可以写作如下：

如果s1为空，s2必须删掉所有字符，DP[i][j]为s2的字符值之和。

如果s2为空，s1必须删掉所有字符，DP[i][j]为s1的字符值之和。

都不为空，那么当前可以选择删除s1[i]，表明s1[1，i-1]和s2[1，j]之间的最优值，或者删除s2[j]，表明s1[1，i]和s2[1，j-1]之间的最优值. 

又或者两个都删除表明选择s1[1，i-1]和s2[1，j-1]之间的最优值，但这时候如果s1[i] == s2[j]，那么当前不用删除，直接匹配即可。

优化的话，可以看到每次都只需要挨着的值，因此可以将其优化为DP[2][s2.size()+1].

### 时间复杂度O(mn), 空间复杂度O(n)

代码如下

Runtime: 36 ms, faster than 24.38% of C++ online submissions for Minimum ASCII Delete Sum for Two Strings.
Memory Usage: 9 MB, less than 77.78% of C++ online submissions for Minimum ASCII Delete Sum for Two Strings.

```c++
class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int len1 = s1.size(), len2 = s2.size();
        vector<vector<int>> res(2, vector<int>(len2+1, 0));
        
        for(int j=0; j<len2; j++) res[0][j+1] = s2[j] + res[0][j];
        
        for(int i=0; i<len1; i++){
            res[1][0] = s1[i] + res[0][0];
            for(int j=0; j<len2; j++){
                res[1][j+1] = min(res[0][j+1]+s1[i], res[1][j]+s2[j]);
                res[1][j+1] = min(res[1][j+1], res[0][j] + (s1[i]==s2[j] ? 0:(s1[i]+s2[j])));
            }
            for(int j=0; j<=len2; j++) res[0][j] = res[1][j];
        }
        return res[1][len2];
    }
};
```

BitBrave, 2019-08-23
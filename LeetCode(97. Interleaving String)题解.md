# LeetCode(97. Interleaving String)题解
------
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
    Example 2:

    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false

# 解题思路
给出三个字符串，判断第三个字符串是不是可以由前两个字符串交叉而成。字符的顺序不能乱。

方法很简单。首先是判断前两个字符串的字符个数和必须和第三个一样。否则肯定不匹配。

然后可以使用DP的办法，建立一个DP数组D，D[i][j]表示s1的前i+1个字符和s2的前j+1个字符是否和s3的前i+j+2个字符相配。然后直接做就可以了。

代码如下：

Runtime: 56 ms, faster than 5.97% of C++ online submissions for Interleaving String.
Memory Usage: 8.5 MB, less than 66.33% of C++ online submissions for Interleaving String.

```c++
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        
        int l1 = s1.size(), l2 = s2.size(), l3 = s3.size();
        if(l3 == 0) return l1+l2 == 0;
        if(l1 == 0) return s2 == s3;
        if(l2 == 0) return s1 == s3;
        if(l1+l2 != l3) return false;
        
        vector<vector<bool>> DP(l1+1, vector<bool>(l2+1, false));
        DP[0][0] = true;
        for(int k=0; k<l3; k++){
            if(l1 >= k+1 && s1[k] == s3[k]) DP[k+1][0] = DP[k][0];
            if(l2 >= k+1 && s2[k] == s3[k]) DP[0][k+1] = DP[0][k];
            
            for(int i=1; (i<=l1) && (i<k+1); i++){
                
                for(int j=k+1-i; j<=l2; j++){
                    if(s1[i-1] != s3[k] && s2[j-1] != s3[k]){
                        DP[i][j] = false;
                        continue;
                    }
                    if(s1[i-1] == s3[k]){
                        DP[i][j] = DP[i-1][j];
                    }
                    if(s2[j-1] == s3[k]){
                        DP[i][j] = DP[i][j] == true ? true : DP[i][j-1];
                    }
                }
            }
        }
        return DP[l1][l2];
    }
};
```

其实还有一种更方便的办法，首先将s1与s3比较，删除s3中与s1相同的字符（一一对应，s1的一个字符在s3中只删一次），然后最后如果s1不为空就表示不匹配，为空就判断剩下的字符串s3是不是等于s2，等于则匹配，否则不匹配。(这是错误的想法)


BitBrave, 2019-06-23
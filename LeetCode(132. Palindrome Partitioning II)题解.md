# LeetCode(132. Palindrome Partitioning II)题解
------
Given a string s, partition s such that every substring of the partition is a palindrome.

    Return the minimum cuts needed for a palindrome partitioning of s.

Example:

    Input: "aab"
    Output: 1
    Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

## 解题思路
给出一个字符串，将其分为不同的子串，要求每个子串都是回文串，求出最少的子串数。

可以使用DP的办法解决，假设字符串S长度为len。建立一个len+1长度的数组DP,DP[i]表示表示前i个字符内最少的回文子串数。DP[0] = -1作为边界值, DP[1] = 0.

后续的DP[i] = min(DP[j]+1) (S[j],...,S[i]为有效回文串，初始化j = i-1，遇到不能构成回文串时就直接结束)。

最后的结果返回DP[len]即可.

代码如下：

Runtime: 1084 ms, faster than 5.04% of C++ online submissions for Palindrome Partitioning II.
Memory Usage: 554.3 MB, less than 6.00% of C++ online submissions for Palindrome Partitioning II.

```c++
class Solution {
public:
    bool isPalindrome(string s, int sta, int end){
        while(s[sta++] == s[end--] && sta<end);
        return sta >= end && s[--sta] == s[++end];
    }
    int minCut(string s) {
        int len = s.size();
        vector<int> DP(len+1, len);
        
        DP[0] = -1;
        DP[1] = 0;
        for(int i=1; i<len; i++){
            for(int j = i; j>=0; j--){
                if(isPalindrome(s, j, i)) DP[i+1] = min(DP[i+1], 1+DP[j]);
            }
        }
        return DP[len];
    }
};
```

BitBrave, 2019-07-17
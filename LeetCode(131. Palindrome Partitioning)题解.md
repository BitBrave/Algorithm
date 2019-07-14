# LeetCode(131. Palindrome Partitioning)题解
------
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

    Input: "aab"
    Output:
    [
        ["aa","b"],
        ["a","a","b"]
    ]

## 解题报告
给一个字符串，将其分成不同的子串，每个子串都是一个回文串。找出所有的这样的组合。

直接暴力搜索，首先取第一个字符串和剩下的，然后取两个和剩下的，然后三个和剩下的，···。如果到最后字符都是合适的话，就直接存储，否则就直接返回。

代码如下：

Runtime: 68 ms, faster than 21.88% of C++ online submissions for Palindrome Partitioning.
Memory Usage: 83.9 MB, less than 7.46% of C++ online submissions for Palindrome Partitioning.

```c++
class Solution {
public:
    vector<vector<string>> res;
    bool isPalindrome(string s, int sta, int end){
        if(sta >= end) return true;
        return s[sta]==s[end] && isPalindrome(s, sta+1, end-1);
    }
    void partition_(string s, int end, int sta, vector<string> tmp){
        if(sta > end){
            res.push_back(tmp);
            return;
        }
        tmp.push_back(s.substr(sta, 1));
        partition_(s, end, sta+1, tmp);
        for(int i=sta+1; i<=end; i++){
            if(isPalindrome(s, sta, i)){
                tmp[tmp.size()-1] = s.substr(sta, i-sta+1);
                partition_(s, end, i+1, tmp);
            }
        }
        return;
    }
    vector<vector<string>> partition(string s) {
        vector<string> tmp;
        partition_(s, s.size()-1, 0, tmp);
        return res;
    }
};
```

BitBrave, 2019-07-14
# LeetCode(14. Longest Common Prefix)题解

------

原文如下：
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

    Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

## 解题思路（easy, 直接比较即可。）代码如下：

```c++
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0) return "";
        string com_pre = "";
        int slen = INT_MAX;
        // find shortest string in vector
        for(int i = 0; i<strs.size(); i++) slen = (slen < strs[i].size()) ? slen : strs[i].size();
        if (slen == INT_MAX) return "";
        
        for(int i = 0; i<slen; i++){
            char a = strs[0][i];
            for(int p = 1; p<strs.size(); p++){
                if(strs[p][i] != a) return com_pre;
            };
            com_pre += a;
        }
        return com_pre;
    }
};
```
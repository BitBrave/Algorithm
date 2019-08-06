# LeetCode(151. Reverse Words in a String)题解
------
Given an input string, reverse the string word by word.

Example 1:

    Input: "the sky is blue"
    Output: "blue is sky the"
Example 2:

    Input: "  hello world!  "
    Output: "world! hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

    Input: "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
    

Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.
    
Follow up:

    For C programmers, try to solve it in-place in O(1) extra space.

## 题意理解
给一个字符串，按照word为单位将其反序。

不需要考脑子的题目，只需要细致就可以

代码如下：

Runtime: 12 ms, faster than 41.62% of C++ online submissions for Reverse Words in a String.
Memory Usage: 69.4 MB, less than 6.55% of C++ online submissions for Reverse Words in a String.

```c++
class Solution {
public:
    string reverseWords(string s) {
        if(s=="") return s;
        int sta = 0, loc;
        while(sta<s.size() && s[sta]==' ') sta++;
        if(sta == s.size()) return "";
        loc = s.find(' ', sta);

        if(loc == string::npos) return s[0] == ' ' ? s.substr(1) : s;
        s = reverseWords(s.substr(loc+1)) + " " + s.substr(sta, loc-sta);
        
        if(s[0] == ' ') return s.substr(1);
        return s;
    }
};
```

BitBrave, 2019-08-06
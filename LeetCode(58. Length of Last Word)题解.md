# LeetCode(58. Length of Last Word)题解
------
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

    Input: "Hello World"
    Output: 5

## 解题思路

Easy题，从后向前遍历，遇到空格就返回。注意要去掉String的最后面的空格。

```c++
class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = s.size();
        while(s[--len]==' ');

        int last = 0;
        while(len>=0 && s[len--]!=' ') last++;
        return last;
    }
};
```
BitBrave，2019-05-02
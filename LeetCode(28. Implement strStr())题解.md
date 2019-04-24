# LeetCode(28. Implement strStr())题解
------
原文如下：
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2
Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

## 题意思路
Easy题。第一次想得有点多，还是老思路，不应该自己造轮子。

```c++
class Solution {
public:
    bool isMatch(int sta, string h, int hl, string n, int nl){
        int j = 0;
        while(sta<hl && j<nl && h[sta++]==n[j++]);
        return j==nl && h[sta-1]==n[j-1];
    }
    int strStr(string haystack, string needle) {
        int hl = haystack.size(), nl = needle.size();
        for(int i=0; i<=hl-nl; i++){
            if(isMatch(i, haystack, hl, needle, nl)) return i;
        };
        return -1;
    }
};
```

其实有个更简单方式，利用string的substr。

```c++
class Solution {
public:
    int strStr(string haystack, string needle) {
        int hl = haystack.size(), nl = needle.size();
        for(int i=0; i<=hl-nl; i++){
            if(haystack.substr(i, nl)==needle) return i;
        };
        return -1;
    }
};
```

BitBrave, 2019-04-24。
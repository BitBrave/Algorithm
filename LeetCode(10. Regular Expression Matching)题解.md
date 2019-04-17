# LeetCode(10. Regular Expression Matching)题解

------
原文如下
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:

    s = "aa"
    p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
Example 2:

Input:

    s = "aa"
    p = "a*"
    Output: true
    Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:

    s = "ab"
    p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:

    s = "aab"
    p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:
Input:

    s = "mississippi"
    p = "mis*is*p*."
    Output: false

这题要求使用p去生成s，s是一串英文字符，p是由英文字符、*（前面的字符重复一次或多次）、.（任意字符，不能为空）。这可以使用动态规划的思想去解决，或者直接进行递归匹配。

我是采用递归的方式解决的。方法如下：
> * 如果p为空，s也为空时，表示匹配成功，返回True；
> * 如果p为空时，但是s不为空，表示匹配失败，因为此时已经没有办法用p来匹配s剩下的字符了，返回False。
> * 如果p的长度等于1，s应当是长度也为1并且满足s[0]==p[0]||p[0]=='.'，此时返回True，否则返回False。（其实这是为了满足后续分析不用考虑p的长度是否大于1的问题，保证后续处理时p的长度大于等于2。）

而一般的情况：
>* 如果S[0]==P[0] || P[0]=='.'，表示第一个字符是可以互相匹配的。此时判断P[1],如果不是‘\*’，表示P[0]并不能重复，那么直接使用同样的函数匹配S[1]和P[1]起始的各自的子串。如果P[1]=='\*'，表示P[0]可以重复0次或多次。那就存在两种情况，即匹配0或一/多次。所以可以分别运行函数匹配S[1]和P[2]开始子串、以S[1]和P[0]开始子串。但是我们只需要验证P是否能生成S，并不是要求完备性，所以只要一种情况出现True，即可返回，不用再继续试验其余情况。
> * 如果S[0]!=P[0] && P[0]!='\*',表示当前字符是不匹配的，就查看P[1]的值，如果P[1]=='\*',那还有救，可以让P[0]重复0次，跳过这个值，匹配S[0]和P[2]开始的子串。否则，P[1]!='\*'表示P[0]是不可跳过的，那就只能返回False。
> * 如果P[0]=='\*', 此时可以判断S[0]!=P[0]。注意我们在寻找P的子串时，总是尽量使得P[0]!='\*'，而唯一能使得P[0]=='\*'的情况出现就是给定的P有诸如'\*\*abc'、'a\*\*c\*def\*\*ded'等连续两个‘\*\*’出现。多个连续的‘\*’其实是没意义的，所以此时可以直接跳过，运行函数匹配S[0]和P[1]开始的子串。

对应的代码为如下——

```c++
class Solution {
    
public:
    bool isMatch(string s, string p) {
        if(p.empty()) return s.empty();
        if(p.length() == 1) return s.length()==1 && (s[0]==p[0] || p[0]=='.');
        
        if(s.empty()){
            if(p[0]=='*') return isMatch(s, p.substr(1));
            else return p[1]=='*' && isMatch(s, p.substr(2));
        };
        
        // s is not empty, p is not empty
        if(s[0]==p[0] || p[0]=='.'){
            if(p[1] != '*') return isMatch(s.substr(1), p.substr(1));
            if(isMatch(s, p.substr(2))) return true;
            while(isMatch(s.substr(1), p)) return true;
            
            return false;
        };
        if(s[0]!=p[0] && p[0]!='*') return p[1]=='*' && isMatch(s, p.substr(2));
        else return isMatch(s, p.substr(1));
    };
};
```

PS：使用C++代码实现时，可以使用string的substr函数寻找子串。

还有一种使用动态规划的思路——
定义一个二维的DP数组，其中dp[i][j]表示s[0,i)和p[0,j)是否match，然后有下面三种情况(下面部分摘自这个帖子)：

    1.  P[i][j] = P[i - 1][j - 1], if p[j - 1] != '*' && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
    2.  P[i][j] = P[i][j - 2], if p[j - 1] == '*' and the pattern repeats for 0 times;
    3.  P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'), if p[j - 1] == '*' and the pattern repeats for at least 1 times.
链接在此：<https://leetcode.com/problems/regular-expression-matching/discuss/5684/c-on-space-dp>

BitBrave, 2019-04-16.
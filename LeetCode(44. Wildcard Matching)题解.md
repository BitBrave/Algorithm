# LeetCode(44. Wildcard Matching)题解
------
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

    Input:
    s = "aa"
    p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
Example 2:

    Input:
    s = "aa"
    p = "*"
    Output: true
    Explanation: '*' matches any sequence.
Example 3:

    Input:
    s = "cb"
    p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

    Input:
    s = "adceb"
    p = "*a*b"
    Output: true
    Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

    Input:
    s = "acdcb"
    p = "a*c?b"
    Output: false

## 解题思路

Hard，要求给定一个字符串s，在给定一个包含通配符？和*的字符串，判断p是否能匹配s，其中？表示匹配任何字符，不能为空，*表示匹配0个或多个任意字符。

以下是自己的思考：

可以如下操作，使用递归函数，各自从s和p的头部开始向后遍历，假设当前走到了位置i和j，s和p的长度各为s1和p1。

如果j大于等于p1，表示p遍历完，若s未完，返回false，否则true

如果j小于等于p1，而s已经遍历完，查看j+1及其之后是否全为*，是则true，否则false

如果j小于等于p1，而s还未遍历完，则查看当前字符，如果j对应的不为？或者*，查看是否和i对应的相等，是则j+1，i+1继续遍历，否则就返回false。如果j对应的？，直接i+1，j+1。如果对应的*，就有三种情况，不匹配，查看i，j+1，匹配1次，i+1，j+1，匹配多次，i+1，j。只要这三种情况一种满足即可，因此取或。

上述的操作，但是等于遍历了所有的可能性，特别是遇到了多个*的时候，因此在处理的时候可以将多个挨着的*删减为1个。但是这样处理也会超时，可能这就是为什么是Hard吧。

以下是网上查询之后得到的思路：

因此还需要思考一下，当我们遇到*的时候，总是会有匹配一次，匹配多次，一次都不匹配三种选择，原则上来说，一个*可以匹配任意一个字符串。因此，可以使用一个贪心的算法。我们在遍历的时候，遇到*，总是先一次都不匹配，然后遇到不匹配的时候，我们往回走，去使用*匹配一次，再重新走一遍。但是这里有一个trick，因为*可以匹配任意字符串，所以我们只需要回退到最近的*就可以了，因为这个*可以模拟前面的*在当前这个位置之后的所有可以匹配出的所有情况

代码如下：

Runtime: 12 ms, faster than 96.74% of C++ online submissions for Wildcard Matching.
Memory Usage: 8.8 MB, less than 89.78% of C++ online submissions for Wildcard Matching.

```C++
class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, slen = s.size(), j = 0, plen = p.size(), lastj = -1, lasti = 0;
        
        while(i<slen){
            if((j<plen) && ((p[j]=='?') || (s[i]==p[j]))){
                i++; j++;
            }
            else if(j<plen && p[j]=='*'){
                lastj = j;
                lasti = i;
                j++;
            }
            else if(lastj != -1){
                j = lastj + 1;
                lasti++;
                i = lasti;
            }
            else return false;
        }
        while(j<plen && p[j]=='*') j++;
        return j==plen;
    }
};
```
这道题也可以使用动态规划的问题，使用一个二维数组就跟求编辑距离一样，ij表示s的前i个字符和p的前j个字符是否匹配。但是实际实现的时候会出现内存溢出的问题，因此可以使用一个1*2的数组，因为每一个位置的只需要前面一个位置的结果而已。

（PS：DP问题，先用简单的办法想出可以解的方案，再逐步优化即可。这道题可以先用二维数组，再慢慢优化！这是一个很重要的方法和思考的办法）

这里也有一个更好的办法，只使用一个1维数组。M的长度与S一致，用一个循环遍历P，M就记录S的前i个字符与P当前遍历过的字符是否匹配。当遍历结束，返回M的最后一个结果，记住每遍历一次就更新一次M。当然也可以用M记录P的前i个字符与S当前遍历过的字符是否匹配，当遍历结束返回M的最后一个结果。这里我只实现了第一种。

代码如下：

Runtime: 64 ms, faster than 55.45% of C++ online submissions for Wildcard Matching.
Memory Usage: 9.2 MB, less than 83.74% of C++ online submissions for Wildcard Matching.

```c++
class Solution {
public:
    bool isMatch(string s, string p) {
        int slen = s.size(), plen = p.size(), i;
        
        if(plen==0) return slen==0;

        vector<bool> M(slen+1, false);
        M[0] = true;
        
        for(int j=0; j<plen; j++){
            if(p[j] == '*'){
                i = 0;
                while(i<slen+1 && M[i]!=true) i++;
                while(i<slen+1) M[i++] = true;
            }
            else{
                for(i=slen-1; i>=0; i--)
                    M[i+1] = M[i] && (s[i]==p[j] || p[j]=='?');
            }
            M[0] = M[0] && p[j]=='*';
        }
        return M[slen];
    }
};
```

BitBrave, 2019-05-25. 我真是越来越优秀了。
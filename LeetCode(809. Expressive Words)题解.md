# LeetCode(809. Expressive Words)题解
------
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

    Example:
    Input: 
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    Output: 1
    Explanation: 
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
    

Notes:

    0 <= len(S) <= 100.
    0 <= len(words) <= 100.
    0 <= len(words[i]) <= 100.
    S and all words in words consist only of lowercase letters

## 解题思路
给一个字符串，和一个字符串集合，查看是否可以用集合中的某个字符串内的组合通过加一些相同的字符（加过之后的组合长度要大于等于3）之后是否可以等于给定的字符串。返回符合条件的个数。

单纯的字符串分析题，首先看一个字符串和给定的字符串的比较，长度一致肯定不可能，然后再挨个字符比较即可。

代码如下，时间复杂度O(n2), 空间复杂度O(1)，算上递归就是O(n).

Runtime: 16 ms, faster than 10.92% of C++ online submissions for Expressive Words.
Memory Usage: 18.1 MB, less than 14.29% of C++ online submissions for Expressive Words.

```c++
class Solution {
public:
    bool isMatch(string a, int al, int alen, string b, int bl, int blen){
        if(al == alen) return bl == blen;
        if(bl == blen) return al == alen;
        if(a[al] != b[bl]) return false;
        int b_num = 1;
        while(bl+b_num < blen && b[bl]==b[bl+b_num]) b_num++;
        int a_num = 1;
        while(al+a_num < alen && a[al]==a[al+a_num]) a_num++;
        if(a_num==b_num || a_num>2) return isMatch(a, al+a_num, alen, b, bl+b_num, blen);
        return false;
    }
    int expressiveWords(string S, vector<string>& words) {
        int len = words.size(), res = 0;
        for(int i=0; i<len; i++){
            if(S.size()<=words[i].size()) continue;
            if(isMatch(S, 0, S.size(), words[i], 0, words[i].size())) res++;
        }
        return res;
    }
};
```

BitBrave, 2019-09-01
# LeetCode(76. Minimum Window Substring)题解
------
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## 解题思路
给两个字符串S和T，判断字符串S内包含T的最小的子字符串，并返回。如果不包含返回“”。

可以使用双指针的办法做到O(n)的时间复杂度。
首先建立两个map，MS和MP，分别记录S内和T内各个字符的数目

然后采用如下规则更新left和right。初始化left=right=0，从左到右遍历S。

查看遍历的字符是否在T内并且MT[S[right]]>0，在就MT[S[right]]--，对应的记录T的个数的变量tcount--,然后right++，重复上述过程，直到tcount=0。表示此时left和right之间的S的子串包含了所有的T。

然后正式施行双指针法。重新用整个T更新MT，用left和right之间的字符更新MS，用scount = right-left+1。用一个begin和end记录最窄的S内包含T的子字符串。查看S[left]是否在T内（MT[S[left]]>0），不在的话就直接left++。

如果在的话，就将MS[S[left]]--,然后left++，scount--;此时查看left和right之间是否满足T(tcount<=scount; MT[S[left-1]]<=MS[S[left]])。如果满足就更新begin和end。如果不满足表示当前left和right之间的数是不能覆盖T的。这时候就将right++，并进行操作scount++，MS[S[right]]++。直到满足覆盖T的条件。再更新begin和end。

当right到达最后，在此要求right++时，就直接返回。或者left>=right时，也直接返回。最后返回S[begin,end]之间的字符即可。

同时因为给出的题目内是字母或者ASCLL字符。所以可以直接使用一个vector[128]的数组，这样也很方便。我偷懒就使用了这样的方式。

代码如下：

Runtime: 8 ms, faster than 97.89% of C++ online submissions for Minimum Window Substring.
Memory Usage: 10.2 MB, less than 42.93% of C++ online submissions for Minimum Window Substring.

```c++
class Solution {
public:
    string minWindow(string s, string t) {
        if(s=="" || t=="") return "";
        int tcount = t.size(), slen = s.size(), tlen = t.size(), left = 0, right = 0, begin = 0, end = 0;
        vector<int> MS(128, 0), MT(128, 0);
        
        for(int i=0; i<tlen; i++) MT[t[i]]++;
        while(tcount>0 && right<slen){
            if(MT[s[right]] > 0) {
                MT[s[right]]--;
                tcount--;
            }
            right++;
        }
        if(tcount>0) return "";
        end = --right;

        for(int i=0; i<tlen; i++) MT[t[i]]++;
        for(int i=left; i<=right; i++) MS[s[i]]++;
        while(right<slen){
            if(MT[s[left]]==0){
                left++;
                if(right-left<end-begin){
                    begin = left; end = right;
                }
                continue;
            }
            MS[s[left]]--;
            while(MS[s[left]]<MT[s[left]] && right+1 < slen) MS[s[++right]]++;
            
            if(MS[s[left]]<MT[s[left]]) break;
            
            left++;
            if(right-left<end-begin){
                begin = left; end = right;
            }
        }
        return s.substr(begin, end-begin+1);
    }
};
```

BitBrave, 2019-06-24
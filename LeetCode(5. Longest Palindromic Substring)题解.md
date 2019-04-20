# LeetCode(5. Longest Palindromic Substring)题解

------
原文如下：
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
Example 2:

    Input: "cbbd"
    Output: "bb"

## 题目思路，就是返回一个string内的最长的回文串而已。这个题是Medium，一般一个写得快一点的O(n2)的就可以AC，一个比较精巧的就是线性时间复杂度。

## O(n2)的解法
以每个字符为中心，从中间向两边遍历，直到遇到不相等的，然后记录下这个子串。遍历完所有字符之后得到最长的奇数子串。然后以每两个相邻的相同的字符为中心，再向两边遍历，得到最长的偶数子串。最后两个子串比较得到最长的回文串。这个方法需要一些技巧，比如不要每次都赋值记录子串，这样会消耗很多不比必要的时间，从而不能AC，可以只记录位置，最后找到最长的子串位置，再赋值即可。

代码如下：

```c++
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size()==0) return "";
        string res(1, s[0]);
        int len = s.size(), rl = 1;
        
        // odd
        for(int i=1; i<len; i++){
            string t(1, s[i]);
            int left = i-1, right = i+1;
            for(; left>=0 && right<len && s[right]==s[left]; left--, right++);
            left++; right--;
            if(right - left + 1 > res.size()) res =  s.substr(left, right - left + 1);
        };
        // even
        for(int i=1; i<len; i++){
            if(s[i-1]!=s[i]) continue;
            if(2 > res.size()) res = s.substr(i-1, 2);
            
            int left = i-2, right = i+1;
            for(; left>=0 && right<len && s[right]==s[left]; left--, right++);
            left++; right--;
            if(right - left + 1 > res.size()) res = s.substr(left, right - left + 1);
        };
        return res;
    }
};
```
## O(n)的
这里也有一个线性时间复杂度的，详细的博客如下：<https://blog.csdn.net/haut_ykc/article/details/52137496>

对应的代码如下：

```c++
class Solution {
public:
    string longestPalindrome(string s) {
        int ind_s = 0, ind_e = 0;
        const int max_len = 2010;
        char strOut[max_len];
        int p[max_len], mx_id, len_p;
        //pre-process
        len_p = proc(s, strOut);
        //manacher
        Manacher(p, strOut, len_p);
    
        int mx_flag = 0;
        for(int i = 0; i < len_p; i++){
            if(p[i]>mx_flag){
                ind_s = i;
                mx_flag = p[i];
            }
        }
        ind_e = p[ind_s] - 1;
        ind_s = (ind_s - p[ind_s])/2;
        return s.substr(ind_s, ind_e);
    }
    void Manacher(int *p, char *strOut, int len_p){
        int mx=0, mx_id = 0;
        
        for(int i = 0; i < len_p; i++)
        {
            p[i] = mx > i ? min(p[2*mx_id - i], mx - i) : 1;
            // cout<<"i+p[i] = "<<i+p[i]<<"; i-p[i] = "<<i-p[i]<<"; len_p = "<<len_p<<endl;
            while(i+p[i]<len_p && i-p[i]>=0 && strOut[i+p[i]]==strOut[i-p[i]]){
                p[i]++;
            }
            if(i + p[i] > mx){
                mx = i+p[i];
                mx_id = i;
            }
        }
    }
    int proc(string s, char *strOut)
    {
        int nLen = 1;
        strOut[0]='!';
        int i = 0;
        while(s[i] != '\0'){            
            strOut[nLen++]='#';strOut[nLen++]=s[i]; // process the string
            i++;
        }
        strOut[nLen++]='#';
        strOut[nLen]=0;
        return nLen;
    }
};
```

BitBrave, 2019-04-20. 
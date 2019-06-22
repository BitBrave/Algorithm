# LeetCode(93. Restore IP Addresses)题解
------
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

    Input: "25525511135"
    Output: ["255.255.11.135", "255.255.111.35"]

## 解题思路
给一个字符串，将其转换为对应的IP地址。

思路很简单，IP地址的四个值都不能大于255.四个值不长。直接暴力枚举就可以了。用一个函数，遍历字符串，看看在符合符合情况下能不能选完所有的字符数字。首先选一个数，然后选两个，最多三个，因为四个以上的肯定大于255了。如果选到最后可以遍历完字符串，就直接存储下来，否则放弃。

具体代码如下：

Runtime: 4 ms, faster than 86.40% of C++ online submissions for Restore IP Addresses.
Memory Usage: 9 MB, less than 18.74% of C++ online submissions for Restore IP Addresses.

```c++
class Solution {
public:
    void IpAddresses(string s, int sta, int len, vector<string> &res, string tmp1, int point){
        if(point>=4 && sta<len) return;
        if(sta>=len){
            if(point==4) res.push_back(tmp1.substr(0, tmp1.size()-1));
            return;
        }
        string tmp = tmp1;
        tmp += s[sta];
        tmp += '.';
        IpAddresses(s, sta+1, len, res, tmp, point+1);
        if(s[sta]=='0') return;
        if(sta+1<len){
            tmp = tmp1 + s[sta];
            tmp += s[sta+1];
            tmp += '.';
            IpAddresses(s, sta+2, len, res, tmp, point+1);
        }
        if(sta+2<len && (((s[sta]-'0')*100+(s[sta+1]-'0')*10+s[sta+2]-'0')<256)){
            tmp = tmp1 + s[sta];
            tmp += s[sta+1];
            tmp += s[sta+2];
            tmp += '.';
            IpAddresses(s, sta+3, len, res, tmp, point+1);
        }
        return;
    }
    vector<string> restoreIpAddresses(string s) {
        int len = s.size();
        vector<string> res;
        
        if(len > 12) return res;
        
        IpAddresses(s, 0, len, res, "", 0);
        return res;
    }
};
```

BitBrave, 2019-06-22
# LeetCode(30. Substring with Concatenation of All Words)题解
------
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

    Input:
    s = "barfoothefoobarman",
    words = ["foo","bar"]
    Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

    Input:
    s = "wordgoodgoodgoodbestword",
    words = ["word","good","best","word"]
    Output: []

## 解题思路
这是一个Hard题，要求给出一个字符串s和一个vector记录的相同长度的字符串。然后vector内的字符串随机组合之后的字符串是否是s的一个子串，如果是的话就记录下这个索引位置，最后返回一个vector。

这个题其实不难，可以只需要从头到尾遍历一下字符串，然后每次取一个固定长度的子串，看看这个子串是不是vector的字符串可以组合出来的，可以的话就记录下这个子串开始的位置。否则就看下一个，一个for循环就可以。

关键是如何判断一个字符串s是否可以由多个相同长度的字符串组合而成。这里我使用了map，将vector的各个字符串作为key，对应的个数作为value。只要依次从s中从前到后截取对应长度的子串看看在map中是否存在，最后判断是不是所有的子串都存在，且map中没有额外的存在了，就可以认为map中的字符串是可以组合而成的，否则就不能。

这样的代码可以AC，但花费了300MB内存，花费920ms。主要是map花费时间太多。

```c++
class Solution {
public:
    bool isStarting(string s, int wlen, map<string, int> mp, int vlen){
        string sstr;
        map<string, int>::iterator iter;
        
        for(int i=0; i<vlen; i++){
            sstr = s.substr(i*wlen, wlen);
            iter = mp.find(sstr);
            if(iter == mp.end()) return false;
            mp[sstr]--;
            if(mp[sstr] <= 0) mp.erase(sstr);
        }
        return true;
    }
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ret;
        int slen = s.size(), vlen = words.size(), wlen;
        if(slen==0 || vlen==0) return ret;
        wlen = words[0].size();
        if(wlen==0) return ret;

        map<string, int> mp;
        map<string, int>::iterator iter;
        
        for(int i=0; i<vlen; i++){
            iter = mp.find(words[i]);
            if(iter != mp.end()) mp[words[i]] += 1;
            else mp[words[i]] = 1;
        }
        
        slen -= wlen * vlen;
        
        for(int i=0; i<=slen; i++){
            if(isStarting(s.substr(i, wlen*vlen), wlen, mp, vlen)) ret.push_back(i);
        }
        return ret;
    }
};
```

但这个也有很多可以优化的地方，比如不在map里使用erase函数。代码如下（还是很慢）：

```c++
class Solution {
public:
    bool isStarting(string s, int wlen, map<string, int> mp, int vlen){
        string sstr;
        map<string, int>::iterator iter;
        
        for(int i=0; i<vlen; i++){
            sstr = s.substr(i*wlen, wlen);
            iter = mp.find(sstr);
            if(iter == mp.end()) return false;
            mp[sstr]--;
            if(mp[sstr] < 0) return false;
        }
        return true;
    }
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ret;
        int slen = s.size(), vlen = words.size(), wlen;
        if(slen==0 || vlen==0) return ret;
        wlen = words[0].size();
        if(wlen==0) return ret;

        map<string, int> mp;
        map<string, int>::iterator iter;
        
        for(int i=0; i<vlen; i++){
            iter = mp.find(words[i]);
            if(iter != mp.end()) mp[words[i]] += 1;
            else mp[words[i]] = 1;
        }
        
        slen -= wlen * vlen;
        
        for(int i=0; i<=slen; i++){
            if(isStarting(s.substr(i, wlen*vlen), wlen, mp, vlen)) ret.push_back(i);
        }
        return ret;
    }
};
```

BitBrave，2019-05-05。
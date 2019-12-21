# LeetCode(\140. Word Break II)题解

Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, add spaces in *s* to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

**Note:**

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

**Example 1:**

```
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
```

**Example 2:**

```
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
```

**Example 3:**

```
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
```

## 解题思路

给一个字符串s和一个单词字典Set。对s中某些字符处加上空格，使之每个单词都存在于字典Set中。找出所有的加空格方案，如果不存在就返回空数组。

这个题使用DP解决。构建一个状态数组D，D(i+1)记录字符串s中0~i的所有组合方案。那么最后返回D(s.size())即可。如何填充这个数组呢？

- 填充D(i)，设定j=0,1,2,...,i.判断单词s(j,i)在不在字典内，如果在就将D(j)中所有单词方案后面加上单词s(j,i)。
- 如果不在就选择下一个j。

按照上述的办法在一个函数内理论上是可行的，但是提交的时候内存爆了。网上查了才发现一样的办法使用dfs就没有问题，我猜想应该是递归时C++会分配更多的空间，或者说不算内存限制，从而可以避免超出内存。因此我将代码改成了dfs 形式，但是内核和上述是完全一样的。

代码如下，假设s的长度为N，时间复杂度最好为O(n2)，空间复杂度为最好为O(N2)。如果字典特别大，那方案就会特别多，就是指数级的时间复杂度和空间复杂度O(N!)。

`Runtime: 32 ms, faster than 24.42% of C++ online submissions for Word Break II.`

`Memory Usage: 21.5 MB, less than 6.06% of C++ online submissions for Word Break II.`

```c++
class Solution {
public:
    vector<string> dfs(string s, int end, unordered_set<string> Set, unordered_map<int,vector<string>>& D) {
        if(D.find(end+1) != D.end()) return D[end+1];
        vector<string> res;
        for(int i=end; i>=0; i--){
            string t = s.substr(i, end-i+1);
            if(Set.find(t) != Set.end()){
                if(i == 0) res.push_back(t);
                vector<string> tmp=dfs(s, i-1, Set, D);
                for(string ss:tmp){
                    res.push_back(ss + " " + t);
                }
            }
        }
        D[end+1] = res;
        return res;
    };
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int len = s.size();
        unordered_set<string> Set(wordDict.begin(), wordDict.end());
        unordered_map<int, vector<string>> D;
        D[0] = vector<string>();
        
        vector<string> res = dfs(s, len-1, Set, D);
        return res;
    }
    
};
```

BitBrave，2019-12-21
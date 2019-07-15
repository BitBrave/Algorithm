# LeetCode(139. Word Break)题解
------
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
Example 1:

    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                Note that you are allowed to reuse a dictionary word.
Example 3:

    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false

## 解题思路
给出一个字符串，和一个单词的字典。查看是否能将字符串由单词组成。

可以使用DP的办法。用一个和字符串长度一致的数组记录。元素D[i]表示前i个字符是否能由字典组成。

初始化D中元素全部为false。

D[0] = true

假设已经完成了D[i], 当完成D[i+1]时，查看第i+1个字符是否在字典内，在则D[i+1] = D[i]，如果结果为true就结束. 如果不在或者为false，则计算第i，i+1个字符组合是否在字典内。依旧按照上述判断。直到走到头。

代码如下：

Runtime: 12 ms, faster than 63.36% of C++ online submissions for Word Break.
Memory Usage: 11.9 MB, less than 58.91% of C++ online submissions for Word Break.

```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int len = s.size();
        vector<bool> D(len+1, false);
        D[0] = true;
        for(int i=0; i<len; i++){
            for(int j=i; j>=0; j--){
                if(find(wordDict.begin(), wordDict.end(), s.substr(j, i-j+1)) != wordDict.end()){
                    D[i+1] = D[j];
                    if(D[i+1] == true) break;
                }
            }
        }
        return D[len];
    }
};
```

BitBrave, 2019-07-15
# LeetCode(890. Find and Replace Pattern)题解

1. You have a list of `words` and a `pattern`, and you want to know which words in `words` matches the pattern.

   A word matches the pattern if there exists a permutation of letters `p` so that after replacing every letter `x` in the pattern with `p(x)`, we get the desired word.

   (*Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.*)

   Return a list of the words in `words` that match the given pattern. 

   You may return the answer in any order.

    

   **Example 1:**

   ```
   Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
   Output: ["mee","aqq"]
   Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
   "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
   since a and b map to the same letter.
   ```

    

   **Note:**

   - `1 <= words.length <= 50`
   - `1 <= pattern.length = words[i].length <= 20`

## 解题思路

有一个单词列表和一个模式，并且想知道单词中哪些单词与该模式匹配。如果在模式中将每个字母x替换为对应单词中的字母之后，能获得所需的单词就表明这个单词是符合模式的。（字母的排列是字母到字母的双射：每个字母都映射到另一个字母，没有两个字母映射到同一字母。）返回与给定模式匹配的单词列表。可以按任何顺序返回答案。

这个题可以使用匹配的方式，依次对每一个单词进行匹配，如果符合就放入结果中。

如何来构建这样的函数呢，我们可以分别从模式和要匹配的单词的第一个字母开始，如果对相同位置上的字母建立一个映射，如果走到最后没有多个字母映射到一个或者一个映射到多个就表明这个是符合的，即一一对应。否则就不匹配。

代码如下，设一个单词长度为N，时间复杂度O(N)，空间复杂度为O(N)。

`Runtime: 8 ms, faster than 37.31% of C++ online submissions for Find and Replace Pattern.`

`Memory Usage: 9.6 MB, less than 81.82% of C++ online submissions for Find and Replace Pattern.`

```C++
class Solution {
public:
    bool isMatch(string w, string p, int len){
        map<char, char> M, rM;
        for(int i=0; i<len; i++){
            if(M.find(p[i]) == M.end() && rM.find(w[i]) == rM.end()){
                M[p[i]] = w[i];
                rM[w[i]] = p[i];
            }
            if(M[p[i]] != w[i] || rM[w[i]] != p[i]) return false;
        }
        return true;
    }
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> ret;
        int len = pattern.size();
        for(auto word : words){
            if(isMatch(word, pattern, len)) ret.push_back(word);
        }
        return ret;
    }
};
```

BitBrave，2019-10-20
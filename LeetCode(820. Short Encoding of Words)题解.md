# LeetCode(820. Short Encoding of Words)题解

Given a list of words, we may encode it by writing a reference string `S` and a list of indexes `A`.

For example, if the list of words is `["time", "me", "bell"]`, we can write it as `S = "time#bell#"` and `indexes = [0, 2, 5]`.

Then for each index, we will recover the word by reading from the reference string from that index until we reach a `"#"` character.

What is the length of the shortest reference string S possible that encodes the given words?

**Example:**

```
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
```

**Note:**

1. `1 <= words.length <= 2000`.
2. `1 <= words[i].length <= 7`.
3. `Each word has only lowercase letters.`

## 解题思路

给出一个字符串列表，用一个大的字符串去表示这些字符串，给出一个等长的列表，然后每个字符串对应一个索引，这个索引到“#”之间的字符 就是原有的对应的字符串。求这样的字符串的最短是多少。

可以知道，如果我们将每个字符串依次排列就以“#”链接，可以得到一个长字符串，可以表示每个字符串。但是这样并不是最短的，就和example一样，字符串之间有公共的字母。但是可以注意到的是，字符串之间如果公用一个“#”，那么这两个字符串之间一定是一个是另一个的后缀。那么我们可以用一个set来记录这些字符串。然后查看每个字符串的后缀，如果在set内，就删除这个。遍历完成之后，将set内所有字符串用“#”即可满足条件了。

代码如下，时间复杂度$O(n^2)$,空间复杂度$O(n)$：

`Runtime: 124 ms, faster than 30.03% of C++ online submissions for Short Encoding of Words. Memory Usage: 16.6 MB, less than 100.00% of C++ online submissions for Short Encoding of Words.`

```C++
class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        set<string> S(words.begin(), words.end());
        string t;
        int l, res = 0;
        for(string s:words){
            l = s.size();
            for(int i=1; i<l; i++){
                t = s.substr(i);
                if(S.find(t) != S.end()) S.erase(t);
            }
        }
        for(string s:S) res += s.size() + 1;
        return res;
    }
};
```

BitBrave, 2019-09-08


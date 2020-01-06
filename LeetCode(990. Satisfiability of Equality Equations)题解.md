# LeetCode(\990. Satisfiability of Equality Equations)题解

Given an array equations of strings that represent relationships between variables, each string `equations[i]` has length `4` and takes one of two different forms: `"a==b"` or `"a!=b"`. Here, `a` and `b` are lowercase letters (not necessarily different) that represent one-letter variable names.

Return `true` if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 



**Example 1:**

```
Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
```

**Example 2:**

```
Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
```

**Example 3:**

```
Input: ["a==b","b==c","a==c"]
Output: true
```

**Example 4:**

```
Input: ["a==b","b!=c","c==a"]
Output: false
```

**Example 5:**

```
Input: ["c==c","b==d","x!=z"]
Output: true
```

 

**Note:**

1. `1 <= equations.length <= 500`
2. `equations[i].length == 4`
3. `equations[i][0]` and `equations[i][3]` are lowercase letters
4. `equations[i][1]` is either `'='` or `'!'`
5. `equations[i][2]` is `'='`

## 解题思路

给出一系列X==Y，X！=Y的等式或者不等式，判断这些等式里是否存在矛盾关系。

这个题明显就是使用Union find来解决，但是说实话我对并查集没有仔细了解过。不过我估摸着我实现的办法和并查集也差不了多少。

使用一个Map，首先遍历给的数据中的所有等式，对于相等的字符使得其Map的val都是一个值。然后遍历数据中的所有不等式，判断是不是存在字符一样或者在map中的val一样，这样就出现矛盾了，返回False。如果到最后都没有这样的情况出现，返回True。

代码如下，时间复杂度O(n)，空间复杂度O(1)，因为只有26个字母。

`Runtime: 8 ms, faster than 69.97% of C++ online submissions for Satisfiability of Equality Equations.`

`Memory Usage: 9.5 MB, less than 100.00% of C++ online submissions for Satisfiability of Equality Equations.`

```c++
class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        int len = equations.size(), label = 0;
        map<char, int> M;
        for (string s : equations) {
            if (s[1] == '!') continue;
            if (M.find(s[0]) != M.end() and M.find(s[3]) == M.end()) M[s[3]] = M[s[0]];
            else if (M.find(s[3]) != M.end() and M.find(s[0]) == M.end()) M[s[0]] = M[s[3]];
            else if (M.find(s[3]) != M.end() and M.find(s[0]) != M.end()) {
                map<char, int>::iterator iter;
                int tmp = M[s[3]];
                iter = M.begin();
                
                while(iter != M.end()) {
                    if(iter->second == tmp) M[iter->first] = M[s[0]];
                    iter++;
                }
            } else {
                M[s[0]] = M[s[3]] = label;
                label++;
            }
        }
        
        for (string s : equations) {
            if (s[1] == '=') continue;
            //cout<<M[s[0]]<<M[s[3]]<<endl;
            if (s[0] == s[3] or M.find(s[0]) != M.end() and M.find(s[3]) != M.end() and M[s[0]] == M[s[3]]) return false;
        }
        return true;
    }
};
```

BitBrave，2020-01-06
# LeetCode(763. Partition Labels)题解

A string `S` of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



**Example 1:**

```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```



**Note:**

1. `S` will have length in range `[1, 500]`.
2. `S` will consist of lowercase letters (`'a'` to `'z'`) only.

## 解题思路

给定一个全部是小写字母的标签，然后对其进行分区。每个字母只能最多在一个分区内出现，问最后要分成多少区。

这个题可以使用类似于Greedy的方法做。首先遍历整个字符串，记录每个字符在字符串中出现的最晚位置。

遍历完成后，再次从头遍历一遍字符串，每遇到一个字符，都查看这个字符在字符串中的最后一个位置，然后查看这个位置到当前字符之间的所有字符，维持一个最大值，使得所有字符都一个区间内。这样走到最后就是一个分区。然后继续向下走，直到最后。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Partition Labels.`

`Memory Usage: 8.6 MB, less than 96.77% of C++ online submissions for Partition Labels.`

```C++
class Solution {
public:
    vector<int> partitionLabels(string S) {
        int len = S.size();
        vector<int> ret, lastP(26, -1);
        for(int i=0; i<len; i++) lastP[S[i]-'a'] = i;
        
        int L, j;
        for(int i=0; i<len; i++){
            j = i;
            L = lastP[S[j]-'a'];
            while(j < L){
                L = max(lastP[S[j]-'a'], L);
                j++;
            }
            ret.push_back(L - i + 1);            
            i = j;
        }
        return ret;
    }
};
```

BitBrave, 2019-10-16
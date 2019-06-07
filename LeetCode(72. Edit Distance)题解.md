# LeetCode(72. Edit Distance)题解
------
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
Example 1:

    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
Example 2:

    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')

## 解题思路
Hard，求编辑距离。两个字符串AB配对，可以通过跳过插入错配等方式计算两个字符串的编辑距离。如果完全一样就为0，如果有一个错配，插入，跳过，编辑距离就+1.距离应该尽可能小。

本题是典型的DP问题。可以用一个大小分别为两个字符串的长度的矩阵D，D[i][j]表示A字符串0～i和B字符串0～j之间的编辑距离，那么最优子结构性质就为D[i][j] = min(D[i-1][j-1]+A[i]==B[j] ? 0:1, D[i][j-1]+1, D[i-1][j]+1).而处理边界问题时，可以将矩阵设为两个字符串长度+1，然后D[0][j]表示A空字符串与B比较，那么D[0][i] = i+1,同理D[i][0] = i+1.

因为更新后面的值只用到了两列，因此可以只使用两列数组就可以了。

代码如下：

Runtime: 12 ms, faster than 90.67% of C++ online submissions for Edit Distance.
Memory Usage: 9.5 MB, less than 78.82% of C++ online submissions for Edit Distance.

```c++
class Solution {
public:
    int minDistance(string word1, string word2) {
        int len1 = word1.size(), len2 = word2.size();
        if(len1 ==0 || len2 == 0) return max(len1, len2);
        //if(len1>len2){
        //    swap(word1, word2);
        //    swap(len1, len2);
        //}
        
        vector<vector<int>> res(len1+1, vector<int>(2));
        for(int i=0; i<len1+1; i++) res[i][0] = i;
        for(int j=0; j<len2; j++){
            res[0][1] = j + 1;
            for(int i=0; i<len1; i++){
                res[i+1][1] = res[i][0] + (word1[i]==word2[j] ? 0:1);
                res[i+1][1] = min(res[i+1][1], 1 + min(res[i][1], res[i+1][0]));
            }
            for(int i=0; i<len1+1; i++) res[i][0] = res[i][1];
        }
        return res[len1][1];
    }
};
```

BitBrave, 2019-06-07
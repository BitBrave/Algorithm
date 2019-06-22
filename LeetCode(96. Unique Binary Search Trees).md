# LeetCode(96. Unique Binary Search Trees)题解
------
    Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

    Example:

    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

        1         3     3      2      1
        \       /     /      / \      \
        3     2     1      1   3      2
        /     /       \                 \
        2     1         2                 3

## 解题思路
给一个数n，求出可以存储值1-n的BST的树的数目。

思路很简单，可以也只能使用DP解决。用一个数组D，size为n的其中D[i]表示从1-i+1字符的可以存储的BST树多少。那么可以想象一下，一个BST有i个字符，一开始加入i+1字符，放在之前的一个树的根节点，之前的树的值都比这个数小，因此在左子树上。那么这时候有一共有D[i]种，然后将其左子树中移动一个最大的数过来到根节点上，对应的右节点肯定就是加入的i+1字符。这时候有D[i-1]*D[0]种，再次移动剩下的左子树中最大的到根节点上，则有D[i-2]*D[1]种。

因此，最优子结构性质为：

D[0] = 1; D[1] = 2

D[i] = D[i-1] + D[i-2]*D[0] + D[i-3]*D[1] + D[i-4]* D[2] + ... + D[0]*D[i-2] + D[i-1]

具体代码如下：

Runtime: 4 ms, faster than 78.43% of C++ online submissions for Unique Binary Search Trees.
Memory Usage: 8.4 MB, less than 21.66% of C++ online submissions for Unique Binary Search Trees.

```c++
class Solution {
public:
    int numTrees(int n) {
        if(n==0) return 0;
        vector<int> res(n, 1);
        
        for(int i=1; i<n; i++){
            int c = i-2;
            res[i] = 2*res[i-1];

            while(c-->=0) res[i] += res[c+1] * res[i-3-c];
        }
        return res[n-1];
    }
};
```

BitBrave, 2019-06-22
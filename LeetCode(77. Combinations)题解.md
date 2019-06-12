# LeetCode(77. Combinations)题解
------
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
    [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
    ]

## 解题思路

Medium，题目要求计算一个组合C(n，k)，从1到n中选k个数，将各种方式排出来。

可以使用递归的办法，首先拿出一个数，再从剩下的n-1个数里面选k-1个，知道k=0直接返回，然后将这些数组成一个vector。

代码如下：

Runtime: 132 ms, faster than 20.87% of C++ online submissions for Combinations.
Memory Usage: 68.6 MB, less than 15.54% of C++ online submissions for Combinations.

```c++
class Solution {
public:
    void combine_(vector<vector<int> > &res, vector<int> tmp, vector<int> Item, int sta, int end, int n, int k, int target) {
        if(k==0 || k>n) {
            if(tmp.size()==target) res.push_back(tmp);
            return;
        }
        
        combine_(res, tmp, Item, sta+1, end, n-1, k, target);
        tmp.push_back(Item[sta]);
        combine_(res, tmp, Item, sta+1, end, n-1, k-1, target);
        return;
    }
    vector<vector<int>> combine(int n, int k) {
        vector<int> Item(n, 1);
        for(int i=1; i<n; i++) Item[i] += i;
        vector<vector<int>> res;
        combine_(res, vector<int>(), Item, 0, n-1, n, k, k);
        return res;
        
    }
};
```

Bitbrave, 2019-06-12

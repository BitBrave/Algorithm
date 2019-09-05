# LeetCode(823. Binary Trees With Factors)题解



## 解题思路

带因子的二叉树个数计算。给定一个元素大于1且不重复的数组，用这些数构建二叉树，每个元素可以用0次和多次。构建的二叉树满足如下条件：除了叶子节点之外，每个节点等于两个孩子节点的乘积。问这样的二叉树一共有多少颗？

首先分析，假设给定的数组为A，长度为$n$，所有的元素单个组成一个二叉树肯定满足条件。其次，假设有一个二叉树不止只有一个节点，那么这个里面的非叶子节点的元素一定有因子是在$A$内的。从根节点往下，假设根节点root和左孩子left和右right满足条件，那么这个二叉树的一共的棵数就是组成left子树的二叉树棵数乘上right子树的棵数再乘2（因为可以交换位置，但如果不同就不能）。

因此，我们可以使用DP的办法。首先将A进行升序排序。然后建立一个与A等长的数组D，$D[i]$表示$A[0~i]$内满足条件的二叉树有多少棵。那么状态转移方程就如下：
$$
D[i] = 1 + D[j]*D[loc(\frac{A[i]}{A[j]})] \ PS:j\in [0, i-1]，loc为通过值寻找index的函数，\frac{A[i]}{A[j]}必须也在数组内，否则就不算。
$$
这样最后返回$\sum D[i](i \in [0, A.size()-1]$即可。loc函数的实现，可以使用map，以A的元素为key，对应的index为value。

代码如下，时间复杂度$O(n^2)$（排序花费$O(nlogn)$，填充D数组花费$O(n^2)$，最后计算花费$O(n)$） ，空间复杂度$O(n)$（Map和D）:

`Runtime: 280 ms, faster than 7.79% of C++ online submissions for Binary Trees With Factors.`

`Memory Usage: 9.9 MB, less than 100.00% of C++ online submissions for Binary Trees With Factors.`

```C++
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& A) {
        long long len = A.size(), res = 0, mode = 1000000007;
        
        vector<long long> D(len, 0);
        map<float, int> M;
        
        sort(A.begin(), A.end());
        for(int i=0; i<len; i++) M[A[i]] = i;
        D[0] = 1;
        res += D[0];
        for(int i=1; i<len; i++){
            D[i] = 1;
            for(int j=0; j<i; j++){
                if(M.find(1.0*A[i]/A[j]) == M.end()) continue;
                D[i] += D[j]*D[M[A[i]/A[j]]];
            }
            res += D[i];
            res %= mode;
        }
        return res;
    }
};
```

BitBrave, 2019-09-05
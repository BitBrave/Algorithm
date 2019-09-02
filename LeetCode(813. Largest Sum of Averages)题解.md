# LeetCode(813. Largest Sum of Averages)题解
------
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

    Example:
    Input: 
    A = [9,1,2,3,9]
    K = 3
    Output: 20
    Explanation: 
    The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
    We could have also partitioned A into [9, 1], [2], [3, 9], for example.
    That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 

Note:

    1 <= A.length <= 100.
    1 <= A[i] <= 10000.
    1 <= K <= A.length.
    Answers within 10^-6 of the correct answer will be accepted as correct.

## 解题思路

这道题给了我们一个数组，说是让我们将数组分成至多K个非空组，然后说需要统计的分数是各组的平均数之和，让我们求一个分割方法，使得这个分数值最大，当然这个分数值不一定是整型数。这道题限制了分割的组必须为非空组，至多分成K组。

首先可以想到，如果K 大于等于数组的长度，那么根本无需分组，因为这样才不会损失数据。如果K小于数组长度就需要进行分组. 而对于这种情况如何做呢。可以使用DP。

假设数组A的长度为lenA，要求分为K组，那么用大小为lenA*K的DP记录最优值，DP[i][k]表示A中1到i的元素中，最多分为k+1组时所得到的最优值。当i==0时，表示不分组

那么状态转移方程就是如下——

DP[i][k] = max(DP[i][k], DP[j][k-1]+sum(j, i-1, A)/(i-j));

代码如下，时间复杂度O(n4), 空间复杂度O(n2):

Runtime: 96 ms, faster than 5.08% of C++ online submissions for Largest Sum of Averages.
Memory Usage: 9.4 MB, less than 50.00% of C++ online submissions for Largest Sum of Averages.

```C++
class Solution {
public:
    double sum(int sta, int end, vector<int>& A){
        int res = 0;
        while(sta<=end) res += A[sta++];
        return res;
    }
    double largestSumOfAverages(vector<int>& A, int K) {
        int len = A.size();
        if(len<=K) return sum(0, len-1, A);
        vector<vector<double>> DP(len+1, vector<double>(K+1, 0));
        for(int i=1; i<=len; i++) DP[i][0] = sum(0, i-1, A)/i;
        for(int i=1; i<=len; i++){
            for(int k=1; k<K; k++){
                for(int j=0; j<=i; j++){
                    DP[i][k] = max(DP[i][k], DP[j][k-1]+sum(j, i-1, A)/(i-j));
                    //cout<<j<<" DP["<<i<<","<<k<<"]"<<": "<<DP[i][k]<<endl;
                }
            }
        }
        
        return DP[len][K-1];
    }
};
```

可以观察到，在K上，每次状态更新都只使用到了上一个K-1行的数据，因此可以将数组缩减为一维数组，同时，Sum可以用一个数组存储，从而避免重复计算。

代码如下，时间复杂度O(n3),空间复杂度O(n):

Runtime: 12 ms, faster than 63.89% of C++ online submissions for Largest Sum of Averages.
Memory Usage: 8.6 MB, less than 100.00% of C++ online submissions for Largest Sum of Averages.

```C++
class Solution {
public:
    double largestSumOfAverages(vector<int>& A, int K) {
        int len = A.size();  
        vector<double> DP(len+1, 0), Sum(len+1, 0);
        for(int i=1; i<=len; i++){
            Sum[i] = Sum[i-1] + A[i-1]; 
            DP[i] = Sum[i] / i;
        }
        if(len<=K) return Sum[len];
        
        for (int k = 1; k < K; k++) {
            for (int i = len; i >= 1; i--) {
                for (int j = i; j >=0; j--) {
                    DP[i] = max(DP[i], DP[j]+(Sum[i]-Sum[j])/(i-j)); 
                }
            }
        }
        
        return DP[len];
    }
};
```

BitBrave, 2019-09-03
# LeetCode(873. Length of Longest Fibonacci Subsequence)题解

A sequence `X_1, X_2, ..., X_n` is *fibonacci-like* if:

- `n >= 3`
- `X_i + X_{i+1} = X_{i+2}` for all `i + 2 <= n`

Given a **strictly increasing** array `A` of positive integers forming a sequence, find the **length** of the longest fibonacci-like subsequence of `A`.  If one does not exist, return 0.

(*Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].*)

 



**Example 1:**

```
Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
```

**Example 2:**

```
Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
```

 

**Note:**

- `3 <= A.length <= 1000`
- `1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9`
- *(The time limit has been reduced by 50% for submissions in Java, C, and C++.)*

## 解题思路

给一个递增的数字序列，求出其中最长的斐波那契子序列。

子序列不要求数据是挨着的，只要数据是保持顺序即可，因此我们可以首先使用最简单的办法。

使用一个set，记录数组中每个数字。然后依次从头到尾随便选两个数，然后作为斐波那契数列的前两个，开始向后寻找，因为数据是递增的，所以只需要向后找即可。每次计算两个数相加，查看在不在set内，在就继续往下找，不在就再另外选一对，这个过程中记住最长的合法数列。

一个小trick是，如果两个数相加大于A中最后一个数也就是最大的数，就没有必要再计算了，因为数据只会越来越大。

这样时间复杂度是O(n3)，空间复杂度O(n)，代码如下。

`Runtime: 288 ms, faster than 17.09% of C++ online submissions for Length of Longest Fibonacci Subsequence.`

`Memory Usage: 9.7 MB, less than 42.86% of C++ online submissions for Length of Longest Fibonacci Subsequence.`

```c++
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& A) {
        int len = A.size(), ret = 0;
        set<int> S;
        set<pair<int, int>> S_P;
        for(int a : A) S.insert(a);
        int a, b, s;
        for(int i=0; i<len; i++){
            for(int j=i+1; j<len; j++){
                if(A[i] + A[j] > A[len-1]) break;
                a = A[i];
                b = A[j];
                s = 2;
                while(b <= A[len-1] && S.find(a+b) != S.end()){
                    s++;
                    int tmp = a;
                    a = b;
                    b = tmp + b;
                }
                if(s >= 3) ret = max(ret, s);
            }
        }
        return ret;
    }
};
```

还有一种使用DP的办法，用一个二维数组DC,DC\[i\]\[j\]表示以A\[i\]和A\[j\]j结尾的最长的斐波那契数列长度，那么久很容易构造一个DP方程出来。这样的时间复杂度就是O(n2)，但是也有一个小Trick就是如果A\[j\]-A\[i\]大于等于A\[i\]的话，第二层循环就不用再寻找了，因为我们要找的值必须要比A\[i\]小。

代码如下，时间和空间复杂度理论上均为O(n2)，但加上Trick之后，效果提升很多。

`Runtime: 132 ms, faster than 76.28% of C++ online submissions for Length of Longest Fibonacci Subsequence.`

`Memory Usage: 62.5 MB, less than 14.29% of C++ online submissions for Length of Longest Fibonacci Subsequence.`

```C++
class Solution {
public:
    
    int lenLongestFibSubseq(vector<int>& A) {
        int len = A.size(), ret = 0;
        map<int, int> M;
        vector<vector<int>> DC(len, vector<int>(len, 0));
        for(int i=0; i<len; i++) M[A[i]] = i;
        
        for(int i=1; i<len; i++){
            for(int j=i+1; j<len; j++){
                if(A[j]-A[i] >= A[i]) break;
                if(M.find(A[j]-A[i]) == M.end() || M[A[j]-A[i]]>=i) continue;
                DC[i][j] = max(3, DC[M[A[j]-A[i]]][i] + 1);
                ret = max(ret, DC[i][j]);
            }
        }
        return ret;
    }
};
```

BitBrave，2019-11-04
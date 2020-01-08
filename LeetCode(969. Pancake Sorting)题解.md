# LeetCode(\969. Pancake Sorting)题解

Given an array `A`, we can perform a *pancake flip*: We choose some positive integer `**k** <= A.length`, then reverse the order of the first **k** elements of `A`. We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array `A`.

Return the k-values corresponding to a sequence of pancake flips that sort `A`. Any valid answer that sorts the array within `10 * A.length` flips will be judged as correct.

 

**Example 1:**

```
Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
```

**Example 2:**

```
Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
```

 

**Note:**

1. `1 <= A.length <= 100`
2. `A[i]` is a permutation of `[1, 2, ..., A.length]`

## 解题思路

给一个由1到N组成的乱序的一维数组，现在有一个煎饼的翻转办法，每次可以选择前K个数翻转，请给出一种翻转次数在10*N次内的办法，将数组变为升序。返回这个办法中每次选择的K值。

这个分析一下就可以想到，我每次找到当前数组中最大的数，选择这个位置及之前的数进行翻转，将其翻转到第一个位置，然后再翻转整个序列，就将最大的数翻转到最后面。后续的操作就不再管这个数，将倒数第二大的数翻转到第一个后再翻转整个序列-1的长度，以此类推我们最多翻转2*N-1次即可。

代码如下，时间复杂度为O(n2)。每次翻转花费O(n)时间，一共翻转n次，空间复杂度O(1)。

`Runtime: 8 ms, faster than 64.27% of C++ online submissions for Pancake Sorting.`

`Memory Usage: 8.5 MB, less than 100.00% of C++ online submissions for Pancake Sorting.`

```c++
class Solution {
public:
    void flip(int K, vector<int>& A) {
        for (int i=0; i<K; i++, K--) {
            swap(A[i], A[K]);
        }
    }
    vector<int> pancakeSort(vector<int>& A) {
        vector<int> ret;
        for (int n=A.size(); n>0; n--) {
            int i = 0;
            while (A[i] != n) i++;
            if (i == n - 1) continue;
            ret.push_back(i + 1);
            ret.push_back(n);
            flip(i, A);
            flip(n - 1, A);
        }
        return ret;
    }
};
```

BitBrave，2020-01-08.
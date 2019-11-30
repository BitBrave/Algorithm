# LeetCode(\1014. Best Sightseeing Pair)题解

Given an array `A` of positive integers, `A[i]` represents the value of the `i`-th sightseeing spot, and two sightseeing spots `i` and `j` have distance `j - i` between them.

The *score* of a pair (`i < j`) of sightseeing spots is (`A[i] + A[j] + i - j)` : the sum of the values of the sightseeing spots, **minus** the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

**Example 1:**

```
Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
```

 

**Note:**

1. `2 <= A.length <= 50000`
2. `1 <= A[i] <= 1000`

## 解题思路

有一个数组，每个元素相当于一个观光地，元素值对应观看的价值，元素的索引值的差代表两个观光地之间的距离。现在要找出两个观光地，价值之和减去距离值为所有两个观光地之间的相同值的最大。

这个题最暴力的解法就是遍历所有的两种组合，但这样时间复杂度O(n2)，我做的时候超时。

其实有一个非常简单的算法，我们从左到右遍历每个元素，然后用一个值去记录已经遍历数组中，到达当前观光地的价值最大的观光地的值，这个值是观光地的值减去其到当前元素位置的距离，这样就可以一次遍历解决，代码非常简单。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 68 ms, faster than 56.81% of C++ online submissions for Best Sightseeing Pair.`

`Memory Usage: 13.2 MB, less than 62.50% of C++ online submissions for Best Sightseeing Pair.`

```c++
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int ret = 0, max_a = 0;
        for(int a : A){
            ret = max(max_a + a, ret);
            max_a = max(max_a, a) - 1;
        }
        return ret;
    }
};
```

BitBrave，2019-11-30
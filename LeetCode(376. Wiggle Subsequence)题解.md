# LeetCode(\376. Wiggle Subsequence)题解

A sequence of numbers is called a **wiggle sequence** if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, `[1,7,4,9,2,5]` is a wiggle sequence because the differences `(6,-3,5,-7,3)` are alternately positive and negative. In contrast, `[1,4,7,2,5]` and `[1,7,4,5,5]` are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

**Example 1:**

```
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
```

**Example 2:**

```
Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
```

**Example 3:**

```
Input: [1,2,3,4,5,6,7,8,9]
Output: 2
```

**Follow up:**
Can you do it in O(*n*) time?

## 解题思路

给一个序列S，找出其中最长震荡子序列的长度。子序列元素可以不相邻，但必须保持相对顺序。震荡序列就是相邻元素之间的差值是+，-，+，-，+，-，...或者-，+，-，+，-，+，-，...。

这个题使用Greedy，我们可以这样想，如果我们找到一个数a，下一个想找一个比它小的数，那么这个数一定是越大越好，因为越大后面的数比它小的可能性就越大，反之想找大的数，我们就让a尽可能小。因此，思路就出来了。

从左到右遍历整个序列。我们维护一个数end，表示我们当前已遍历的序列内找到的最长子序列的最后一个数，并且用一个变量记录下一个数是需要比end大还是小。

因此遍历到数a时，如果a==end，就跳过，如果a>end而需要大的，下一次就需要小的，那么更新end=a，同时res++，因为序列+1。如果需要小的，那说明不能组成序列，需要丢弃一个，那肯定丢弃当前数中小的，因此还是end=a。

反之如果a<end而需要小的，下一次就需要大的，那么更新end=a，同时res++，因为序列+1。如果需要大的，那说明不能组成序列，需要丢弃一个，那肯定丢弃当前中大的，因此还是end=a。

因此上述的分析中得出来，end其实就一直在更新，不管怎么样，遍历下一个之前，end就等于前一个，因此每个元素直接和前一个比较就可以了。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Wiggle Subsequence.`

`Memory Usage: 8.7 MB, less than 40.00% of C++ online submissions for Wiggle Subsequence.`

```c++
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int res = 1, end = 0, len = nums.size();
        if (len <= 1) return len;
        
        int dir = 0;
        for (int i=1; i<len; i++) {
            if (nums[i] == nums[i-1]) continue;
            else if (dir==0 or (nums[i]>nums[i-1] and dir==1) or (nums[i]<nums[i-1] and dir==-1)) {
                res++;
                dir = nums[i]>nums[i-1] ? -1 : 1;
                
            }
        }
        return res;
    }
};
```

BitBrave，2019-12-27
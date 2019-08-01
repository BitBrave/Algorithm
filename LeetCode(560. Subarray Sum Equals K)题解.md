# LeetCode(560. Subarray Sum Equals K)题解
------
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

    Example 1:
    Input:nums = [1,1,1], k = 2
    Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

## 解题思路
给出数组，找出其中连续子数组之和为K的子数组个数。

可以使用最简单的办法，暴力搜索，从前到后，每次相加，看看其和是不是等于K，是就记录下来。时间复杂度O(n2)

代码如下：

Runtime: 480 ms, faster than 21.08% of C++ online submissions for Subarray Sum Equals K.
Memory Usage: 10 MB, less than 91.80% of C++ online submissions for Subarray Sum Equals K.

```c++
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int res = 0, len = nums.size(), sum;
        for(int i=0; i<len; i++){
            sum = 0;
            for(int j=i; j<len; j++){
                sum += nums[j];
                if(sum == k) res++;
            }
        }
        return res;
    }
};
```

还有一种更聪明的办法。使用哈希表以从头到尾的累积和为key，对应出现的次数为value。用一个哈希表来建立连续子数组之和跟其出现次数之间的映射，初始化要加入 {0,1} 这对映射，这是为啥呢，因为我们的解题思路是遍历数组中的数字，用 sum 来记录到当前位置的累加和，我们建立哈希表的目的是为了让我们可以快速的查找 sum-k 是否存在，即是否有连续子数组的和为 sum-k，如果存在的话，那么和为k的子数组一定也存在，这样当 sum 刚好为k的时候，那么数组从起始到当前位置的这段子数组的和就是k，满足题意，如果哈希表中事先没有 m[0] 项的话，这个符合题意的结果就无法累加到结果 res 中，这就是初始化的用途。

代码如下

Runtime: 52 ms, faster than 39.16% of C++ online submissions for Subarray Sum Equals K.
Memory Usage: 18.3 MB, less than 8.87% of C++ online submissions for Subarray Sum Equals K.

```c++
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int res = 0, sum = 0, n = nums.size();
        map<int, int> m{{0, 1}};
        for (int i = 0; i < n; ++i) {
            sum += nums[i];
            res += m[sum - k];
            ++m[sum]; 
        }
        return res;
    }
};
```

PS: Map对于不存在的数会输出0

BitBrave, 2019-08-01

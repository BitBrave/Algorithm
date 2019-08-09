#LeetCode(494. Target Sum)
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

    Example 1:
    Input: nums is [1, 1, 1, 1, 1], S is 3. 
    Output: 5
Explanation: 

    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

## 解题思路
给一个数组，每个元素可以加或者减，最终得到一个固定的结果，求一共有几种方式。

这就是一个深搜，遍历每种可能性。

代码如下：

Runtime: 992 ms, faster than 28.47% of C++ online submissions for Target Sum.
Memory Usage: 8.5 MB, less than 76.92% of C++ online submissions for Target Sum.

```c++
class Solution {
public:
    void findTargetSumWays_(vector<int>& nums, int sta, int end, int s, int& res, int S){
        if(sta > end) return;
        if(sta == end){
            if(nums[sta] + s == S) res += 1;
            if(s - nums[sta] == S) res += 1;
            return;
        }
        findTargetSumWays_(nums, sta+1, end, s-nums[sta], res, S);
        findTargetSumWays_(nums, sta+1, end, s+nums[sta], res, S);
        return;
    }
    int findTargetSumWays(vector<int>& nums, int S) {
        int res = 0;
        findTargetSumWays_(nums, 0, nums.size()-1, 0, res, S);
        return res;
    }
};
```

但这相当于二叉树，可以进行剪枝。比如当走到一个节点，如果其和大于S，而后续所有的节点都减法都大于S，那么就不必继续计算了，反之若当前和小于S，加上后面所有的都小于S，也就不用再往下走了。

优化后的代码如下：

Runtime: 364 ms, faster than 38.93% of C++ online submissions for Target Sum.
Memory Usage: 8.5 MB, less than 61.54% of C++ online submissions for Target Sum.

```C++
class Solution {
    vector<int> sum_;
public:
    void findTargetSumWays_(vector<int>& nums, int sta, int end, int s, int& res, int S){
        if(sta > end) return;
        if(sta == end){
            if(nums[sta] + s == S) res += 1;
            if(s - nums[sta] == S) res += 1;
            return;
        }
        if(s>S && s-sum_[sta]>S) return;
        if(s<S && s+sum_[sta]<S) return;
        findTargetSumWays_(nums, sta+1, end, s-nums[sta], res, S);
        findTargetSumWays_(nums, sta+1, end, s+nums[sta], res, S);
        return;
    }
    int findTargetSumWays(vector<int>& nums, int S) {
        int res = 0, len = nums.size();
        sum_ = vector<int>(len, 0);
        sum_[len-1] = nums[len-1];
        for(int i=len-2; i>=0; i--){
            sum_[i] = sum_[i+1] + nums[i]; 
        }
        findTargetSumWays_(nums, 0, nums.size()-1, 0, res, S);
        return res;
    }
};
```

BitBrave, 2019-08-09
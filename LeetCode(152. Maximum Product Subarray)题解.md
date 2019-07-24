# LeetCode(152. Maximum Product Subarray)题解
------
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
Example 2:

    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

## 题意理解
给一个整数数组，找出乘积最大的连续子数组的乘积。

最简单的办法就是遍历每一个连续子数组的组合，一共花费O(n^2)的时间复杂度。但这样会超时。

这道题有一个精彩的解释，<https://blog.csdn.net/whuwangyi/article/details/39577455>

我使用DP的办法。

```c++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int len = nums.size();
        int min_ = nums[0], max_ = nums[0], t = nums[0], res = nums[0];
        
        for(int i=1; i<len;  i++){
            t = min(min_*nums[i], min(nums[i], max_*nums[i]));
            max_ = max(min_*nums[i], max(nums[i], max_*nums[i]));
            min_ = t;
            res = max(res, max_);
        }
        return res;
    }
};
```

BitBrave, 2019-07-24
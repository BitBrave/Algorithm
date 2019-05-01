# LeetCode(53. Maximum Subarray)题解
------
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## 解题思路

Easy题，可以直接使用DC解决，使用两个值。从左到右遍历数组，一个值记录当前已遍历数组中最大的连续子数组，一个值记录当前已遍历数组中包括最右边元素在内的最大连续子数组。

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size()==0) return 0;
        if(nums.size()==1) return nums[0];

        int len = nums.size();
        int maxa = nums[0], maxb = nums[0];
        for(int i=1; i<len; i++){
            maxb = max(0, maxb);
            
            if(maxb+nums[i]>0) maxb += nums[i];
            else maxb = nums[i];
            
            maxa = max(maxa, maxb);
        }
        return maxa;
    }
};
```

BitBrave，2019-05-02
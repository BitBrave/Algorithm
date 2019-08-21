# LeetCode(713. Subarray Product Less Than K)题解
------
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

    Example 1:
    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

    0 < nums.length <= 50000.
    0 < nums[i] < 1000.
    0 <= k < 10^6.

## 解题思路
给出一个数组，找出其中所有的子数组个数，其元素乘积小于K。

这个可以用一个二指针法得到。res=0表示最优结果，首先，两个指针left和right都在最左边，然后right向右边走。当left和right中的元素乘积小于s时，res += right-left+1. 如果大于等于，left++. 直到小于，然后right继续++。如果left>right, right++。

## 时间复杂度O(n), 空间复杂度O(1).

代码如下：

Runtime: 136 ms, faster than 29.80% of C++ online submissions for Subarray Product Less Than K.
Memory Usage: 18.1 MB, less than 100.00% of C++ online submissions for Subarray Product Less Than K.

```c++
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int len = nums.size();
        if(len <= 0) return 0;
        int res = 0, left = 0, right = 0;
        int pro = nums[right];
        while(right < len && left < len){
            if(left>right){
                right++;
                pro *= nums[right];
            }
            else if(pro<k){
                res += right - left + 1;
                right++;
                if(right < len) pro *= nums[right];
            }
            else{
                pro /= nums[left];
                left++;
            }
        }
        return res;
    }
};
```

BitBrave, 2019-08-21
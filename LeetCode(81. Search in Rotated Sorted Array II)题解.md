# LeetCode(81. Search in Rotated Sorted Array II)题解
------
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true
Example 2:

    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false
Follow up:

    This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
    Would this affect the run-time complexity? How and why?

## 解题思路
给一个在某处旋转了的包含重复数的升序序列，从中查看是否存在特定的数。

使用二分法，每次比较中间的数。出现以下几种情况

中间的数小于右边的数，表示旋转的数组的旋转点在中间数左边

1 等于中间数，返回true

2 小于中间数，从左边数组中寻找。

3 大于中间数但小于右边数，在右边数组中寻找，若大于左边数则在左边数组寻找

中间的数大于右边的数，表示旋转的数组的旋转点在中间数右边

1 等于中间数，返回true

2 大于中间数，从右边数组中寻找。

3 小于中间数但大于右边数，在左边数组中寻找，若小于右边数则在右边数组寻找

中间的数等于右边的数，表示旋转的数组的旋转点在中间数右边或左边都有可能

1 等于中间数，返回true

2 直接二叉树，两边都寻找

代码如下：
Runtime: 4 ms, faster than 99.77% of C++ online submissions for Search in Rotated Sorted Array II.
Memory Usage: 8.9 MB, less than 6.02% of C++ online submissions for Search in Rotated Sorted Array II.

```C++
class Solution {
public:
    bool findindex(vector<int>& nums, int left, int right, int target){
        if(left>right) return false;
        if(left==right) return nums[left]==target;
        int med = (left+right)/2;
        
        if(nums[med]==nums[right]){
            if(target==nums[med]) return true;
            return findindex(nums, med+1, right-1, target) || findindex(nums, left, med-1, target);
        }
        if(nums[med]<nums[right]){
            if(target==nums[med]) return true;
            if(target==nums[right]) return true;
            if(target<nums[med]) return findindex(nums, left, med-1, target);
            if(target>nums[right]) return findindex(nums, left, med-1, target);
            return findindex(nums, med+1, right-1, target);
        }
        //nums[med]>nums[right]){
        if(nums[med]>nums[right]){        
            if(target==nums[med]) return true;
            if(target==nums[right]) return true;
            if(target>nums[med]) return findindex(nums, med+1, right-1, target);
            if(target<nums[right]) return findindex(nums, med+1, right-1, target);
            return findindex(nums, left, med-1, target);
        }
        return false;
    }
    bool search(vector<int>& nums, int target) {
        int len = nums.size();
        if(len==0) return false;
        
        return findindex(nums, 0, len-1, target);
    }
};
```

BitBrave, 2019-06-18
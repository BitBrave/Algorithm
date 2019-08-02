# LeetCode(162. Find Peak Element)题解
------
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

    Input: nums = [1,2,1,3,5,6,4]
    Output: 1 or 5 
    Explanation: Your function can return either index number 1 where the peak element is 2, 
                or index number 5 where the peak element is 6.
Note:

    Your solution should be in logarithmic complexity.


## 解题思路
给一个数组，找出其中的峰顶数据，就是大于两个邻居的数的index，如果有多个答案，任意一个都可以。

这个题可以直接使用最简单的暴力搜索，遍历整个数组，时间复杂度为O(n).虽然题目要求是log时间，但是这样也可以AC。

代码如下

Runtime: 8 ms, faster than 56.66% of C++ online submissions for Find Peak Element.
Memory Usage: 8.6 MB, less than 87.08% of C++ online submissions for Find Peak Element.

```c++
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int len = nums.size();
        if(len == 1 || nums[0]>nums[1]) return 0;
        if(nums[len-2]<nums[len-1]) return len-1;
        for(int i=1; i<len-1; i++){
            if(nums[i]>nums[i-1] && nums[i]>nums[i+1]) return i;
        }
        return -1;
    }
};
```

但是也可以实现O(logn)的时间复杂度。可以用binary search。每次寻找中间的数，如果恰好是峰顶数据，就返回index。如果不是，就查看其与中间元素相邻的左边和右边的值，选取大于中间元素的那边的一半数组继续遍历，如果两边都大于，就随便选一个。注意，这里是没有考虑相同的数据挨着的情况的。

代码如下

Runtime: 4 ms, faster than 96.70% of C++ online submissions for Find Peak Element.
Memory Usage: 8.7 MB, less than 60.89% of C++ online submissions for Find Peak Element.

```c++
class Solution {
public:
    int findPeakElement_(vector<int>& nums, int left, int right){
        if(left>right) return -1;
        if(left == right) return left;
        if(left+1 == right) return nums[left]>nums[right] ? left:right;
        
        int mid = (left+right) / 2;
        if(nums[mid]>nums[mid-1] && nums[mid]>nums[mid+1]) return mid;
        if(nums[mid]<nums[mid-1]) return findPeakElement_(nums, left, mid-1);
        return findPeakElement_(nums, mid+1, right);
    }
    int findPeakElement(vector<int>& nums) {
        return findPeakElement_(nums, 0, nums.size()-1);
    }
};
```

BitBrave, 2019-08-02
# LeetCode(33. Search in Rotated Sorted Array)题解
------

## 解题思路
给定一个升序的一串数字，其中有可能在某个位置被旋转了，比如 1、2、3、4、5在3旋转就变成了3、4、5、1、2，此时的旋转点位置的值5，因为这个值之后的数都变小了。现在假定这串数字是不重合的，给定一个数target，要求在O(logn)的时间内找出这个数在一串数字中的索引，如果有的话就返回位置，没有返回-1。

一旦涉及到logn通常考虑二分查找。因此这个题可以这样想，首先将数组对半分，查看中间的数与两边的数的大小，可以知道的是，当数组被旋转之后，第一个元素是一定大于最后一个元素的。

假如中间元素小于右边元素，可以判断旋转点在中间元素的左边。此时有以下几种情况：

1 target=中间元素，直接返回索引值，算法结束
2 target=右边元素，直接返回索引值，算法结束
3 target大于右边元素，表明其值只可能在左边的半个数组内，在左边数组内寻找
4 target小于中间元素，表明其值只可能在左边的半个数组内，在左边数组内寻找
5 target在中间元素和右边元素之间，表明其值只可能在右边的半个数组内，在右边数组内寻找

假如中间元素大于右边元素，可以判断旋转点在中间元素的右边。此时有以下几种情况：

1 target=中间元素，直接返回索引值，算法结束
2 target=左边元素，直接返回索引值，算法结束
3 target小于左边元素，表明其值只可能在右边的半个数组内，在右边数组内寻找
4 target大于中间元素，表明其值只可能在右边的半个数组内，在右边数组内寻找
5 target在中间元素和左边元素之间，表明其值只可能在左边的半个数组内，在左边数组内寻找

注意，如果没有target如何判断，可以这样：当中间元素等于右边元素时，表明此时数组内就一个元素，而此时target还是不等于的话，就返回-1。
这样，每次都将数组减半，时间复杂度为O(logn)

代码如下：
Runtime: 4 ms, faster than 99.87% of C++ online submissions for Search in Rotated Sorted Array.
Memory Usage: 9.1 MB, less than 98.58% of C++ online submissions for Search in Rotated Sorted Array.

```c++
class Solution {
public:
    int findindex(vector<int>& nums, int left, int right, int target){
        if(left>right) return -1;
        
        int med = (left+right)/2;
        
        if(nums[med]==nums[right]) return nums[med]==target ? med:-1;
        else if(nums[med]<nums[right]){
            if(target==nums[med]) return med;
            if(target==nums[right]) return right;
            if(target<nums[med]) return findindex(nums, left, med-1, target);
            if(target>nums[right]) return findindex(nums, left, med-1, target);
            return findindex(nums, med+1, right, target);
        }
        //nums[med]>nums[right]){
        if(target==nums[med]) return med;
        if(target==nums[left]) return left;
        if(target>nums[med]) return findindex(nums, med+1, right, target);
        if(target<nums[left]) return findindex(nums, med+1, right, target);
        return findindex(nums, left, med-1, target);
    }
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        if(len==0) return -1;
        
        return findindex(nums, 0, len-1, target);
    }
};
```
或者

```c++
class Solution {
public:
    int findindex(vector<int>& nums, int left, int right, int target){
        if(left>right) return -1;
        if(left==right) return nums[left]==target ? left:-1;
        int med = (left+right)/2;
        
        //if(nums[med]==nums[right]) return nums[med]==target ? med:-1;
        if(nums[med]<nums[right]){
            if(target==nums[med]) return med;
            if(target==nums[right]) return right;
            if(target<nums[med]) return findindex(nums, left, med-1, target);
            if(target>nums[right]) return findindex(nums, left, med-1, target);
            return findindex(nums, med+1, right, target);
        }
        //nums[med]>nums[right]){
        if(target==nums[med]) return med;
        if(target==nums[left]) return left;
        if(target>nums[med]) return findindex(nums, med+1, right, target);
        if(target<nums[left]) return findindex(nums, med+1, right, target);
        return findindex(nums, left, med-1, target);
    }
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        if(len==0) return -1;
        
        return findindex(nums, 0, len-1, target);
    }
};
```

BitBrave, 2019-05-10
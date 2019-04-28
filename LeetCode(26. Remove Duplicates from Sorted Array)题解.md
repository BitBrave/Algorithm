# LeetCode(26. Remove Duplicates from Sorted Array)题解
------
原文如下
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.
Example 2:

    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

    It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

    // nums is passed in by reference. (i.e., without making a copy)
    int len = removeDuplicates(nums);

    // any modification to nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }

## 解题思路
这是一个easy题，直接使用vector的erase函数即可，在遍历的时候发现与前面一样的数直接删除，注意的是函数不仅要返回正确的length，还要返回正确的vector。

这是一种方式，但是不断的删除是一个比较耗时的操作（156ms），代码如下：

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        
        for(int i=1; i<len; i++){
            if(nums[i]!=nums[i-1]) continue;
            nums.erase(nums.begin()+i);
            i--;
            len--;
        }
        return len;
    }
};
```

## 解法二
根据题意我们只要将vector前面正确length内的容器内放入正确的数就可以了，因此可以用一个位置来记录，当发现一样的数的时候，将后面的数直接覆盖前面的就可以了。

代码如下(24ms)：

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() <= 1) return nums.size();
        int len = nums.size();
        int i=0, count = len;
        for(int j=1; j<len; j++){
            if(nums[j-1]!=nums[j]) nums[++i] = nums[j];
        }
        return i+1;
    }
};
```
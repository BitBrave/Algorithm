# LeetCode(80. Remove Duplicates from Sorted Array II)题解
------
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,1,2,2,3],

    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

    Given nums = [0,0,1,1,1,1,2,3,3],

    Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

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

# 解题思路
要求给定一个数组，已经排序好的。将其中重复的去掉，每个数字最多重复两次。不能使用额外的内存，只能在O(1)的空间复杂度内完成。

可以使用一个变量c记录当前数字重复的次数。从左到右遍历数组。当前遇到的若和前面的数字不一样，表示没有重复，c=1.如果和前面一样则c++。如果此时c>2表示重复超过了两次，则将此数删掉。

代码如如下：


```C++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int c = 1, len = nums.size();
        for(int i=1; i<len; i++){
            if(nums[i]!=nums[i-1]){
                c = 1;
                continue;
            }
            c++;
            if(c>2){
                nums.erase(nums.begin()+i);
                i--;
                c--;
                len--;
            }
        }
        return nums.size();
    }
};
```

BitBrave, 2019-06-017
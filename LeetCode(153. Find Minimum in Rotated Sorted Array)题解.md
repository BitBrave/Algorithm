# LeetCode(153. Find Minimum in Rotated Sorted Array)题解
------
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

    Input: [3,4,5,1,2] 
    Output: 1
Example 2:

    Input: [4,5,6,7,0,1,2]
    Output: 0

## 解题思路
给一个升序的但是在某个点旋转了的数组，找出其中最小的。数组没有相同的元素存在。

最简单的方式就是O(n)，从左到右遍历数组。找到最小的即可。

但是有一个O(logn)的算法，每次中间找，然后查看中间元素和右边相比，如果大于最右边元素说明拐点（就是旋转的点）在右边数组内，那么最小值也在右边，小于最右边元素就说明拐点在左边数组，最小值也在左边。这样直接二分即可。如果等于右边，此时若数组大小为1，就直接返回，否则返回左右中最小的值。

代码如下：

Runtime: 8 ms, faster than 10.03% of C++ online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 10.4 MB, less than 5.04% of C++ online submissions for Find Minimum in Rotated Sorted Array.

```c++
class Solution {
public:
    int findMin_(vector<int> nums, int sta, int end){
        if(sta == end) return nums[sta];
        int mid = (sta+end) / 2;
        if(nums[mid] > nums[end]) return findMin_(nums, mid+1, end);
        return findMin_(nums, sta, mid);
    }
    int findMin(vector<int>& nums) {
        return findMin_(nums, 0, nums.size()-1);
    }
};
```

当然也可以不用递归，使用循环。代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 8.6 MB, less than 100.00% of C++ online submissions for Find Minimum in Rotated Sorted Array.

```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int sta = 0, end = nums.size() - 1;
        int mid;
        
        while(end>sta){
            mid = (sta+end) / 2;
            if(nums[mid] > nums[end]) sta = mid + 1;
            else end = mid;
        }
        return nums[sta];
    }
};
```

BitBrave, 2019-08-07
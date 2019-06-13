# LeetCode(78. Subsets)题解
------
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

    Input: nums = [1,2,3]
    Output:
    [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
    ]

## 解题思路
Medium，给出一个集合，返回这个集合的所有子集，包括空集。

可以直接使用递归分叉的办法，每一个数有选择进入或不进入一个特定子集的方式。直接二分叉即可。一个N个数的集合有2的N次方个子集。

代码如下：

Runtime: 16 ms, faster than 5.29% of C++ online submissions for Subsets.
Memory Usage: 18.6 MB, less than 5.03% of C++ online submissions for Subsets.

```c++
class Solution {
public:
    void subsets_(vector<int> nums, int sta, int end, vector<vector<int>> &res, vector<int> tmp) {
        if(sta>end){
            res.push_back(tmp);
            return;
        }
        subsets_(nums, sta+1, end, res, tmp);
        tmp.push_back(nums[sta]);
        subsets_(nums, sta+1, end, res, tmp);
        return;
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> tmp;
        
        subsets_(nums, 0, nums.size()-1, res, tmp);
        return res;
    }
};
```

BitBrave，2019-06-13
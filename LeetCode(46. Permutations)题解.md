# LeetCode(46. Permutations)题解
------
Given a collection of distinct integers, return all possible permutations.

Example:

    Input: [1,2,3]
    Output:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]

## 解题思路
Medium，要求给一个数组（每个数不一样），然后求出这个数的所有排列，按照数学的计算，一个N个数的数组，排列有N！种。

我的思路是直接使用递归，permute_函数，就每次将一个数放在最前面，然后剩下的数做全排列，一共有n-1！种，依次类推，当没有数就直接返回。

代码如下

Runtime: 16 ms, faster than 46.36% of C++ online submissions for Permutations.
Memory Usage: 10.8 MB, less than 8.29% of C++ online submissions for Permutations.

```c++
class Solution {
public:
    void permute_(vector<vector<int>> &ret, vector<int> tmp, vector<int> nums, int left, int right){
        if(left>right){
            ret.push_back(tmp);
            return;
        }
        for(int i=left; i<=right; i++){
            vector<int> tmp_(tmp);
            tmp_.push_back(nums[i]);
            swap(nums[left],nums[i]);
            permute_(ret, tmp_, nums, left+1, right);
        }
        return;
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ret;
        vector<int> tmp;
        
        permute_(ret, tmp, nums, 0, nums.size()-1);
        return ret;
    }
};
```

BitBrave, 2019-05-16
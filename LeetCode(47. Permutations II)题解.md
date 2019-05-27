# LeetCode(47. Permutations II)题解
------
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
    [
    [1,1,2],
    [1,2,1],
    [2,1,1]
    ]

## 解题思路
Medium，看到这个题，第一个思路就是递归。首先将数组排序，然后每次递归将第一个数放在第一个位置，后面的数排列完形成一种情况。然后跳过相同的数，查看第二个不同的数放在头部形成的不一样的排列组合。

代码如下：

Runtime: 28 ms, faster than 53.18% of C++ online submissions for Permutations II.
Memory Usage: 17.9 MB, less than 5.52% of C++ online submissions for Permutations II.

```c++
class Solution {
public:
    void permuteUnique_(vector<vector<int>>& res, vector<int> nums, int sta, int len, vector<int> tmp){
        if(sta>=len){
            res.push_back(tmp);
            return;
        }
      
        tmp.push_back(nums[sta]);
        
        permuteUnique_(res, nums, sta+1, len, tmp);
        
        for(int i=sta+1; i<len; i++){
            if(nums[sta]==nums[i]) continue;
            swap(nums[sta], nums[i]);
            tmp[tmp.size()-1] = nums[sta];
            permuteUnique_(res, nums, sta+1, len, tmp);
        }
        return;
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> tmp;
        int len = nums.size();
        if(len==0) return res;
        
        sort(nums.begin(), nums.end());
        
        permuteUnique_(res, nums, 0, len, tmp);
        return res;
    }
};
```

BitBrave, 2019-05-27
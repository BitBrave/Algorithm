# LeetCode(90. Subsets II)题解
------
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
    [
        [2],
        [1],
        [1,2,2],
        [2,2],
        [1,2],
        []
    ]

## 解题思路
给一个有重复数的数组集合，求出其所有的子集，子集不能有重复。

可以将数组先排序。然后使用递归的办法，对于每个数，有加入或者不加入之分。而如果有重复的话，就有加入一次，加入两次，加入多次之分。递归时判断一下即可。

代码如下：

Runtime: 8 ms, faster than 92.10% of C++ online submissions for Subsets II.
Memory Usage: 18.2 MB, less than 5.00% of C++ online submissions for Subsets II.

```c++
class Solution {
public:
    void subsetsWithDup_(vector<int>& nums, int sta, int len, vector<int> tmp, vector<vector<int>>& res){
        if(sta == len){
            res.push_back(tmp);
            return;
        }
        int n = sta + 1;
        while(n<len && nums[sta] == nums[n]) n++;
        
        subsetsWithDup_(nums, n, len, tmp, res);
        
        for(int i=sta; i<n; i++){
            tmp.push_back(nums[sta]);
            subsetsWithDup_(nums, n, len, tmp, res);
        }
        return;
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> tmp;
        int len = nums.size();
        if(len == 0) return res;
        subsetsWithDup_(nums, 0, len, tmp, res);
        return res;
    }
};
```

BitBrave, 2019-06-21

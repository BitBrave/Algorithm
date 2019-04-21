# LeetCode(18. 4Sum)题解
------
原文如下
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

    A solution set is:
    [
    [-1,  0, 0, 1],
    [-2, -1, 1, 2],
    [-2,  0, 0, 2]
    ]

## 题目思路
与15题类似，15题是3sum，要求三个数相加得到某一个特定的数，而本题则为4sum。直接在3sum的基础之上套一层循环即可。唯一要注意的就是，可能有的同学会疑问：遇到重复的数字要不要跳过，比如选定第一个数之后再剩下的数组中找寻其余几个数，找寻完毕之后，那么要是第二次选定数的时候选定的数与第一个数相同是否应该跳过。有没有可能以为追求独一性而漏掉了某些选择。答案是应该跳过，并且不会漏掉。因为我们将数组排序之后，从左到右依次选定第一个数第二个数，当前面的数和后面的数相同时，在选定前面的数为基准操作时，就已经把后面的数的所有情况都给遍历下来了。比如[1,1,a,b,c,...]，当选定第一个1作为4sum中的一个数寻找剩下的三个数时，已经把将第二个1作为4sum中的一个数的所有情况都给遍历了。

代码如下：
```c++
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        int len = nums.size();
        
        // sort O(nlogn)
        sort(nums.begin(), nums.end());
        for(int i=0; i<len-3; i++){// first number
            for(int j=i+1; j<len-2; j++){
                int l = j+1, r = len-1;
                int diff = target - nums[i] - nums[j];
                while(l < r){
                    if(nums[l] + nums[l+1] > diff || nums[r] + nums[r-1] < diff) break;
                    
                    if(diff > nums[l]+nums[r]) l++;
                    else if(diff < nums[l]+nums[r]) r--;
                    else{ // equal
                        vector<int> a{nums[i], nums[j], nums[l], nums[r]};
                        res.push_back(a);
                        l++;
                        r--;
                        while(l < r && nums[l] == nums[l-1]) l++;
                        while(r > l && nums[r] == nums[r+1]) r--;
                    }
                }
                while(j + 1 < len - 2 && nums[j] == nums[j + 1]) j++; 
            }
            while(i + 1 < len - 3 && nums[i] == nums[i + 1]) i++; 
        };
        return res;   
    }
};
```
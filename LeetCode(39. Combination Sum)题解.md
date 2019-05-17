# LeetCode(39. Combination Sum)题解
------
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
    [7],
    [2,2,3]
    ]
Example 2:

    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
    [2,2,2,2],
    [2,3,3],
    [3,5]
    ]

## 解题思路
Medium，要求给定一个不重复的数组，求出一些元素的组合其和位target，这些元素可以重复多次。

这道题看到首先想到的是先排序，然后队首队尾两个指针向中间走，但是这个题并不用这么复杂。

我们可以使用递归的办法，将数组升序排序之后，进入一个递归数组，首先加入第一个数，当其和小于target的，剩下的在第二个数到之后的数中选，这涵盖了一些情况。然后将第一个数在此加入，等于把第一个数选取两次，然后剩下的在第二个数到之后的数中选。然后将第一个数加入三次·····当然要保证数之和要小于等于target。最后递归内的核心结构就是如果大于就返回，等于就记录，小于就往下走。

代码如下：

Runtime: 276 ms, faster than 5.00% of C++ online submissions for Combination Sum.
Memory Usage: 113.9 MB, less than 5.01% of C++ online submissions for Combination Sum.

```c++
class Solution {
public:
    void findSum(vector<vector<int>>& ret, vector<int> tmp, int tsum,  int target, vector<int> candidates, int sta, int len){
        if(tsum==target){
            ret.push_back(tmp);
            return;
        }
        if(sta>=len || tsum>target) return;
        
        vector<int> tmp_(tmp);
        findSum(ret, tmp_, tsum, target, candidates, sta+1, len);
        for(int i=1; i*candidates[sta]+tsum <= target; i++){
            tmp_.push_back(candidates[sta]);
            findSum(ret, tmp_, i*candidates[sta]+tsum, target, candidates, sta+1, len);
        }
        return;
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        int len = candidates.size();
        vector<vector<int>> ret;
        vector<int> tmp;
        
        sort(candidates.begin(), candidates.end());
        
        findSum(ret, tmp, 0, target, candidates, 0, len);
        return ret;
    }
};
```
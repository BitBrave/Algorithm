# LeetCode(40. Combination Sum II)题解
------
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
    ]
Example 2:

    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [
    [1,2,2],
    [5]
    ]


## 解题思路
Medium，要求给定一个可能重复的数组，求出一些元素的组合其和位target，这些元素最多出现一次。

我们可以使用递归的办法，将数组升序排序之后，进入一个递归数组，首先加入第一个数，当其和小于target的，剩下的在第二个数到之后的数中选，这涵盖了一些情况。然后不入这个数，直接在剩下的数内选所有的，·····当然要保证数之和要小于等于target。最后递归内的核心结构就是如果大于就返回，等于就记录，小于就往下走。

因为有重复的数出现，所以要注意去重。可以使用这样的方法：当遍历到一个数时，这个数可以选择加与不加，如果不加的话，直接就跳到下一个与这个不一样的数的位置。然后找出这个数重复的次数K，然后把这个数加入1次到K次，然后再加入到下一个与这个不一样的数的位置。最后得到结果。

代码如下：

Runtime: 428 ms, faster than 5.03% of C++ online submissions for Combination Sum II.
Memory Usage: 176.9 MB, less than 5.01% of C++ online submissions for Combination Sum II.

```c++
class Solution {
public:
    void findSum(vector<vector<int>>& ret, vector<int> tmp, int tsum,  int target, vector<int> candidates, int sta, int len){
        if(tsum==target){
            ret.push_back(tmp);
            return;
        }
        if(sta>=len || tsum>target) return;
        
        int p = sta + 1;
        while(p<len && candidates[sta]==candidates[p]) p++;
        findSum(ret, tmp, tsum, target, candidates, p, len);
        
        for(int i=sta; i<p; i++){
            tmp.push_back(candidates[sta]);
            findSum(ret, tmp, (1+i-sta)*candidates[sta]+tsum, target, candidates, p, len);
        }
        
        return;
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        int len = candidates.size();
        vector<vector<int>> ret;
        vector<int> tmp;
        
        sort(candidates.begin(), candidates.end());
        
        findSum(ret, tmp, 0, target, candidates, 0, len);
        return ret;
    }
};
```
# LeetCode(228. Summary Ranges)题解

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

    Input:  [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


## 解题思路
给一个升序的数组，将其中连续的数组用区间表示出来，用字符串表示。

很简单的题，直接遍历，如果满足+1就一直往后走，不满足了就表示找到了一个区间，直接转换过来就行了。

代码如下：

Runtime: 4 ms, faster than 53.61% of C++ online submissions for Summary Ranges.
Memory Usage: 8.5 MB, less than 84.62% of C++ online submissions for Summary Ranges.

```c++
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int len = nums.size();
        vector<string> res;
        if(len == 0) return res;
        int lasti = 0, i;

        for(i=1; i<len; i++){
            if(nums[i] - 1 == nums[i-1]) continue;
            stringstream ss1, ss2;
            ss1<<nums[lasti];
            ss2<<nums[i-1];
            if(lasti < i-1) res.push_back(ss1.str()+"->"+ss2.str());
            else res.push_back(ss1.str());
            lasti = i;
        }
        stringstream ss1, ss2;
        ss1<<nums[lasti];
        ss2<<nums[i-1];
        if(lasti < i-1) res.push_back(ss1.str()+"->"+ss2.str());
        else res.push_back(ss1.str());
        
        return res;
    }
};
```

BitBrave， 2019-08-14
# LeetCode(56. Merge Intervals)题解
------
Given a collection of intervals, merge all overlapping intervals.

Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

## 解题思路

Medium，将一个不同的区间求并集。

我的方法很简单，首先将数组按照区间的左边值升序排序，再逐个遍历，根据策略进行合并或单独加入结果。

代码如下（很慢，懒得优化了）：

Runtime: 64 ms, faster than 16.99% of C++ online submissions for Merge Intervals.
Memory Usage: 26.6 MB, less than 5.00% of C++ online submissions for Merge Intervals.

```c++
class Solution {
public:
    static bool cmp(const vector<int> a, const vector<int> b){
        return a[0]<b[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        int len = intervals.size(), rlen = 0;
        if(len == 0) return res;
        
        sort(intervals.begin(), intervals.end(), cmp);

        res.push_back(intervals[0]);
        rlen = 1;
        
        for(int i=1; i<len; i++){
            if(res[rlen-1][1]>=intervals[i][0]) res[rlen-1][1] = intervals[i][1]>res[rlen - 1][1] ? intervals[i][1]:res[rlen - 1][1];
            else {
                res.push_back(intervals[i]);
                rlen++;
            }
        };
        return res;
    }
};
```

BitBrave, 2019-05-30
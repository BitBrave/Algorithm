# LeetCode(57. Insert Interval)题解
------
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

## 解题思路
Hard，就是一个已经排序好的集合，加入一个新的单个的区间，重新求集合而已。感觉不应该设为Hard。

方法非常简单，从左到右遍历，看看当前区间与新加入的是否有交集，有就更新，无就插入这个区间。注意新加入的区间可能嵌入排序好的区间集合之中。

代码如下：

Runtime: 12 ms, faster than 98.84% of C++ online submissions for Insert Interval.
Memory Usage: 12.5 MB, less than 9.57% of C++ online submissions for Insert Interval.

```c++
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int len = intervals.size(), count = 0;
        if(len==0){
            res.push_back(newInterval);
            return res;
        }
        
        res.push_back(intervals[0]);
        count++;
        if(res[0][1]>=newInterval[0] && res[0][0]<=newInterval[1]){
            res[count-1][0] = res[count-1][0]<newInterval[0] ? res[count-1][0] : newInterval[0];
            res[count-1][1] = res[count-1][1]>newInterval[1] ? res[count-1][1] : newInterval[1];
        }
        
        for(int i=1; i<len; i++){
            if(newInterval[0]>intervals[i-1][1] && newInterval[1]<intervals[i][0]) res.push_back(newInterval);
            if(res[count-1][1]>=intervals[i][0])
                res[count-1][1] = res[count-1][1]>intervals[i][1] ? res[count-1][1] : intervals[i][1];
            else {
                res.push_back(intervals[i]);
                count++;
            }
            if(res[count-1][1]>=newInterval[0] && res[count-1][0]<=newInterval[1]){
                res[count-1][0] = res[count-1][0]<newInterval[0] ? res[count-1][0] : newInterval[0];
                res[count-1][1] = res[count-1][1]>newInterval[1] ? res[count-1][1] : newInterval[1];
            }
        }
        if(res[count-1][1]<newInterval[0]) res.push_back(newInterval);
        else if(res[0][0]>newInterval[1]) res.insert(res.begin(), newInterval);
        return res;
    }
};
```

BitBrave, 2019-05-31
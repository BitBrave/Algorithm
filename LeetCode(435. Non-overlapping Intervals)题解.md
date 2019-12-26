# LeetCode(\435. Non-overlapping Intervals)题解

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



**Example 1:**

```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```

**Example 2:**

```
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```

**Example 3:**

```
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

 

**Note:**

1. You may assume the interval's end point is always bigger than its start point.
2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

##  解题思路

给出若干个区间，从中删除最少的区间数，使得剩下的区间都不相交。

这个题明显就是Greedy，将所有区间按起始点开始升序排序，然后从左到右遍历。维持一个变量end，表示遍历到当前位置时，区间所占的最大位置。遍历到位置i时，比较i区间的左边与end的大小，如果end小于等于，说明这个区间和已遍历的区间（已经删除一些的）并不相交，所以直接放进去（暂时），更新end = i的右端位置。如果end大于，说明这个区间相交了，就应该删除，那么删除哪一个呢，这时候我们的greedy法则就出来了。那就是，我们尽量不往右占更多空间，就是比较end 和i的右边位置，谁大删除谁，因此res++，end = min(end，i的右边位置)。

代码如下，时间复杂度，排序加遍历为O(nlogn)，空间复杂度O(1)。

`Runtime: 76 ms, faster than 14.44% of C++ online submissions for Non-overlapping Intervals.`

`Memory Usage: 27.4 MB, less than 11.11% of C++ online submissions for Non-overlapping Intervals.`

```c++
bool cmp(vector<int> a, vector<int> b) {
    return a[0] < b[0];
}
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int len = intervals.size(), res = 0;
        if (len == 0) return 0;
        sort(intervals.begin(), intervals.end(), cmp);
        int end = intervals[0][1];
        for (int i=1; i<len; i++) {
            if (intervals[i][0] >= end) {
                end = intervals[i][1];
            } else {
                res++;
                end = min(end, intervals[i][1]);
            }
        }
        return res;
    }
};
```

BitBrave, 2019-12-26
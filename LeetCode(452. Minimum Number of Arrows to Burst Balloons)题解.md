# LeetCode(\452. Minimum Number of Arrows to Burst Balloons)题解

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

**Example:**

```
Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
```

## 解题思路

一串气球在各自的区间，区间之间可能有重叠。从一个位置射出一箭，包含这个位置的区间所对应的就会破裂。要求用最少的箭把所有的气球射爆。

这个题简化了就是，我们选最少的点，可以使得其对应所有的区间。这是一个Greedy题。策略是什么呢，就是我们每次选点的时候，都尽可能包含更多的区间进去。

将所有区间按照左位置升序排列。然后维护一个sta和end值。初始化sta和end为第一个区间的左位置和右位置。然后依次遍历后面的区间。如果后面区间的左位置小于等于end值，说明这个区间和前面是重叠的，就可以和前面的用一个点来包含，更新sta为这个区间的左值，end为min(end,区间右值)。如果大于end值，说明不重叠，就必须额外选点，因此ret++，然后sta和end更新为这个区间的左位置和右位置。

代码如下，时间复杂度因为排序为O(nlogn)，空间复杂度O(1)。

`Runtime: 680 ms, faster than 7.76% of C++ online submissions for Minimum Number of Arrows to Burst Balloons.`

`Memory Usage: 159.6 MB, less than 20.00% of C++ online submissions for Minimum Number of Arrows to Burst Balloons.`

```c++
bool cmp(vector<int> a, vector<int> b) {
    return a[0] <= b[0];
}
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int len = points.size();
        int sta = 0, end = 0, ret = 0;
        if (len == 0) return ret;
        sort(points.begin(), points.end(), cmp);
        
        sta = points[0][0];
        end = points[0][1];
        for (int i=1; i<len; i++) {
            if (points[i][0] <= end) {
                sta = points[i][0];
                end = min(end, points[i][1]);
            } else {
                ret++;
                sta = points[i][0];
                end = points[i][1];
            }
        }
        ret++;
        return ret;
    }
};
```

BitBrave，2019-12-30
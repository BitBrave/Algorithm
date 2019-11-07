# LeetCode(939. Minimum Area Rectangle)题解

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

**Example 1:**

```
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
```

**Example 2:**

```
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
```

 

**Note**:

1. `1 <= points.length <= 500`
2. `0 <= points[i][0] <= 40000`
3. `0 <= points[i][1] <= 40000`
4. All points are distinct.

## 解题思路

给一些二维平面上的点，计算其组成的最小矩形点，矩形的四边必须平行于X和Y轴，如果不存在就返回0.

这个题可以直接使用暴力枚举，但是也要注意方法。 每次选定要两个点，将其作为对角点，有了对角点之后查看另外两个点是否在数组中，如果在就记录其面积，如果不在的话就放弃这两个点，再次选择一对。这个过程中要一直记录最小的面积。

代码如下，时间复杂度O(N2)，空间复杂度O(n).

`Runtime: 576 ms, faster than 30.14% of C++ online submissions for Minimum Area Rectangle.`

`Memory Usage: 18 MB, less than 75.00% of C++ online submissions for Minimum Area Rectangle.`

```c++
class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        int ret = INT_MAX, len = points.size();
        set<pair<int, int>> S;
        
        for(vector<int> p : points){
            S.insert(make_pair(p[0], p[1]));
        }
        for(int i=0; i<len; i++){
            for(int j=i+1; j<len; j++){
                if(points[i][0] == points[j][0] or points[i][1] == points[j][1]) continue;
                if(S.find(make_pair(points[i][0], points[j][1])) == S.end() or S.find(make_pair(points[j][0], points[i][1])) == S.end()) continue;
                ret = min(ret, abs((points[i][0]-points[j][0]) * (points[i][1]-points[j][1])));
            }
        }
        return INT_MAX == ret ? 0 : ret;
    }
};
```

BitBrave, 2019-11-07
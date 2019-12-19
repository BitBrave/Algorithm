# LeetCode(\1094. Car Pooling)题解

You are driving a vehicle that has `capacity` empty seats initially available for passengers. The vehicle **only** drives east (ie. it **cannot** turn around and drive west.)

Given a list of `trips`, `trip[i] = [num_passengers, start_location, end_location]` contains information about the `i`-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off. The locations are given as the number of kilometers due east from your vehicle's initial location.

Return `true` if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

**Example 1:**

```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

**Example 2:**

```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

**Example 3:**

```
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
```

**Example 4:**

```
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
```

 

 

**Constraints:**

1. `trips.length <= 1000`
2. `trips[i].length == 3`
3. `1 <= trips[i][0] <= 100`
4. `0 <= trips[i][1] < trips[i][2] <= 1000`
5. `1 <= capacity <= 100000`

## 解题思路

有一个车站序列，一辆固定容量的汽车每站停下来下乘客和上乘客。问给定一个乘客的上下站位置和数目的数组，判断这个汽车是否可以成功载人到终点。

这个题有点类似于教室安排的情况，用最少的教室来排出所有的课，这个题转化过来就是满足开课的最小教室数和给定的教室数之间的比较。

因此我们可以使用Greedy办法做，设定一个与车站数等长的数组，数组i位置记录车站i-1到i之间的乘客数目。因此我们需要做的就是用乘客组来填充这个数组。最后遍历数组，如果有数大于车的载重返回False，否则返回True。

代码如下，时间复杂度O(乘客组数\*车站数)，空间复杂度O(车站数)。

`Runtime: 20 ms, faster than 16.98% of C++ online submissions for Car Pooling.`

`Memory Usage: 10.4 MB, less than 100.00% of C++ online submissions for Car Pooling.`

```c++
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<int> ret(1001, 0);
        for (vector<int> trip : trips) {
            for (int i=trip[1]; i<trip[2]; i++) {
                ret[i] += trip[0];
                if (ret[i] > capacity) return false;
            }
        }
        // for (int r : ret) {
        //     if (r > capacity) return false;
        // }
        return true;
    }
};
```

BitBrave，2019-12-19
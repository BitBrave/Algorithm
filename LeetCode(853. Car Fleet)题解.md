# LeetCode(853. Car Fleet)题解

`N` cars are going to the same destination along a one lane road.  The destination is `target` miles away.

Each car `i` has a constant speed `speed[i]` (in miles per hour), and initial position `position[i]` miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A *car fleet* is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

**Example 1:**

```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
```


**Note:**

1. `0 <= N <= 10 ^ 4`
2. `0 < target <= 10 ^ 6`
3. `0 < speed[i] <= 10 ^ 6`
4. `0 <= position[i] < target`
5. All initial positions are different.

## 解题思路

N辆车沿着一条车道行驶到同一目的地。目的地是目标英里。每辆汽车均具有恒定的speed[i]（以英里/小时为单位），初始位置position[i]沿道路朝向目标。一辆汽车永远无法超越前面的另一辆汽车，但它可以追上它，并以相同的速度驾驶。忽略这两辆车之间的距离-假定它们具有相同的位置。车队是在相同位置和相同速度下行驶的一些非空车组。请注意，单车也是车队。如果汽车正好赶上目的地的车队，它将仍被视为一个车队。多少车队将到达目的地？

我们可以这样理解，以时间为横轴，路程为纵轴画一个平面直角坐标系，那么每辆车的行驶就对应这个坐标中的一条直线。与y轴的交点就是车的出发位置，斜率就是车的速度。那么在到达target（y轴target位置与X轴平行的直线）之前，所有后来居上超过先前直线的直线都表示超车，根据题意就可以删除这条直线。因此，每遇到相交的两条直线，就删除与y轴相交更低的那条线。最后坐标系中的所有直线在target之下都不相交，直线的数量就是问题的解。

因此，这道题可以使用排序的方法来做，将车辆按照出发距离排序，然后从头到尾遍历，对于每一辆车，看后续的车是否在target之前有超过的，有就将其删除。

代码如下，时间复杂度O(n)，空间复杂度O(n)。

`Runtime: 48 ms, faster than 73.22% of C++ online submissions for Car Fleet.`

`Memory Usage: 10.5 MB, less than 100.00% of C++ online submissions for Car Fleet.`

```C++
vector<int> P;
bool cmp(int a, int b){
    return P[a] > P[b];
}
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int len = position.size();
        P = position;
        vector<int> car(len);
        for(int i=0; i<len; i++) car[i] = i;
        sort(car.begin(), car.end(), cmp);
        for(int i=0; i<len; i++){
            if(car[i] == -1) continue;
            double X = (target - position[car[i]])*1.0 / speed[car[i]];
            for(int j=i+1; j<len; j++){
                if(car[j] == -1) continue;
                if(X*speed[car[j]] + position[car[j]] >= target) car[j] = -1;
            }
        }
        int res = 0;
        for(int c : car){
            if(c != -1) res++;
        }
        return res;
    }
};
```

BitBrave，2019-10-14
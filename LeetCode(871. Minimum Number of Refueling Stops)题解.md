# LeetCode(\871. Minimum Number of Refueling Stops)题解

A car travels from a starting position to a destination which is `target` miles east of the starting position.

Along the way, there are gas stations. Each `station[i]` represents a gas station that is `station[i][0]` miles east of the starting position, and has `station[i][1]` liters of gas.

The car starts with an infinite tank of gas, which initially has `startFuel` liters of fuel in it. It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination? If it cannot reach the destination, return `-1`.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

**Example 1:**

```
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
```

**Example 2:**

```
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
```

**Example 3:**

```
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: 
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
```

**Note:**

1. `1 <= target, startFuel, stations[i][1] <= 10^9`
2. `0 <= stations.length <= 500`
3. `0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target`

## 解题思路

有一个有油箱无限大的车，车本身的油可以走startFuel公里，从起始点0向东出发达到目的地（距离起始点target公里）。路上有一些加油站，每个加油站有一定量的油，stations\[i\]\[0\]表示该加油站离起点的距离，stations\[i\]\[1\]表示该加油站的油可以支持车跑多远。现在求出车到达目的地的最少的加油次数，如果不能到达，就返回-1.

一般来说求极值问题可以使用DP问题求解。不过这个题如果简单地设为一最少加油站的次数作为转移特征很不好搞。我也是参考网上资料之后才想到DP的解法。总结如下。

设定一个N+1大小的一维数组DP（N为加油站的个数），其中DP\[i\]表示加油i次能到达的最大距离。假设我们得到了这个DP数组，只需要遍历这个数组，找到最小的i使得DP\[i\]大于等于target即可。那么如何构建这个DP数组呢？

可知，DP\[0\]=startFuel.因为不加油只能走这么远。

那么接下来就依次根据离起点远近遍历所有的加油站，所幸给定的加油站就是根据距离排序的。当我们遍历到第i个加油站，我们已经得到了目前DP\[0,...,i-1\]的当前最优值。那么就遍历这些最优值，判断其能否到达i加油站，如果能就更新其DP\[j+1\] = max(DP\[j+1\], DP\[j\]+station\[i\]\[1\]).表示在这个站加油一次之后能走的最远距离（也可能不加）。

代码如下，时间复杂度O(n2)，空间复杂度O(n).

`Runtime: 52 ms, faster than 36.23% of C++ online submissions for Minimum Number of Refueling Stops.`

`Memory Usage: 13.1 MB, less than 100.00% of C++ online submissions for Minimum Number of Refueling Stops.`

```c++
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        int len = stations.size();
        vector<long> DP(len+1, 0);
        DP[0] = startFuel;
        for(int i=0; i<len; i++){
            for(int j=i; j>=0 && DP[j]>=stations[i][0]; j--){
                DP[j+1] = max(DP[j+1], DP[j] + stations[i][1]);
            }
        }
        
        for(int i=0; i<=len; i++){
            if(DP[i] >= target) return i;
        }
        return -1;
    }
};
```

还有另一种使用Heap最大堆的办法，有时间再细看吧。

或者我想到可以使用队列的方式，从起点开始，将当前车能到达的加油站放入队列，然后遍历这个队列，对每一个计算在这个加油站加油能走到的最远的距离，再将这些路途上能到达的加油站都记录上，清空当前的队列之后，再将记录的加油站都入队。要记住，每个入队的加油站都记着车在这里加油之后可以走到的最远距离。然后每一层就相当于车多停留一个站，这个过程中随时判断车是否能到达目标，能就直接返回当前的加油次数即可。

BitBrave, 2019-10-05
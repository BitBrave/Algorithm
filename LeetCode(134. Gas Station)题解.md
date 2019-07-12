# LeetCode(134. Gas Station)题解
------
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

    If there exists a solution, it is guaranteed to be unique.
    Both input arrays are non-empty and have the same length.
    Each element in the input arrays is a non-negative integer.
Example 1:

    Input: 
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    Output: 3

    Explanation:
    Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 4. Your tank = 4 - 1 + 5 = 8
    Travel to station 0. Your tank = 8 - 2 + 1 = 7
    Travel to station 1. Your tank = 7 - 3 + 2 = 6
    Travel to station 2. Your tank = 6 - 4 + 3 = 5
    Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
    Therefore, return 3 as the starting index.
Example 2:

    Input: 
    gas  = [2,3,4]
    cost = [3,4,3]
    
    Output: -1

    Explanation:
    You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
    Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 0. Your tank = 4 - 3 + 2 = 3
    Travel to station 1. Your tank = 3 - 3 + 3 = 3
    You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
    Therefore, you can't travel around the circuit once no matter where you start.

## 解题思路
一个环形的路上有若干个加油站，每个加油站有固定的油，一辆车空车有无限容量的加油箱。从某个加油站出发，到达下一个站需要花费一定的油，现在需要找出一个出发的加油站，让这个车不会因为半路没有油而到达不了下一个站。找到了解决方案就返回对应的起始站位置，没有找到就返回-1.

这个题简单点就是从两个数组中找一个起始位置，从这个位置开始，gas的元素和的值，要大于等于cost的元素值之和。

因此，可以将gas的值对应减去cost的值，然后看看总的值之和，如果小于0就放弃，因为肯定跑不了一圈。否则，然后从gas中寻找大于等于0的数开始，然后开始计算和，一旦小于0就放弃。

然后，注意到这样一个现象：

1. 假如从位置i开始，i+1，i+2...，一路开过来一路油箱都没有空。说明什么？说明从i到i+1，i+2，...肯定是正积累。

2. 现在突然发现开往位置j时油箱空了。这说明什么？说明从位置i开始没法走完全程(废话)。那么，我们要从位置i+1开始重新尝试吗？不需要！为什么？因为前面已经知道，位置i肯定是正积累，那么，如果从位置i+1开始走更加没法走完全程了，因为没有位置i的正积累了。同理，也不用从i+2，i+3，...开始尝试。所以我们可以放心地从位置j+1开始尝试。

同时也可以这样想，思路: 累加在每个位置的left += gas[i] - cost[i], 就是在每个位置剩余的油量, 如果left一直大于0, 就可以一直走下取. 如果left小于0了, 那么就从下一个位置重新开始计数, 并且将之前欠下的多少记录下来, 如果最终遍历完数组剩下的燃料足以弥补之前不够的, 那么就可以到达, 并返回最后一次开始的位置.否则就返回-1.

证明这种方法的正确性: 

1. 如果从头开始, 每次累计剩下的油量都为整数, 那么没有问题, 他可以从头开到结束.

2. 如果到中间的某个位置, 剩余的油量为负了, 那么说明之前累积剩下的油量不够从这一站到下一站了. 那么就从下一站从新开始计数. 为什么是下一站, 而不是之前的某站呢? 因为第一站剩余的油量肯定是大于等于0的, 然而到当前一站油量变负了, 说明从第一站之后开始的话到当前油量只会更少而不会增加. 也就是说从第一站之后, 当前站之前的某站出发到当前站剩余的油量是不可能大于0的. 所以只能从下一站重新出发开始计算从下一站开始剩余的油量, 并且把之前欠下的油量也累加起来, 看到最后剩余的油量是不是大于欠下的油量.

代码如下：

Runtime: 8 ms, faster than 79.33% of C++ online submissions for Gas Station.
Memory Usage: 9.1 MB, less than 22.22% of C++ online submissions for Gas Station.

```c++
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int len = gas.size(), total = 0, res = 0, pos = 0;
        for(int i=0; i<len; i++){
            total += gas[i] - cost[i];
            res += gas[i] - cost[i];
            if(res < 0){
                res = 0;
                pos = i + 1;
            }
        }
        return total < 0 ? -1 : pos;
    }
};
```

BitBrave, 2019-07-12


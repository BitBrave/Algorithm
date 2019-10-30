# LeetCode(881. Boats to Save People)题解

The `i`-th person has weight `people[i]`, and each boat can carry a maximum weight of `limit`.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most `limit`.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

**Example 1:**

```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```

**Example 2:**

```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
```

**Example 3:**

```
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
```

**Note**:

- `1 <= people.length <= 50000`
- `1 <= people[i] <= limit <= 30000`

## 解题思路

有一些人倍困在岛上，每个人有不同的体重，现在有一条船，每条船最多可以装两个人，且两个人的体重之和不能超过一定的限制。要求计算出最少的船只，可以将这些人都运走。

最暴力的办法就是求出所有人两两组合的情况，但是这样时间复杂度肯定不能接受。因此我们可以考虑使用贪心的办法。

假设有N个人，并且已经组好了对就是最优解，a1和a2，b1和b2等等。不妨假设a1<=a2，b1<=b2，a2<=b2。这时候如果a1<=b1，我们肯定可以将a1和b1相交换，因为max(b1+a2, a1+b2)<=max(a1+a2, b1+b2)。因此对于任意两个队，如果存在一个船上的人每个人的体重都比另一个船的人轻，那这个可以进行交换，同时不必增加船的数目。

因此，我们可以使用这样一种策略，每次最重和最轻的人组队，如果能上一条船就分配到一条船，否则就给最大的单独一条船。然后在剩下的人中执行相同的策略。这样得出来的船的数量一定是最少的。因为假设有一个最优解，那么按照之前的描述，也一定可以转变成我们的这种分配方式从而不用增加船的数目。

代码如下，因为需要排序，时间复杂度O(nlogn)，空间复杂度O(1)。

`Runtime: 116 ms, faster than 58.98% of C++ online submissions for Boats to Save People.`

`Memory Usage: 13.7 MB, less than 100.00% of C++ online submissions for Boats to Save People.`

```C++
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int sta = 0, end = people.size() - 1, ret = 0;
        sort(people.begin(), people.end());
        
        while(sta < end){
            if(people[sta] + people[end] <= limit) sta++;
            end--;
            ret++;
        }
        if(sta == end) return ret + 1;
        return ret;
    }
};
```

BitBrave，2019-10-30
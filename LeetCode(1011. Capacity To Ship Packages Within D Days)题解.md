# LeetCode(\1011. Capacity To Ship Packages Within D Days)题解

A conveyor belt has packages that must be shipped from one port to another within `D` days.

The `i`-th package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `D` days.

 

**Example 1:**

```
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
```

**Example 2:**

```
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

**Example 3:**

```
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
```

 

**Note:**

1. `1 <= D <= weights.length <= 50000`
2. `1 <= weights[i] <= 500`

## 解题思路

把一个数组按顺序输入，每天一艘船，并且每天船的承载量相同，在D天之内需要全部运出去。求每艘船的承载量最少是多少。

这个可以使用二分搜索的思路，二分枚举船的载重，载重下限是最大物品的重量，载重上限是所有物品的和，然后求中点是否满足D天内运输完成，如果满足则进一步降低上限，不满足就提高下限，直到找到刚好满足D天运输完成为止。

时间复杂度为O(NlogM)，空间复杂度O(N)，N为包裹数目，M为总的重量。

`Runtime: 104 ms, faster than 6.49% of C++ online submissions for Capacity To Ship Packages Within D Days.`

`Memory Usage: 12.9 MB, less than 11.11% of C++ online submissions for Capacity To Ship Packages Within D Days.`

```c++
class Solution {
public:
    bool isOK(vector<int>& Sum, int len, int w, int D) {
        int d = 1, j = 0;
        for (int i=1; i<=len; i++) {
            if (Sum[i]-Sum[j] <= w) continue;
            d += 1;
            j = i - 1;
            if (d > D) return false;
        }
        return true;
    }
    int shipWithinDays(vector<int>& weights, int D) {
        int len = weights.size(), m = 0;
        vector<int> Sum(len + 1, 0);
        for (int i=0; i<len; i++) {
            Sum[i+1] = Sum[i] + weights[i];
            m = max(m, weights[i]);
        }
        
        int l = m, r = Sum[len], mid;
        while (l < r) {
            mid = (l + r) / 2;
            if (isOK(Sum, len, mid, D)) r = mid;
            else l = mid + 1;
        }
        return r;
    }
};
```

BitBrave，2020-01-23
# LeetCode(875. Koko Eating Bananas)题解

Koko loves to eat bananas.  There are `N` piles of bananas, the `i`-th pile has `piles[i]` bananas.  The guards have gone and will come back in `H` hours.

Koko can decide her bananas-per-hour eating speed of `K`.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than `K` bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer `K` such that she can eat all the bananas within `H` hours.

**Example 1:**

```
Input: piles = [3,6,7,11], H = 8
Output: 4
```

**Example 2:**

```
Input: piles = [30,11,23,4,20], H = 5
Output: 30
```

**Example 3:**

```
Input: piles = [30,11,23,4,20], H = 6
Output: 23
```

**Note:**

- `1 <= piles.length <= 10^4`
- `piles.length <= H <= 10^9`
- `1 <= piles[i] <= 10^9`

## 解题思路

Koko喜欢吃香蕉。有N堆香蕉，第i堆有成堆的香蕉。守卫走了，将在H小时后回来。Koko可以决定她每小时的香蕉进食速度K.她每小时选择一堆香蕉，然后从那一堆中吃K根香蕉。如果堆中的香蕉少于K个，她将全部吃掉，并且在此小时内不再吃香蕉。Koko喜欢慢慢吃东西，但仍想在警卫回来之前吃完所有香蕉。返回最小整数K，以便她可以在H小时内吃掉所有香蕉。

因为Koko每小时最多吃一堆香蕉，H一定大于等于香蕉的堆数。如果要在H个小时之内吃完所有的香蕉，最基本的只要保证每小时Koko都吃掉一堆就可以了，因此K的答案一定小于等于Max(piles[i])。同时K>=1。

确定了K的范围，就可以进行二分搜索了，得到上下界，如果上下界相同，表示得到了界。否则就没有，然后取中间数，查看是否满足H个小时的限制，如果满足，表示一定大于等于这个数，如果不满足，表示答案一定小于这个数。直接找左区间、右区间即可。

代码如下，设最大的香蕉数为N，香蕉堆数为M，则时间复杂度为O(MlogN)。空间复杂度O(1)。

`Runtime: 68 ms, faster than 45.77% of C++ online submissions for Koko Eating Bananas.`

`Memory Usage: 10.2 MB, less than 100.00% of C++ online submissions for Koko Eating Bananas.`

```C++
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int H) {
        int spend_time, len = piles.size(), sta = 1, end = 0, mid;
        for(int p : piles) end = max(p, end);
        
        while(sta < end){
            mid = (sta + end) / 2;
            spend_time = 0;
            for(int p : piles) spend_time += ceil(1.0 * p / mid);
            if(spend_time > H) sta = mid + 1;
            else end = mid;
        }

        return end;
    }
};
```

BitBrave，2019-10-22
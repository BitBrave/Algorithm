# LeetCode(846. Hand of Straights)题解

Alice has a `hand` of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size `W`, and consists of `W` consecutive cards.

Return `true` if and only if she can.

**Example 1:**

```
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
```

**Example 2:**

```
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
```

**Note:**

1. `1 <= hand.length <= 10000`
2. `0 <= hand[i] <= 10^9`
3. `1 <= W <= hand.length`

## 解题思路

给一个数组A，和一个数W，要求将A分成不同的子集，每个子集有W个元素，元素必须是顺序排列的。问是否可以成功分出来。

这个题可以使用暴力解法，直接就将数组排序，然后从小到大，挨个删除一组数，看看是否满足条件，注意元素是有重合的，因此需要判断一下。

代码如下，时间复杂度$ O(n^2) $，空间复杂度 $ O(1) $:

`Runtime: 328 ms, faster than 6.99% of C++ online submissions for Hand of Straights.Memory Usage: 9.9 MB, less than 100.00% of C++ online submissions for Hand of Straights.`

```c++
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        if(hand.size() % W != 0) return false;
        sort(hand.begin(), hand.end());
        int last_val = -1, last = 0;
        while(hand.size()>0){
            last_val = hand[0];
            last = 1;
            hand.erase(hand.begin());
            for(int i=0; i<hand.size(); i++){
                if(last == W) break;
                if(hand[i] == last_val + 1){    
                    last_val = hand[i];
                    last++;
                    hand.erase(hand.begin()+i);
                    i--;
                }
            }
            if(last != W) return false;
        }
        return true;
    }
};
```

BitBrave, 2019-09-07
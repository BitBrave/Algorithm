# LeetCode(822. Card Flipping Game)题解

On a table are `N` cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card. 

If the number `X` on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output `0`.

Here, `fronts[i]` and `backs[i]` represent the number on the front and back of card `i`. 

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

**Example:**

```
Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.
```

**Note:**

1. `1 <= fronts.length == backs.length <= 1000`.
2. `1 <= fronts[i] <= 2000`.
3. `1 <= backs[i] <= 2000`.

## 解题思路

有N张卡片，每个卡片有正反两面，各有一个数字（正整数）。现在可以随便翻转一些卡片，使得其正反面互换，然后选中一个卡片，如果这张卡片背面的数字与所有正面的卡片中的数字都不一样，那么这个数字就是“Good”。现在请问这样的数字最小是多少？返回最小的数字，如果没有，就返回0。

这个题最直观也是最简单的办法就是一次选定一个卡片，然后将其余卡片随机翻转，遍历所有的情况，这样一定可以得到答案，但是时间复杂度有$O(2^n)$。肯定是不可以的。

可以观察到一个现象，如果一个卡片正面和反面的数字是一样的，那么不管怎么翻转，这个数都不可能是“good”。而假设我们记录并除去所有的正反面一样的卡片的值，对于其余卡片中的数且不与记录的值一致，寻找一个最小的数，将其对应的卡片翻转，使得对应的数在反面。对于所有正面的数，如果与这个数相同，就将对应的该卡片进行翻转，因为去掉了一样的数的卡片，所有翻转之后的正面的数与之前的数一定不相等。最后一定可以使得这个最小的数就是“Good”。

代码如下，时间复杂度$O(n)$，空间复杂度$O(n)$：

`Runtime: 16 ms, faster than 90.21% of C++ online submissions for Card Flipping Game. Memory Usage: 10.6 MB, less than 66.67% of C++ online submissions for Card Flipping Game.`

```C++
class Solution {
public:
    int flipgame(vector<int>& fronts, vector<int>& backs) {
        int len = fronts.size(), res = INT_MAX;
        set<int> S;
        for(int i=0; i<len; i++){
            if(fronts[i] == backs[i]) S.insert(backs[i]);
        }
        for(int i=0; i<len; i++){
            if(fronts[i] == backs[i]) continue;
            if(S.find(fronts[i]) == S.end()) res = min(res, fronts[i]);
            if(S.find(backs[i]) == S.end()) res = min(res, backs[i]);
        }
        return res == INT_MAX ? 0 : res;
    }
};
```

BitBrave，2019-09-15
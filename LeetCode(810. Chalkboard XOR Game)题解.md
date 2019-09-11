# LeetCode(810. Chalkboard XOR Game)题解

We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return True if and only if Alice wins the game, assuming both players play optimally.

```
Example:
Input: nums = [1, 1, 2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.
```

**Notes:**

- `1 <= N <= 1000`. 
- `0 <= nums[i] <= 2^16`.

## 解题思路

给一个数组，表示一个棋盘上的棋子，每个棋子有对应数组内的值。A和B两个人轮流从中删除一个棋子，从A先开始。判断胜负的标准是，如果一方删除一个棋子导致剩下棋子的值XOR值为0或者棋盘上没有棋子了，则落败，否则就继续下去。如果一方删除前就遇到棋盘的所有棋子XOR和为0，则获胜。假设双方都是按最优策略进行，判断A是否能获胜。

这个题虽然是Hard的难度，但是其实异常简单。分析一下就可以得知，如果一方拿到删除权时棋盘上棋子XOR为0则自动获胜，否则，如果拿到时只剩一个棋子，那么这个人必输，因为删除了就没有了。反之如果剩两个，全一样或者棋子元素值全为0则自动获胜，那么随便删除一个留下一个不为0的棋子，就能导致对方只剩一个，则我必胜。若拿到三个，除非三个的XOR值为0，否则不管删除哪一个，都会导致对方剩两个从而导致自己必输。

因此推广到一半的情况，如果A删除时棋盘棋子为奇数，那么以后每一轮都是奇数，到最后轮到A只剩一个棋子，肯定会输，除非轮到A时棋子的XOR值恰好为0。而按照双方最佳策略来说，B肯定不会给A这样的机会，因为如果B不得不给A这样的机会，那么就表示B不管删除棋盘中哪个棋子都使得其余棋子的XOR值为0，那么就表示这些值肯定都一样，一样则表示B拿到时就全部一样，B自动获胜。所以，不管怎样，A必输。

反之，如果A删除时棋盘棋子为偶数，则AB的情况倒置，A必胜。

因此代码如下，时间复杂度$O(N)$，空间复杂度$O(1)$:

`Runtime: 8 ms, faster than 98.47% of C++ online submissions for Chalkboard XOR Game.`

`Memory Usage: 8.9 MB, less than 100.00% of C++ online submissions for Chalkboard XOR Game.`

```C++
class Solution {
public:
    bool xorGame(vector<int>& nums) {
        int res = 0;
        for(int i:nums) res ^= i;
        return res == 0 || (nums.size() & 1) == 0;
    }
};
```

BitBrave, 2019-09-11
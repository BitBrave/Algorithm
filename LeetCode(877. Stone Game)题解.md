# LeetCode(877. Stone Game)题解

Alex and Lee play a game with piles of stones.  There are an even number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`.

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return `True` if and only if Alex wins the game.

 

**Example 1:**

```
Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
```

 

**Note:**

1. `2 <= piles.length <= 500`
2. `piles.length` is even.
3. `1 <= piles[i] <= 500`
4. `sum(piles)` is odd.

## 解题思路

有一个从左到右一堆堆排列的石子，每堆石子有不同的数量，但是石子的总数是奇数，石子的堆数是偶数。现在A和B玩一个游戏，从A开始，轮流从左边或者右边选一堆石子，最后每个人都有相同堆数的石子，但是因为石子的数目是奇数，因此两个人的石子数不可能一样。最后，得到石子多的人获得游戏的胜利，假设A和B都是按照最优的策略选择石子，判断A是否能获胜。

这个题可以用常规的DP来做，转一下思路，A寻找最大的值，而B是从A得到的值中取值。

也可以如下思路，这个石子的数量是奇数但是堆数是偶数，所以AB一定有个胜负，如果A胜利，则不管，如果是B胜利，就将选择顺序对调，还是A胜利。因此A一定总是胜利的。比如如下策略：将初始的石子按顺序编号，按照从1到N。分别计算奇数序号堆的石子总数和偶数序号堆的石子总数，一定有一堆大的，选择大的那一系列石子堆，则可以保证最后得到最多的石子。



这个在[这个链接里]([https://github.com/MisterBooo/LeetCodeAnimation/blob/master/notes/LeetCode%E7%AC%AC877%E5%8F%B7%E9%97%AE%E9%A2%98%EF%BC%9A%E7%9F%B3%E5%AD%90%E6%B8%B8%E6%88%8F.md](https://github.com/MisterBooo/LeetCodeAnimation/blob/master/notes/LeetCode第877号问题：石子游戏.md))里有详细的解说。

代码如下。

```C++
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        return true;
    }
};
```

 BitBrave, 2019-10-05
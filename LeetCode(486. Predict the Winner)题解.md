# LeetCode(\486. Predict the Winner)题解

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

**Example 1:**

```
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you need to return False.
```



**Example 2:**

```
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
```



**Note:**

1. 1 <= length of the array <= 20.
2. Any scores in the given array are non-negative integers and will not exceed 10,000,000.
3. If the scores of both players are equal, then player 1 is still the winner.

## 解题思路

给出一串非负数，有两个人依次从数组的前面或者后面选一个数，最后依据谁选的数之和谁大谁胜利来判断。每个人都是用最优的决策，现在要求判断最开始选的人的是否可以获胜（一样也为胜利）。

这个题可以从两个方面来说，如果数组的元素个数是偶数，那么根据奇偶判断，第一个人可以一直选择选奇数或者偶数，从而可以始终保持胜利。

如果数组元素是奇数，就不一定了，有的人可能会想说奇数的话第一个人选定一个数之后就是偶数了呀，然后可以使用上述的方法解决，这是不可以的，因为上面的方法只能保证胜利，不能保证是最优的。

所以如果是奇数，还是使用DP最好，我们用一个二维数组作为DP，DP\[i\]\[j\]表示第i个和第j个元素之间，第一个人能选的最多的数和第二个人能选的最优数的差值。那么状态转移方程就是DP\[i\]\[j\]=max(nums[i]-DP\[i-1\]\[j\], nums[j]-DP\[i\]\[j-1\])。这里使用减法的原因是第一个人选定了之后，那么剩下的数组内，第二个人先选，所以第一个人就变成后选的了。

代码如下，时间复杂度O(n2)，空间复杂度O(n2)。

`Runtime: 4 ms, faster than 70.40% of C++ online submissions for Predict the Winner.`

`Memory Usage: 8.5 MB, less than 77.78% of C++ online submissions for Predict the Winner.`

```C++
class Solution {
    
public:
    bool PredictTheWinner(vector<int>& nums) {
        int len = nums.size(), odd = 0, even = 0;
        if(len % 2 == 0) return true;
        vector<vector<int>> D(len, vector<int>(len, 0));
        for(int i=0; i<len; i++) D[i][i] = nums[i];
        for(int k=2; k<=len; k++){
            for(int i=0; i<=len-k; i++){
                D[i][i+k-1] = max(nums[i]-D[i+1][i+k-1], nums[i+k-1]-D[i][i+k-2]);
            }
        }
        return D[0][len-1] >= 0;
    }
};
```

BitBrave，2019-12-09
# LeetCode(789. Escape The Ghosts)题解

You are playing a simplified Pacman game. You start at the point `(0, 0)`, and your destination is` (target[0], target[1])`. There are several ghosts on the map, the i-th ghost starts at` (ghosts[i][0], ghosts[i][1])`.

Each turn, you and all ghosts simultaneously *may* move in one of 4 cardinal directions: north, east, west, or south, going from the previous point to a new point 1 unit of distance away.

You escape if and only if you can reach the target before any ghost reaches you (for any given moves the ghosts may take.) If you reach any square (including the target) at the same time as a ghost, it doesn't count as an escape.

Return True if and only if it is possible to escape.

```
Example 1:
Input: 
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
Output: true
Explanation: 
You can directly reach the destination (0, 1) at time 1, while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.
Example 2:
Input: 
ghosts = [[1, 0]]
target = [2, 0]
Output: false
Explanation: 
You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.
Example 3:
Input: 
ghosts = [[2, 0]]
target = [1, 0]
Output: false
Explanation: 
The ghost can reach the target at the same time as you.
```

**Note:**

- All points have coordinates with absolute value <= `10000`.
- The number of ghosts will not exceed `100`.

## 解题思路

你从(0, 0)位置出发，需要到达目的地(target[0], target[1])，不过周围有许多鬼魂，你和它们每次可以向4个方向移动一格，问你是否能在被鬼魂碰到之前到达目的地，同时到达也不算逃脱成功。

输入一个列表ghosts，列表鬼魂所在的位置。target表示你需要到达的目的地。

这题看上去很难，感觉可能需要遍历所有的情况才能找到最后的答案。然而却并不需要。考虑下第二个案例，为何鬼魂拦在我们和目的地之间，我们就无法顺利到达？如果考虑我们始终选择最短路径到达目的地（因为如果我们不选择最短路径，则鬼魂的移动范围则会增加），则鬼魂也可以选择最短路径去目标处埋伏你。所以问题就转化为，你到达目的地的最快速度，是否能比鬼魂快。这样这道题就很好解答了。至于为什么鬼魂不再中途拦截，可以看下这篇文章的解释Why interception in the middle is not a good idea for ghosts.或则我们考虑个极端点的情况，如果鬼魂能比你更快的到达目的地，则它可以一直在目的地蹲守，这样无论如何你都不能逃脱（其实鬼魂每次必须移动，但是在格子行进过程中碰到你也算是失败，所以可以简化为鬼混可以在原地蹲守）。



代码如下，时间复杂度O(n)，空间复杂度O(n)，可以O(1)。

`Runtime: 60 ms, faster than 34.63% of Python3 online submissions for Escape The Ghosts.`

`Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Escape The Ghosts.`

```python
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        P = [abs(p[0]-target[0])+abs(p[1]-target[1]) for p in ghosts]
        dis = abs(target[0]) + abs(target[1])
        return True if dis<min(P) else False
```

BitBrave，2019-10-19
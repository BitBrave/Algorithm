# LeetCode(756. Pyramid Transition Matrix)题解

We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.

We are allowed to place any color block `C` on top of two adjacent blocks of colors `A` and `B`, if and only if `ABC` is an allowed triple.

We start with a bottom row of `bottom`, represented as a single string. We also start with a list of allowed triples `allowed`. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

**Example 1:**

```
Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.
```

 

**Example 2:**

```
Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
```

 

**Note:**

1. `bottom` will be a string with length in range `[2, 8]`.
2. `allowed` will have length in range `[0, 200]`.
3. Letters in all strings will be chosen from the set `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}`.

## 解题思路

我们正在堆叠块以形成金字塔。每个块都有一个字母字符串的颜色。当且仅当ABC是允许的三元组时，我们才可以将任何颜色块C放置在两个相邻的颜色A和B块之上。我们从底部的底部一行开始，以单个字符串表示。我们还从允许的三元组列表开始。每个允许的三元组都表示为长度为3的字符串。如果我们可以一路建造金字塔，则返回true，否则返回false。

这个题可以直接使用DFS，首先将允许的三元组变为一个set，然后每次遍历情况，使用DFS一层层往上填充，如果能填充到最后，则返回true，不能则返回false。

代码如下，时间复杂度理论上为所有的可能情况。空间复杂度就O(n)。

`Runtime: 68 ms, faster than 6.33% of Python3 online submissions for Pyramid Transition Matrix.`

`Memory Usage: 15.3 MB, less than 50.00% of Python3 online submissions for Pyramid Transition Matrix.`

```python
class Solution:
    Set = set()
    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    def DFS(self, S: str) -> bool:
        if len(S) == 1: return True
        ret = [""]
        for i in range(len(S) - 1):
            T = [a for a in self.A if S[i] + S[i+1] + a in self.Set]
            if len(T) == 0: return False 
            R = []
            for t in T:
                R += ([r + t for r in ret])
            ret = R  
        
        for r in ret:
            if self.DFS(r): return True
        return False
        
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.Set = set(allowed)
        return self.DFS(bottom)
```

BitBrave, 2019-10-12
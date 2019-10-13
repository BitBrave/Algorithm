# LeetCode(752. Open the Lock)题解

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the 4 wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

**Example 1:**

```
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
```



**Example 2:**

```
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
```



**Example 3:**

```
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
```



**Example 4:**

```
Input: deadends = ["0000"], target = "8888"
Output: -1
```



**Note:**

1. The length of `deadends` will be in the range `[1, 500]`.
2. `target` will not be in the list `deadends`.
3. Every string in `deadends` and the string `target` will be a string of 4 digits from the 10,000 possibilities `'0000'` to `'9999'`.

## 解题思路

前面有一个带4个圆形轮子的锁。每个轮子有10个插槽：“ 0”，“ 1”，“ 2”，“ 3”，“ 4”，“ 5”，“ 6”，“ 7”，“ 8”，“ 9”。轮子可以自由旋转并环绕：例如，我们可以将“ 9”设为“ 0”，或者将“ 0”设为“ 9”。每一步包括将一个车轮转动一个槽。锁最初从“ 0000”开始，该字符串表示4个车轮的状态。您将获得死胡同列表，这意味着如果锁显示以下任何一种代码，则锁的轮子将停止转动，并且您将无法打开它。给定一个目标值，该目标值代表将解锁锁的轮子的值，则返回打开锁所需的最小总转数；如果不可能，则返回-1。

简单的说就是平时行李箱上的密码，怎么转最小的次数而且不要转到特定的值来打开它。

这个题可以使用BFS，维护一个队列，首先将0000入队，然后查看队列，从队首取值，再依次对每个值进行变换，每次只变一个值，每个值可以选择变大变小或者不变，一共有8（除去原本的）种组合方式，判断这里面有没有目标值，有就结束算法，否则将这些入队继续上面的步骤。但是要注意，已经进入过队列的不要再入队，因此要用一个Map记录，找到目标值之后返回遍历的层数即可。

同时，如果找到目标值之后要返回路径，所以将Map的key设为入过队列的值，然后value设为这个值的前缀，就是它是通过哪个值变换而来的。这个题不需要

代码如下，因为只有四个轮子，十个数，因此时间复杂度无非是将所有的值都遍历一遍，为O(10000)，空间复杂度也是O(10000)。如果有N个轮子，M个数，那就是O(M^N)了。

`Runtime: 624 ms, faster than 65.96% of Python3 online submissions for Open the Lock.`

`Memory Usage: 14.7 MB, less than 25.00% of Python3 online submissions for Open the Lock.`

```python
class Solution:
    def Conv(self, S: str) -> List[str]:
        res = []
        for i in range(4):
            res += [S[:i]+str((int(S[i])-1)%10)+S[i+1:], S[:i]+str((int(S[i])+1)%10)+S[i+1:]]
        return res
    
    def openLock(self, deadends: List[str], target: str) -> int:
        D = set(deadends)
        if "0000" in D: return -1
        S = {}
        Q = ["0000"]
        
        res = 0
        M = set()
        while len(Q) > 0:
            res += 1
            lay = len(Q)
            for i in range(lay):
                R = self.Conv(Q[i])

                R = [i for i in R if i not in D and i not in M]
                if len([i for i in R if i == target]): return res
                M.update(R)
                Q += R
            Q = Q[lay:]
        return -1
```

BitBrave, 2019-10-13
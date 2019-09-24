# LeetCode(826. Most Profit Assigning Work)题解

We have jobs: `difficulty[i]` is the difficulty of the `i`th job, and `profit[i]` is the profit of the `i`th job. 

Now we have some workers. `worker[i]` is the ability of the `i`th worker, which means that this worker can only complete a job with difficulty at most `worker[i]`. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

**Example 1:**

```
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
```

**Notes:**

- `1 <= difficulty.length = profit.length <= 10000`
- `1 <= worker.length <= 10000`
- `difficulty[i], profit[i], worker[i]`  are in range `[1, 10^5]`

## 解题思路 

现在有一些工作，每个工作有不同的困难度，比如工作1的困难度3，工作2困难度4.然后每个工作有各自不同的收益。一些工人有自己的能力值，每个工人只能完成困难度不能高于自己能力值的工作，完成一个工作得到一份收益。一个工人只能完成一份工作，但是一个工作可以被多个人完成。求这种情况下，这些工人可以获得的最大收益是多少。

我们可以这样想，一个工人需要在自己能力范围内完成尽可能高收益的工作。因此直接把工人可以完成的工作中，最高收益的工作完成即可。针对每个工人，对工作进行全搜索当然可以行。但是这样会花费O(N)的时间。

因此，可以构建一个数组S，将工作W[i]按照困难度排序之后的i作为S的key，低于这个困难度的工作中最大收益作为value，这样只需要使用O(logn).就可以得到一名工人可以得到的最大收益了。但是其实也有一个Trick，可以将工人也按照能力值排序，比如从小到大，然后利用双指针法，平均花费O(1)的时间就可以得到一名工人的收益。

如何构建这个数组呢？可以先将工作按照困难度排序，然后遍历工作，从小到大，将每个元素换成小于等于这个困难度的工作中的最大收益即可，时间复杂度O(nlogn).这里有一个Trick，不要直接对困难度排序，而是建一个数组，存储各个工作的编号，对编号进行排序。

但是上述因为C++的Sort排序必须静态，我懒得自己写Sort函数。因此采用如下策略。
将任务按照difficult 从小到大排

将worker 从小到大排

对于当前的worker遍历它力所能及的工作并取最大利润

那么下一个worker在上一个worker利润基础上，继续遍历力所能及的范围

排序后one pass即可

这道题的基本逻辑是，如果workerA 比workerB能力大，那么B能获得的利润肯定比A高。

时间复杂度不变，空间复杂度反而还降低了，但是还是需要自己写排序函数，因此我选择Python。



代码如下，设工人数量M，工作数N。则空间复杂度O(1)，时间复杂度O(NlogN+MlogM+N+M)。

`Runtime: 336 ms, faster than 70.70% of Python online submissions for Most Profit Assigning Work.`

`Memory Usage: 14.3 MB, less than 100.00% of Python online submissions for Most Profit Assigning Work.`

```Python
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        index, cur_max, res = 0, 0, 0
        for ability in worker:
            while(index < len(difficulty) and ability >= jobs[index][0]):
                cur_max = max(cur_max, jobs[index][1])
                index += 1
                
            res += cur_max
        return res
```

BitBrave，2019-09-24.
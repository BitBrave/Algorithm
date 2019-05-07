# LeetCode(45. Jump Game II)题解
------
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

    Input: [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
        Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.


## 解题思路

这个题的前提是，这个题一定有解法。即我肯定可以在n-1步之内跳到最后。当然，就算是不可解的，下面的算法稍微改一改，判断一下即可。


一个比较简单的解法是，我们用一个同等长度的数组JumpTimes来记录从当前位置开始起跳的话，最少跳几次可以达到最后一个位置。我们只需要填充完则合格数组，然后返回JumpTimes\[0\]即可。如何来填充呢，可以采用如下方式：最后一个位置往前数，当当前位置的数ai>=l（l=i位置离最后一个位置的长度）时，表示只需要跳一次就可以记录JumpTimes\[i\]=1。当遇到ai<\l时，就从离i位置最远的i+ai位置开始往左数直到i+1，JumpTimes\[i\] = min(1+JumpTimes\[j\])(i+1<=j<=ai+i)，表示我多跳一次到达这些位置即可。当然，如果能直接到最后一个就直接设置JumpTimes\[i\]=1。就这样首先将i设为n-1，然后n-2，直到n=1，回到最初的地方。时间复杂度为O(n2).但这样LeetCode内会超时。


可以使用贪心的算法，假设给定的数组为A=[a1,a2,a3, ..., an]，那么可以知道我们需要从a1要跳最小的次数到an。当然如果a1直接>=n-1的话，就表示跳一次就可以到达最后面。那么如果需要跳的次数超过一次呢？首先我们考虑从开头最远跳a1的长度到达位置i，然后在这个位置最长可以跳ai的长度。这里我们可以观察到一个性质：从位置1开始跳长度l（l<=a1）到位置l+1，那么寻找一个L = max(l+al+1)，从位置1开始跳两次的长度最远都不会超过这个距离。而在后续的跳法中，就算是最优的（即跳得最少的次数）跳法里面，从开头跳两次的方法都可以改为L中的第一次的跳法。这是因为L的跳法涵盖了保证了我可以跳得最远，有最多的选择，那么就可以涵盖其它跳得不够远的情况了。

因此，我们可以说最优的办法就是第一次跳的位置就是L中的跳l长度，达到al+1，然后第二次的跳的位置就是以al+1为起始点，按照上述的策略一样。需要注意的就是，只要可以一步到达最后的位置，就可以结束算法了。

代码如下，其实可以由优化的，比如在for循环的时候，下一次的比较是不需要从sta+nums\[sta\]到sta都遍历一遍的，而只需要记录下上一次的位置pre_sta，从sta+nums\[sta\]到pre_sta+nums\[pre_sta\]即可。但是不这样效果也已经很不错了。

```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        int len = nums.size();
        if(len <= 1) return 0;
        
        int times = 0, sta = 0, tmp, tmps;
        while(sta<len-1){
            times++;
            tmp = 0;
            tmps = INT_MAX;
            for(int i=sta+nums[sta]; i>sta; i--){
                if(i>=len-1) break;
                if(tmp < i+nums[i]){
                    tmp = i+nums[i];
                    tmps = i;
                }
            }
            sta = tmps;
        }
        return times;
    }
};
```

BitBrave, 2019-05-07
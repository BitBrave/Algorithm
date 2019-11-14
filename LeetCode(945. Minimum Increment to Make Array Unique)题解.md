# LeetCode(945. Minimum Increment to Make Array Unique)题解

Given an array of integers A, a *move* consists of choosing any `A[i]`, and incrementing it by `1`.

Return the least number of moves to make every value in `A` unique.

 

**Example 1:**

```
Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
```

**Example 2:**

```
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
```

 

**Note:**

1. `0 <= A.length <= 40000`
2. `0 <= A[i] < 40000`

## 解题思路

给定一个数组，对其中每次元素可以执行一个操作，即元素值+1。求使用最少的操作使得数组内的元素都不一样。

这个题可以使用排序，首先将所有的元素从小到大排序，然后从左到右遍历。遍历到A[i]，如果和A[i-1]一样或者比A[i]小，就表示A[i]这个数需要调整，因为我们从左到右，第一次遇到需要调整的一定是两个相同元素（因为元素是从小到大排列的），那么如果遇到相同的，我们就将后面的元素+1，尽可能执行最少的加法操作。然后再向后走如果发现A[i]比A[i-1]就表示这个数肯定重复了两次以上。那么久仍旧将A[i]调整到恰好比A[i-1]大1即可。即加A[i-1]-A[i]次即可。就这样走到最后，返回ret。

如何证明这个算法是正确的呢？可以这样想，如果要想使得两个数不同，那么其中任意一个数不同即可，即+1.如果三个相同的数要不同，那么其中一个数必然要加1，另一个必然要两次加1.而比如1,1,2,3,4这样五个数，可以直接将1加到5加四次，也可以1,2,3,4各自都加1，这是一样的，因为加法是可以移植的。我们这里采用的就是第二种算法。

代码如下，时间复杂度O(nlpgn)，空间复杂度O(1)。

`Runtime: 76 ms, faster than 88.16% of C++ online submissions for Minimum Increment to Make Array Unique.`

`Memory Usage: 12 MB, less than 100.00% of C++ online submissions for Minimum Increment to Make Array Unique.`

```c++
class Solution {
public:
    int minIncrementForUnique(vector<int>& A) {
        int ret = 0, len = A.size();
        sort(A.begin(), A.end());
        
        for(int i=1; i<len; i++){
            if(A[i] > A[i-1]) continue;
            ret += A[i-1] - A[i] + 1;
            A[i] = A[i-1] + 1;
        }
        return ret;
    }
};
```

BitBrave，2019-11-14
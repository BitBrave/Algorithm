# LeetCode(837. New 21 Game)题解

Alice plays the following game, loosely based on the card game "21".

Alice starts with `0` points, and draws numbers while she has less than `K` points.  During each draw, she gains an integer number of points randomly from the range `[1, W]`, where `W` is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets `K` or more points.  What is the probability that she has `N`or less points?

**Example 1:**

```
Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
```

**Example 2:**

```
Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
```

**Example 3:**

```
Input: N = 21, K = 17, W = 10
Output: 0.73278
```

**Note:**

1. `0 <= K <= N <= 10000`
2. `1 <= W <= 10000`
3. Answers will be accepted as correct if they are within `10^-5` of the correct answer.
4. The judging time limit has been reduced for this question.

##  解题思路

新21点，给定三个数N，W，K，其中N小于等于K。每次从[1,W]中随机选一个数，累积的超过或者等于K时就停止，这时候求对应的和小于等于N的概率。

可以知道，当K大于N时，概率一定是0。

这个题可以用DP的方法求解：我们维护一个一维数组dp，其中dp[i]表示当目标为i时的概率，由于最后一次的选择的排数的范围为[i-w,i-1]，这时可选的牌有[1,w]，所以最后的点数和是[i,w+i-1]，对应我们是要求大于等于K的数，所以最后的累加范围是[K,K+W-1]，所以我们的结果便是返回dp[i]（K<=i<=K+W-1）的和。最后还有一个小技巧，由于最后的范围是[K,K+W-1]，如果N>=K+W-1（意味着在最后一次累加和[K-W,K-1]选择时，无论选择[1,W]中的任何数，最后的累加和一定在[K,N]范围内，在这种条件下[K,K+W-1]是[K,N]的子集，所以直接返回1，如果N<K+W-1，那么我们最后的答案就只用累加[K,N]的dp值即可，所以申请长度为N+1的数组即可）。

而DP的计算，按照正常的思路，代码如下：时间复杂度$O(n^2)$，空间复杂度$O(n)$:

```C++
class Solution {
public:
    double new21Game(int N, int K, int W) {
        if(N>=K+W-1 || K==0) return 1;
        double res = 0;
        vector<double> D(N+1, 0);
        D[0] = 1;
        for(int i=1; i<=K; i++){
            //if(i<=W) D[i] = 1.0/W;
            for(int j=i-1; j>=0 && i-j<=W; j--) D[i] += 1.0/W * D[j];
        }
        res = D[K];
        for(int i=K+1; i<=N; i++){
            for(int j=K-1; j>=0 && i-j<=W; j--) D[i] += 1.0/W * D[j];
            res += D[i];
        }
        return res;
    }
};
```

但是上述代码会超时，因为重复了很多无意义的计算，仔细观察第二个for循环，发现可以使用一个sum_维持最多W长度的局部概率值和，可以替代掉第二个for循环。

因此优化的代码如下，时间复杂度$O(n)$，空间复杂度$O(n)$:

`Runtime: 4 ms, faster than 82.13% of C++ online submissions for New 21 Game. Memory Usage: 11.6 MB, less than 100.00% of C++ online submissions for New 21 Game.`

```C++
class Solution {
public:
    double new21Game(int N, int K, int W) {
        if(N>=K+W-1 || K==0) return 1;
        double res = 0, sum_ = 0;
        vector<double> D(N+1, 0);
        for(int i=1; i<=N; i++){
            D[i] = i<=W ? sum_/W + 1.0/W : sum_/W;
            if(i<K) sum_ += D[i];
            else res += D[i];
            if(i>W) sum_ -= D[i-W];
        }
        return res;
    }
};
```

BitBrave, 2019-09-13
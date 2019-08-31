# LeetCode(808. Soup Servings)题解
------
There are two types of soup: type A and type B. Initially we have N ml of each type of soup. There are four kinds of operations:

 Serve 100 ml of soup A and 0 ml of soup B
 Serve 75 ml of soup A and 25 ml of soup B
 Serve 50 ml of soup A and 50 ml of soup B
 Serve 25 ml of soup A and 75 ml of soup B
When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.  

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

 

    Example:
    Input: N = 50
    Output: 0.625
    Explanation: 
    If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:

    0 <= N <= 10^9. 
    Answers within 10^-6 of the true value will be accepted as correct.

## 阶梯思路
有A，B两种汤。初始每种汤各有N毫升，现有4种操作：

1. A倒出100ml，B倒出0ml
2. A倒出75ml， B倒出25ml
3. A倒出50ml， B倒出50ml
4. A倒出25ml， B倒出75ml
每种操作的概率均等为0.25。如果汤的剩余容量不足完成某次操作，则有多少倒多少。当每一种汤都倒完时停止操作。

求A先倒完的概率，加上A和B同时倒完的概率。

这个可以用DP，DP\[i\]\[j\]分别表示A中的为i和B中为j时满足题目的概率。这题关键其实是返回1的trick，因为Notes里说了可以容忍一定的数据错误，那么当N足够大的时候，概率足够接近1，就直接返回1就可了。

代码如下,时间复杂度O(n2)，空间复杂度O(n2).(其实都是O(1)):

Runtime: 4 ms, faster than 81.50% of C++ online submissions for Soup Servings.
Memory Usage: 9 MB, less than 100.00% of C++ online submissions for Soup Servings.

```C++
class Solution {
public:
    double soupServings(int N) {
        if(N > 5000) return 1;
        N = ceil(N/25.0);
        vector<vector<double>> V;
        if(N == 0) return 0.5;
        V = vector<vector<double>>(N+1, vector<double>(N+1, 1));
        V[0][0] = 0.5;
        if(N>0) V[0][1] = 5/8.0;
        if(N>1) V[0][2] = 6/8.0;
        if(N>2) V[0][3] = 7/8.0;
        cout<<V[0][1]<<endl;
        for(int a=1; a<=N; a++){
            V[a][0] = 0.0;
            for(int b=1; b<=N; b++){
                if(a==1){
                    if(b==1) V[a][b] = 5/8.0;
                    else if(b==2) V[a][b] = 6/8.0;
                    else if(b==3) V[a][b] = 7/8.0;
                    else  V[a][b] = 1.0;
                }
                else if(a==2){
                    if(b==1) V[a][b] = 4/8.0;
                    else if(b==2) V[a][b] = 5/8.0;
                    else if(b==3) V[a][b] = 6/8.0;
                    else  V[a][b] = 6/8.0 + 0.25 * V[a-1][b-3];
                }
                else if(a==3){
                    if(b==1) V[a][b] = 3/8.0;
                    else if(b==2) V[a][b] = 4/8.0;
                    else if(b==3) V[a][b] = 4/8.0 +  0.25 * V[a-2][b-2];
                    else  V[a][b] = 4/8.0 + 0.25 * (V[a-2][b-2] + V[a-1][b-3]);
                }
                else if(a==4){
                    if(b==1) V[a][b] = 2/8.0;
                    else if(b==2) V[a][b] = 2/8.0 + 0.25 * V[a-3][b-1];
                    else if(b==3) V[a][b] = 2/8.0 +  0.25 * (V[a-3][b-1] + V[a-2][b-2]);
                    else  V[a][b] = 2/8.0 + 0.25 * (V[a-3][b-1] + V[a-2][b-2] + V[a-1][b-3]);
                }
                else{
                    if(b==1) V[a][b] = 0.25 * V[a-4][b];
                    else if(b==2) V[a][b] = 0.25 * (V[a-4][b]+ V[a-3][b-1]);
                    else if(b==3) V[a][b] = 0.25 * (V[a-4][b]+ V[a-3][b-1] + V[a-2][b-2]);
                    else  V[a][b] = 0.25 * (V[a-4][b] + V[a-3][b-1] + V[a-2][b-2] + V[a-1][b-3]);
                }
            }
        }
        return V[N][N];
    }
};
```

BitBrave, 2019-08-31
# LeetCode(\957. Prison Cells After N Days)题解

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
- Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: `cells[i] == 1` if the `i`-th cell is occupied, else `cells[i] == 0`.

Given the initial state of the prison, return the state of the prison after `N` days (and `N` such changes described above.)

 

**Example 1:**

```
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

**Example 2:**

```
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
```

 

**Note:**

1. `cells.length == 8`
2. `cells[i]` is in `{0, 1}`
3. `1 <= N <= 10^9`

## 解题思路

给有一个长度为8由0和1组成的数组，对其中的数，一个数如果两边都是1或者0，那么就将其变为1，否则变为0。求这样计算若干次之后序列是多少。

这个题肯定不能用纯暴力的办法，因为变化的次数上限是10亿次，肯定会TLE。我们可以分析，一个长度为8的01数组，那么总的组合最多只有256种，而且因为序列变化的缘故，首尾必然变换之后一直保持为0.那就必然只有最多32+1为33种，因此序列一定会以一个序列重复出现，N一定是可以缩减的。

我们使用一个Map记录变幻的序列的所处的变换次数，后边每次变换都判断这个序列是否出现过，没有就记录，出现了就表示后面的都是重复的，直接就可以通过求余得到最后答案。

代码如下，时间复杂度O(1)，空间复杂度O(1)。

`Runtime: 4 ms, faster than 89.38% of C++ online submissions for Prison Cells After N Days.`

`Memory Usage: 9.8 MB, less than 7.14% of C++ online submissions for Prison Cells After N Days.`

```c++
class Solution {
public:
    string toString(vector<int>& cells) {
        string res = "";
        for (int c : cells) res += (char)(c + 48);
        //cout<<res<<endl;
        return res;
    }
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        if (N == 0) return cells;
        vector<vector<int>> V(33, vector<int>(8, 0));
        map<string, int> M;
        int pos = 0;
        
        M[toString(cells)] = 0;
        
        for (int i=0; i<8; i++) V[0][i] = cells[i];
        for (int n=1; n<=min(33, N); n++) {
            pos = n;
            for (int i=1; i<7; i++) {
                if (V[n-1][i-1] == V[n-1][i+1]) V[n][i] = 1;
                else V[n][i] = 0;
            }
            V[n][0] = V[n][7] = 0;
            string tmp = toString(V[n]);
            if (M.find(tmp) == M.end()) M[tmp] = n;
            else {
                pos = (N - M[tmp]) % (n - M[tmp]) + M[tmp];
                break;
            }
        }
        return V[pos];
    }
};
```

BitBrave， 2020-01-07
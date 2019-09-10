# LeetCode(842. Split Array into Fibonacci Sequence)题解

Given a string `S` of digits, such as `S = "123456579"`, we can split it into a *Fibonacci-like sequence* `[123, 456, 579].`

Formally, a Fibonacci-like sequence is a list `F` of non-negative integers such that:

- `0 <= F[i] <= 2^31 - 1`, (that is, each integer fits a 32-bit signed integer type);
- `F.length >= 3`;
- and` F[i] + F[i+1] = F[i+2] `for all `0 <= i < F.length - 2`.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from `S`, or return `[]` if it cannot be done.

**Example 1:**

```
Input: "123456579"
Output: [123,456,579]
```

**Example 2:**

```
Input: "11235813"
Output: [1,1,2,3,5,8,13]
```

**Example 3:**

```
Input: "112358130"
Output: []
Explanation: The task is impossible.
```

**Example 4:**

```
Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
```

**Example 5:**

```
Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
```

**Note:**

1. `1 <= S.length <= 200`
2. `S` contains only digits.

## 解题思路

给出了一个有0-9数字组成的纯数字字符串。判断能否组成所谓的费布拉奇数列。注意这个题注重点在不管你几位数字去划分，只要满足后面的数字等于前两个的和即可。最终要返回的是任何一个组合即可。

因为只要判断能否构成即可，所以不需要res数组保存结果。回溯法仍然是对剩余的数字进行切片，看该部分切片能否满足条件。剪枝的方法是判断数组是否长度超过3，如果超过那么判断是否满足费布拉奇数列的规则。不超过3或者已经满足的条件下继续进行回溯切片。最后当所有的字符串被切片完毕，要判断下数组长度是否大于等于3，这是题目要求。

因为题目要求返回任意一个就好了，因此，只要找到一个满足条件的，那么就返回True，再结束循环就好了。


代码如下，时间复杂度理论上来说是$O(n^n)$，但是使用了很多剪枝方法，应当能到$O(n)$，空间复杂度$O(n)$：

`Runtime: 4 ms, faster than 80.17% of C++ online submissions for Split Array into Fibonacci Sequence.`

`Memory Usage: 9.5 MB, less than 100.00% of C++ online submissions for Split Array into Fibonacci Sequence.`

```C++
class Solution {
    vector<int> res;
public:
    vector<int> splitIntoFibonacci(string S) {
        isFibonacci(S, 0, S.size()-1);
        return res;
    }
    bool isFibonacci(string S, int sta, int end){
        if(sta > end) return res.size() >= 3;
        
        long long tmp = 0;
        int len = res.size();
        for(int i=0; sta+i<=end; i++){
            if(S[sta] == '0' && i>0) break;
            tmp = stoll(S.substr(sta, i+1));
            if(tmp > INT_MAX) break;
            if(len > 2 && tmp - res[len-1] > res[len-2]) break;
            if(len <= 1 || tmp - res[len-1] == res[len-2]){
                res.push_back((int)tmp);
                if(isFibonacci(S, sta+i+1, end)) return true;
                res.pop_back();
            }
        }
        return false;
    }
};
```

BitBrave, 2019-09-10
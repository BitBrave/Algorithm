# LeetCode(\779. K-th Symbol in Grammar)题解

On the first row, we write a `0`. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

Given row `N` and index `K`, return the `K`-th indexed symbol in row `N`. (The values of `K` are 1-indexed.) (1 indexed).

```
Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
```

**Note:**

1. `N` will be an integer in the range `[1, 30]`.
2. `K` will be an integer in the range `[1, 2^(N-1)]`.

## 解题思路

构造一系列的字符，第一行输入0，此后每一行对上一行的数据进行扩展，从左到右遍历上一行数据，如果是0就在下一行加入01，是1就加入10，最后下一行得到了上一行的两倍长的数据。现在给定一个整数N和K，返回第N行第K个字符。

这个我们可以思考一下，下一行的数据都是由上一行扩展开来的，理论上来说我们只要知道上一行就可以知道下一行每个位置都是什么数，以此类推我们只要知道第一行是什么数据，就可以得到任意位置的数据。比如第N行第K个是由N-1行K/2的数字决定的，只要知道这个数字和K的奇偶性就可以知道下一行的位置数据了。而K是已知的，N-1行的K/2的数据是和原来的问题是一样的。因此我们可以使用递归的方式，这样直到第一行返回0，或者K=1返回0.

代码如下，时间复杂度为min(O(N), O(logK)).

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for K-th Symbol in Grammar.`

`Memory Usage: 8 MB, less than 100.00% of C++ online submissions for K-th Symbol in Grammar.`

```C++
class Solution {
public:
    int kthGrammar(int N, int K) {
        if(N == 1 or K == 1) return 0;
        return (1-K&1) ^ kthGrammar(N-1, ceil(K/2.0));
    }
};
```

其实仔细观察，还可以知道每一行的数据，前一行半和后一半的数据都是互逆的，而前一半又和上一半一样。因此完全可以用一个for循环就可以了。

BitBrave， 2019-11-03
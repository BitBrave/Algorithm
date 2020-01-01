# LeetCode(\1247. Minimum Swaps to Make Strings Equal)题解

You are given two strings `s1` and `s2` of equal length consisting of letters `"x"` and `"y"` **only**. Your task is to make these two strings equal to each other. You can swap any two characters that belong to **different** strings, which means: swap `s1[i]` and `s2[j]`.

Return the minimum number of swaps required to make `s1` and `s2` equal, or return `-1` if it is impossible to do so.

 

**Example 1:**

```
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
```

**Example 2:** 

```
Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
```

**Example 3:**

```
Input: s1 = "xx", s2 = "xy"
Output: -1
```

**Example 4:**

```
Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4
```

 

**Constraints:**

- `1 <= s1.length, s2.length <= 1000`
- `s1, s2` only contain `'x'` or `'y'`.

## 解题思路

有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。

每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。

交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。

最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。



首先判断什么情况下必定不可能使得s1 s2相同：

1. 如果两者长度都不相等

2. x或y的总个数为奇数

如果上述条件满足任意一个，则直接返回-1。

然后分析一下题目，s1和s2只由两种字符组成， x和y。

所以s1和s2不相等的单个字符情况只有： 

1. s1[i] = y, s2[i] = x， 即yx，用一个变量pair1统计这种情况出现的次数

2. s1[i] = x, s2[i] = y,   即xy，用一个变量pair2统计这种情况出现的次数

得到pair1和pair2之后，分析一下：

显然如果有n对pair1或n对pair2，当n为偶数的情况时，只需交换 n // 2 次，

比如 有 s1 = yy, s2 = xx, 此时pair2 = 2， 只需交换s1[0]和s2[1]即可使得s1和s2相等。

当pair1和pair2都为奇数时（如果有解则pair1和pair2奇偶性必定相同），则最后剩下的yx和xy要交换两次。

比如 有 s1 = yx, s2 = xy，此时pair1 = 1， pair2 也为1，需要交换两次才能使s1和s2相等。



代码如下，时间复杂度O(n)，空间复杂度O(1).

`Runtime: 4 ms, faster than 58.27% of C++ online submissions for Minimum Swaps to Make Strings Equal.`

`Memory Usage: 8.4 MB, less than 100.00% of C++ online submissions for Minimum Swaps to Make Strings Equal.`

```c++
class Solution {
public:
    int minimumSwap(string s1, string s2) {
        int len = s1.size(), res = 0, xy = 0, yx = 0;
        for (int i=0; i<len; i++) {
            if (s1[i] == 'x' and s2[i] == 'y') xy++;
            else if (s1[i] == 'y' and s2[i] == 'x') yx++;
        };
        if ((xy + yx) % 2) return -1;
        res = xy / 2 + yx / 2 + xy % 2 + yx % 2;  
        return res;
    }
};
```

BitBrave, 2020-01-01
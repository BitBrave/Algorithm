# LeetCode(848. Shifting Letters)题解

We have a string `S` of lowercase letters, and an integer array `shifts`.

Call the *shift* of a letter, the next letter in the alphabet, (wrapping around so that `'z'` becomes `'a'`). 

For example, `shift('a') = 'b'`, `shift('t') = 'u'`, and `shift('z') = 'a'`.

Now for each `shifts[i] = x`, we want to shift the first `i+1` letters of `S`, `x` times.

Return the final string after all such shifts to `S` are applied.

**Example 1:**

```
Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
```

**Note:**

1. `1 <= S.length = shifts.length <= 20000`
2. `0 <= shifts[i] <= 10 ^ 9`

## 解题思路

给定一个字符串，和一个等长的数组，要求将字符串的每个0~i之间的字符向右移动数组内Array[i]长度。

这个题理解起来并不难，做起来也很简单，但是很容易超时，因此一定要将每个字符要移动的次数统一算出来，再进行移位，不然很多重复工，无法AC。

代码如下，时间复杂度$O(n)$，空间复杂度$O(n)$：

`Runtime: 56 ms, faster than 65.74% of C++ online submissions for Shifting Letters. Memory Usage: 11.6 MB, less than 75.00% of C++ online submissions for Shifting Letters.`

```C++
class Solution {
public:
    string shiftingLetters(string S, vector<int>& shifts) {
        int len = S.size(), sum_ = 0;
        for(int i=len-1; i>-1; i--){
            sum_ = (sum_+shifts[i]) % 26;
            shifts[i] = sum_;
        }
        for(int i=0; i<len; i++){
            shifts[i] %= 26;
            S[i] = 'a' + (S[i]+shifts[i]-'a') % 26;
        }
        return S;
    }
};
```

**BitBrave， 2019-09-09**
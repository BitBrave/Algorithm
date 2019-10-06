# 

# LeetCode(791. Custom Sort String)题解

`S` and `T` are strings composed of lowercase letters. In `S`, no letter occurs more than once.

`S` was sorted in some custom order previously. We want to permute the characters of `T` so that they match the order that `S` was sorted. More specifically, if `x` occurs before `y` in `S`, then `x` should occur before `y` in the returned string.

Return any permutation of `T` (as a string) that satisfies this property.

```
Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
```

 

**Note:**

- `S` has length at most `26`, and no character is repeated in `S`.
- `T` has length at most `200`.
- `S` and `T` consist of lowercase letters only.

## 解题思路

将字符串T重新进行排序，出现在S中的字符就按照S中出现的顺序排序，未出现的就随便排。

这是个民工题，只要将T记录每个字符出现的次数，整理成字典。然后遍历S，查看其元素是否在字典内，在就放入最后的结果，最后记录字典内有哪些没有在S中，放在最后即可。

代码如下，设S和T长n和m，时间复杂度，空间复杂度均为`O(n+m)`。

`Runtime: 32 ms, faster than 94.51% of Python3 online submissions for Custom Sort String.`

`Memory Usage: 13.5 MB, less than 5.00% of Python3 online submissions for Custom Sort String.`

```python
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        dT = {}
        res1, res2 = "", ""
        ST = set(S)
        for i in T: 
            dT[i] = 1 if not i in dT else dT[i] + 1
            if not i in ST: res2 += i

        for i in S:
            if i in dT: res1 += i * dT[i]
    
        return res1 + res2
```

BitBrave，2019-10-06

 
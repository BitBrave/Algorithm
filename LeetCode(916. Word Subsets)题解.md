# LeetCode(916. Word Subsets)题解

We are given two arrays `A` and `B` of words.  Each word is a string of lowercase letters.

Now, say that word `b` is a subset of word `a` if every letter in `b` occurs in `a`, **including multiplicity**.  For example, `"wrr"` is a subset of `"warrior"`, but is not a subset of `"world"`.

Now say a word `a` from `A` is *universal* if for every `b` in `B`, `b` is a subset of `a`. 

Return a list of all universal words in `A`.  You can return the words in any order.

 



**Example 1:**

```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
```

**Example 2:**

```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
```

**Example 3:**

```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
```

**Example 4:**

```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
```

**Example 5:**

```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
```

 

**Note:**

1. `1 <= A.length, B.length <= 10000`
2. `1 <= A[i].length, B[i].length <= 10`
3. `A[i]` and `B[i]` consist only of lowercase letters.
4. All words in `A[i]` are unique: there isn't `i != j` with `A[i] == A[j]`.

## 解题思路

给出两个字符串数组A和B，对于B中每个字符串，如果A中的某个字符串的组成元素和对应的个数均大于等于B中任意一个字符串的组成元素和对应个数，就表示A中这个字符串是宇宙字符串。要求找出所有的字符串。

这个可以使用暴力枚举，使用python中的Counter类，将B中所有字符串建立一个dict，其中存储出现的每个字符和其在某个字符串中出现的最大次数，然后对A中每个字符串也单独做这样的处理，然后对比这两个dict，如果A中的全包围B中，表示A中的这个字符串是我们想要的结果。

设A中字符串数目为N，B中为M，每个字符串长度为K，那么时间复杂度为O(N*26)=O(N)，空间复杂度O(1)。因为最多26个字母。

最普通的代码如下。

`Runtime: 884 ms, faster than 70.83% of Python3 online submissions for Word Subsets.`

`Memory Usage: 16.4 MB, less than 50.00% of Python3 online submissions for Word Subsets.`

```python
from collections import Counter
class Solution:
    def isUniversal(self, A, B):
        #print(A)
        for b in B.keys():
            if (b not in A) or (A[b] < B[b]): return False
        return True
        
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dicB = {}
        for b in B:
            b = dict(Counter(b))
            for i in b.keys():
                if i in dicB: dicB[i] = max(dicB[i], b[i])
                else: dicB[i] = b[i]
        #print(dicB)   
        ret = [a for a in A if self.isUniversal(dict(Counter(a)), dicB)]
        return ret
        
        
```

如果精简一点，就如下。

```python
from collections import Counter
class Solution:
    def isUniversal(self, A, B):
        #print(A)
        for b in B.keys():
            if A.get(b, 0) < B[b]: return False
        #return False if sum([int(True if B[b] > A.get(b, 0) else False) for b in B]) else True
        return True
        
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dicB = {}
        for b in [dict(Counter(b)) for b in B]:
            for i in b.keys():
                dicB[i] = max(dicB.get(i,0), b[i])
        #print(dicB)   
        return [a for a in A if self.isUniversal(dict(Counter(a)), dicB)]
```

BitBrave，2019-11-09
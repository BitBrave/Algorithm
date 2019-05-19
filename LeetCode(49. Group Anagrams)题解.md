# LeetCode(49. Group Anagrams)题解
------
Given an array of strings, group anagrams together.

Example:

    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

## 解题思路
Medium题，要求给多个字符串，对于用相同个数和种类的字母组合成的字符串，放入一个集合内，最后按这种方式将所有的字符串分开。直接使用map就可以，将每个字符串按照字母序排序然后作为key，然后看是否在map内，如果在就将其加入对应的value内，不在就新开一个，因为这表明这是一个不同的字符串。

写c有点麻烦，所以使用python，真的异常方便，真的想从c++转了。

Runtime: 112 ms, faster than 93.00% of Python3 online submissions for Group Anagrams.
Memory Usage: 15.8 MB, less than 81.03% of Python3 online submissions for Group Anagrams.

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}
        for item in strs:
            item_ = "".join(sorted(item))
            if item_ in ret: ret[item_].append(item)
            else: ret[item_] = [item]
        
        return list(ret.values())
```

BitBrave，2019-05-19
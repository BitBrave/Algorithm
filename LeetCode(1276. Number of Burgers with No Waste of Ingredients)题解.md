# LeetCode(\1276. Number of Burgers with No Waste of Ingredients)题解

Given two integers `tomatoSlices` and `cheeseSlices`. The ingredients of different burgers are as follows:

- **Jumbo Burger:** 4 tomato slices and 1 cheese slice.
- **Small Burger:** 2 Tomato slices and 1 cheese slice.

Return `[total_jumbo, total_small]` so that the number of remaining `tomatoSlices` equal to 0 and the number of remaining `cheeseSlices` equal to 0. If it is not possible to make the remaining `tomatoSlices` and `cheeseSlices` equal to 0 return `[]`.

 

**Example 1:**

```
Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.
```

**Example 2:**

```
Input: tomatoSlices = 17, cheeseSlices = 4
Output: []
Explantion: There will be no way to use all ingredients to make small and jumbo burgers.
```

**Example 3:**

```
Input: tomatoSlices = 4, cheeseSlices = 17
Output: []
Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
```

**Example 4:**

```
Input: tomatoSlices = 0, cheeseSlices = 0
Output: [0,0]
```

**Example 5:**

```
Input: tomatoSlices = 2, cheeseSlices = 1
Output: [0,1]
```

 

**Constraints:**

- `0 <= tomatoSlices <= 10^7`
- `0 <= cheeseSlices <= 10^7`

## 解题思路

给若干份西红柿和奶酪，每四份西红柿和1份奶酪组成大汉堡，2份西红柿和1份奶酪组成小汉堡。现在判断如果给的原料刚好用完来组成两种汉堡，就返回汉堡的数目。否则就返回空值。

这个题很简单其实，因为就是一个鸡兔同笼问题。等于就是解方程组，假设给定西红柿A份，奶酪B份，最终答案中，大汉堡X份，小汉堡为Y份，那么组成小汉堡的有Y份奶酪，2Y份西红柿，组成大汉堡的有4X份西红柿，X份奶酪。那么。

- 4X+2Y = A
- X+Y = B

解方程组，如果X和Y为整数，那么久表示有解，返回\[(4B-A)/2, (A-2B)/2\]。否则返回\[\].

代码如下，时间复杂度和空间复杂度均为O(1)。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of Burgers with No Waste of Ingredients.`

`Memory Usage: 8.2 MB, less than 100.00% of C++ online submissions for Number of Burgers with No Waste of Ingredients.`

```c++
class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        if (tomatoSlices<2*cheeseSlices or tomatoSlices>4*cheeseSlices or (4*cheeseSlices - tomatoSlices) % 2 == 1) return vector<int>();
        return vector<int>({(tomatoSlices - 2*cheeseSlices)/2, (4*cheeseSlices - tomatoSlices)/2});
    }
};
```

BitBrave，2019-12-20
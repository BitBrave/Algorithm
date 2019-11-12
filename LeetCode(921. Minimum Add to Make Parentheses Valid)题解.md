# LeetCode(921. Minimum Add to Make Parentheses Valid)题解

给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。

从形式上讲，只有满足下面几点之一，括号字符串才是有效的：

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

**Example 1:**

```
Input: "())"
Output: 1
Example 2:
```

```
Input: "((("
Output: 3
Example 3:
```

```
Input: "()"
Output: 0
Example 4:
```

```
Input: "()))(("
Output: 4
```

**Note:**

1. S.length <= 1000
2. S only consists of '(' and ')' characters.

## 解题思路

题目要求给出最少的括号使得整体有效。因此可以使用Greedy办法，我们尽量匹配尽可能多的括号，只有遇到必须匹配时才匹配。因此，可以模拟一个栈，遇到左括号就入栈，遇到右括号就用用栈内的左括号匹配，出栈一个元素，如果没有就表示无法匹配需要添加括号。这时候就加一个括号ret++。字符串遍历完成后，看看栈内的左括号数，如果存在就表示缺少右括号与之匹配。因此最后的结果就是ret+Stack.size()。

代码如下，时间复杂度O(n)，空间复杂度O(n)。

`执行用时 :0 ms, 在所有 cpp 提交中击败了100.00%的用户`

`内存消耗 :8.5 MB, 在所有 cpp 提交中击败了79.89%的用户`

```c++
class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> St;
        int ret = 0;
        for(char c : S){
            if(c == '(') St.push(c);
            else if(St.empty()) ret++;
            else St.pop();
        }
        return ret + St.size();
    }
};
```

这个题也可以不用栈，因为只需要返回需要的括号数目而不是具体的需要增加的括号位置和类型。因此我们可以这样想，一个字符串括号匹配的话，就是其从左到右，任意以最左端开始的子字符串中，偶数字符串下，左括号的数目都是大于等于和右括号的数目的。整个字符串的左括号和右括号数是相等的。

因此我们可以从左到右遍历字符串，记录遍历的左括号和右括号数目，如果走到某一个位置右括号数目大于左括号，就表示不匹配了，这时候就ret++，表示必须匹配一个了，然后左括号也加1。遍历完整个字符串之后，查看左括号和右括号的数目，返回答案ret+(左括号-右括号)即可。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`执行用时 :4 ms, 在所有 cpp 提交中击败了78.32%的用户`

`内存消耗 :8.4 MB, 在所有 cpp 提交中击败了85.63%的用户`

```C++
class Solution {
public:
    int minAddToMakeValid(string S) {
        int ret = 0, left = 0, right = 0;
        for(char c : S){
            if(c == '(') left++;
            else right++;
            
            if(left < right){
                ret++;
                left++;
            }
        }
        return ret + left - right;
    }
};
```

BitBrave，2019-11-12

```c++

```

这个题也可以不用栈，因为只需要返回需要的括号数目而不是具体的需要增加的括号位置和类型。因此我们可以这
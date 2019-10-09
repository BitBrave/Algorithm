# LeetCode(856. Score of Parentheses)题解

## 解题思路

给一个括号拓扑匹配的字符串，根据一定的规则计算其得分，单独的'()'得分1，挨着的(\*\*)(\*\*\*\*)表示就将其相加，包围着的((\*\*))外部就乘以2.

首先说说我的解法，就是遍历字符串，找出第一个(对应的右括号，然后判断这个字符串是不是全包围，如果是就用2乘以递归相同的函数，只不过输入的字符串变为S[1,len-1]的返回值，否则就分别前后相加即可。

代码如下，时间复杂度O(n2)，空间复杂度O(1)。

`Runtime: 4 ms, faster than 56.50% of C++ online submissions for Score of Parentheses.`

`Memory Usage: 9 MB, less than 12.50% of C++ online submissions for Score of Parentheses.`

```C++
class Solution {
public:
    int scoreOfParentheses(string S) {
        int len = S.size(), left = 0, right = 0;
        if(len == 2) return 1;
        for(int i=0; i<len; i++){
            if(S[i] == '(') left++;
            else right++;
            if(left == right) break;
        }
        if(left + right == len) return 2 * scoreOfParentheses(S.substr(1, len-2));
        return scoreOfParentheses(S.substr(0, left+right)) + scoreOfParentheses(S.substr(left + right));
    }
};
```

还有网络找到的。

一种方法是直接通过栈来模拟操作，这样简单易懂，如果遇到“(”，就压入栈。如果遇到右括号，判断栈顶元素是什么，如果是“(”，证明出现了”()”的情况，那么把栈顶元素弹出，压入“1”。如果是其他情况，那么先判断栈顶是不是数字，如果是数字，证明是（()()）的结构，那么这时的栈情况是（1,1），所以应该把栈里的元素相加再压入栈，一直遇到左括号，这时情况是（2），所以应该把数字2乘以2。再压入栈，这样操作完栈里会有一堆数字，我们把数字相加即可。

代码如下，时间复杂度O(n)，空间复杂度O(n)。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Score of Parentheses.`

`Memory Usage: 8.5 MB, less than 37.50% of C++ online submissions for Score of Parentheses.`

```C++
class Solution {
public:
    int scoreOfParentheses(string S) {
        int len = S.size();
        stack<int> ST; // '(' = -2
        
        for(int i=0; i<len; i++){
            if(S[i] == '(') ST.push(-2);
            else{
                if(ST.top() == -2){
                    ST.pop();
                    ST.push(1);
                }
                else{
                    int t = ST.top(); ST.pop();
                    while(ST.top() != -2){
                        t += ST.top(); ST.pop();
                    }
                    ST.pop();
                    ST.push(2 * t);
                }
            }
        }
        
        int res = ST.top(); ST.pop();
        while(!ST.empty()){
            res += ST.top(); ST.pop();
        }
        return res;
    }
};
```

还有一个办法也是用栈，但是思路不一样（不容易想，但是代码灰常简洁），

字符串中的每个位置都有一个深度，围绕它的一些匹配括号。 例如：（（）（.（））中的点的深度为2，因为这些括号满足这个规律：（__（.__））

我们的目标是将目前分数score保持在我们目前所处的深度。 当我们看到一个开括号时，我们增加了深度，我们在新深度的位置插入0。当我们看到一个结束括号时，我们将栈顶元素*2+下一个栈顶元素的的值加入新的栈。

例如，当遇到（（）（（）））时，我们的堆栈将如下所示：

- [0, 0] 遇到 (
- [0, 0, 0] 遇到 (
- [0, 1] 遇到 )
- [0, 1, 0] 遇到 (
- [0, 1, 0, 0] 遇到 (
- [0, 1, 1] 遇到 )
- [0, 3] 遇到 )
- [6] 遇到 )

代码如下，时间复杂度O(n)，空间复杂度O(n)。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Score of Parentheses.`

`Memory Usage: 8.3 MB, less than 100.00% of C++ online submissions for Score of Parentheses.`

```C++
class Solution {
public:
    int scoreOfParentheses(string S) {
        stack<int> ST;
        int a, b;
        
        ST.push(0);
        for(int s : S){
            if(s == '(') ST.push(0);
            else{
                a = ST.top(); ST.pop();
                b = ST.top(); ST.pop();
                ST.push(b + max(a * 2, 1));
            }
        }
        
        return ST.top();
    }
};
```

BitBrave， 2019-10-09
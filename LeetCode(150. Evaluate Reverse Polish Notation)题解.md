# LeetCode(150. Evaluate Reverse Polish Notation)题解
------
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

    Input: ["2", "1", "+", "3", "*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    Example 2:

    Input: ["4", "13", "5", "/", "+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6
Example 3:

    Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    Output: 22
    Explanation: 
    ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22

## 解题思路

要求使用逆波兰表达式，就是后缀计算法给出的式子，计算表达式的值。

逆波兰表达式的解释：<https://baike.baidu.com/item/%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F/128437?fr=aladdin>

直接根据上述解释就可以写代码啦。

代码如下：

Runtime: 8 ms, faster than 99.46% of C++ online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 11.6 MB, less than 49.40% of C++ online submissions for Evaluate Reverse Polish Notation.

```C++
class Solution {
public:
    bool isOperator(string a){
        if(a == "+" || a == "-" || a == "*" || a == "/") return true;
        return false;
    }
    int Cal(int a, int b, string o){
        if(o == "+") return a+b;
        if(o == "-") return a-b;
        if(o == "*") return a*b;
        if(o == "/") return a/b;
        return 0;
    }
    int evalRPN(vector<string>& tokens) {
        int len = tokens.size();
        int v1 = 0, v2 = 0;
        stack<int> S;
        
        for(int i=0; i<len; i++){
            if(!isOperator(tokens[i])){
                sscanf(tokens[i].c_str(),"%d",&v1);
                S.push(v1);
            }
            else{
                v1 = S.top(); S.pop();
                v2 = S.top(); S.pop();
                S.push(Cal(v2, v1, tokens[i]));
            }
        }
        return S.top();
    }
};
```

BitBrave, 2019-07-10
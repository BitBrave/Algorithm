# LeetCode(20. Valid Parentheses)题解
------
原文如下
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

    Input: "()"
    Output: true
Example 2:

    Input: "()[]{}"
    Output: true
Example 3:

    Input: "(]"
    Output: false
Example 4:

    Input: "([)]"
    Output: false
Example 5:

    Input: "{[]}"
    Output: true

## 题意理解，Easy题，直接使用STL的栈就可以了。代码非常简单。

代码如下：

```c++
class Solution {
public:
    bool isLeft(char c){
        switch(c){
            case '(': return true;
            case '[': return true;
            case '{': return true;
            default: return false;
        };
        return false;
    };
    bool isMatch(char a, char b){
        if((a=='(' && b==')') || (a=='[' && b==']') || (a=='{' && b=='}')) return true;
        return false;
    }
    bool isValid(string s) {
        stack<char> st;
        int len = s.size();

        for(int i = 0; i < len; i++){
            if(isLeft(s[i])) st.push(s[i]);
            else if(!st.empty()){
                if(!isMatch(st.top(), s[i])) return false;
                st.pop();
            }
            else return false;
        }
        return st.empty();
    }
};
```
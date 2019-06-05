# LeetCode(65. Valid Number)题解
------
Validate if a given string can be interpreted as a decimal number.

    Some examples:
    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true
    " -90e3   " => true
    " 1e" => false
    "e3" => false
    " 6e-1" => true
    " 99e2.5 " => false
    "53.5e93" => true
    " --6 " => false
    "-+3" => false
    "95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

    Numbers 0-9
    Exponent - "e"
    Positive/negative sign - "+"/"-"
    Decimal point - "."
    Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

## 解题思路

Hard， 给一个字符串判断是不是数字。

这个题的难度我觉得主要在于+-和e还有.上。如果一个字符串有别的字母，那么字符串肯定不是数字。而如果只有数字，那就是肯定是可以组成数的，关键就在于如何判断出现上述字符之后的字符串的判断。

我的思路是使用递归，从左到右遍历字符串。用一个位记录是否出现了e，出现了那么这之后就不能再出现除了数字之外的任意字符了，除非是在紧挨着e之后出现的-/+。+-只能出现在开头或者挨着e之后。小数点最多只能出现一次。

代码如下,这题太恶心了，字符串各种判断的条件太恶心，估计就恶心人这一点是Hard吧：

Runtime: 4 ms, faster than 95.51% of C++ online submissions for Valid Number.
Memory Usage: 10.3 MB, less than 48.86% of C++ online submissions for Valid Number.

```c++
class Solution {
public:
    bool isNumber_(string s, int sta, int len, bool exp, bool point){
        if(sta>0 && sta==len) return s[sta-1]>='0' && s[sta-1]<='9' || s[sta-1]=='.';
        if(s[sta]>='0' && s[sta]<='9') return isNumber_(s, sta+1, len, exp, point);
        if(s[sta] == '.'){
            if(point || exp) return false;
            point = true;
            return isNumber_(s, sta+1, len, exp, point); 
        }
        if(s[sta] == 'e'){
            if(exp) return false;
            if(sta>0 && !(s[sta-1]>='0' && s[sta-1]<='9')){
                if(!(sta>1 && s[sta-2]>='0' && s[sta-2]<='9')) return false;
            }
            exp = true;
            return isNumber_(s, sta+1, len, exp, point);
        }
        if(s[sta]=='+' || s[sta]=='-'){
            if(sta > 0 && s[sta-1]=='e') return isNumber_(s, sta+1, len, exp, point);
            return false;
        }
        return false;
    }
    bool isNumber(string s) {
        int len = s.size();
        if(len == 0) return false;
        while(len>0 && s[0]==' '){
            s = s.substr(1);
            len--;
        }
        while(len>0 && s[len-1]==' '){
            s.erase(len-1, 1);
            len--;
        }
        if(len == 0) return false;
        if(s[0]=='+' || s[0]=='-'){
            len--;
            s = s.substr(1);
        }
        if(len == 0) return false;
        if(s[0]=='e' || len==1 && s[0]=='.') return false;
        return isNumber_(s, 0, len, false, false);
    }
};
```

BitBrave, 2019-06-05
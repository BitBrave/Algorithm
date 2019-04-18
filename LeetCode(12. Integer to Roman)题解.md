# LeetCode(12. Integer to Roman)题解

------
原文如下：
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

    Example 1:

    Input: 3
    Output: "III"
    Example 2:

    Input: 4
    Output: "IV"
    Example 3:

    Input: 9
    Output: "IX"
    Example 4:

    Input: 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.
    Example 5:

    Input: 1994
    Output: "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

## 题目思路
这是一个Medium的题目，但其实很简单。只是将数字转为对应的罗马字符而已，数字大小在1～3999之间。因此可以从左到右分别取对应位数上的数，然后转为对应的Roman字符即可。因为确实很简单，就不过多分析了。代码如下：

```c++
class Solution {
public:
    string transNumToSym(int num, string a, string b, string c){
        switch(num){
            case 0: return ""; 
            case 1: return c; 
            case 2: return c+c; 
            case 3: return c+c+c; 
            case 4: return c+b; 
            case 5: return b;     
            case 6: return b+c; 
            case 7: return b+c+c; 
            case 8: return b+c+c+c; 
            case 9: return c+a; 
            default:
                break;
        };
        return "";
    }
    string intToRoman(int num) {
        string symbol = "";
        symbol += transNumToSym(num / 1000, "M", "M", "M"); // 1994->1=M
        num %= 1000;
        symbol += transNumToSym(num / 100, "M", "D","C"); // 994->9=CM
        num %= 100;
        symbol += transNumToSym(num / 10, "C", "L","X"); // 94->9=XC
        num %= 10;
        symbol += transNumToSym(num, "X", "V", "I"); // 4->4=IV
        return symbol; // MCMXCIV
    }
};
```

BitBrave, 2019-04-18
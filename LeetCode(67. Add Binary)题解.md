# LeetCode(67. Add Binary)题解
------
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

    Input: a = "11", b = "1"
    Output: "100"
Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"

## 解题思路

Easy， 对两个二进制进行相加而已。

直接使用加法，记录进位，从右到左遍历即可。

代码如下：

Runtime: 8 ms, faster than 51.93% of C++ online submissions for Add Binary.
Memory Usage: 9.3 MB, less than 15.35% of C++ online submissions for Add Binary.

```c++
class Solution {
public:
    string addBinary(string a, string b) {
        string res = "";
        int alen = a.size(), blen = b.size(), e = 0;
        while(alen>0 && blen>0){
            e = e + a[alen-1] - '0' + b[blen-1] - '0';
            if(e==3){
                res = '1' + res;
                e = 1;
            }
            else if(e==2){
                res = '0' + res;
                e = 1;
            }
            else if(e==1){
                res = '1' + res;
                e = 0;
            }
            else{
                res = '0' + res;
                e = 0;
            }
            alen--;
            blen--;
        }
        while(alen>0){
            e = e + a[alen-1] - '0';
            if(e==2){
                res = '0' + res;
                e = 1;
            }
            else if(e==1){
                res = '1' + res;
                e = 0;
            }
            else{
                res = '0' + res;
                e = 0;
            }
            alen--;
        }
        while(blen>0){
            e = e + b[blen-1] - '0';
            if(e==2){
                res = '0' + res;
                e = 1;
            }
            else if(e==1){
                res = '1' + res;
                e = 0;
            }
            else{
                res = '0' + res;
                e = 0;
            }
            blen--;
        }
        if(e==1) res = "1" + res;
        
        return res;
    }
};
```

BitBrave, 2019-06-05
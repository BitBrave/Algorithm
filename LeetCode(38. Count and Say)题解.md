# LeetCode(38. Count and Say)题解
------
The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

    Input: 1
    Output: "1"
Example 2:

    Input: 4
    Output: "1211"


## 解题思路
Easy题，要求根据要求进行读数。

这个题其实看了很久，好几天，每次都是看一会儿发现不懂就换了。这个乍一看是有点难懂，其实就是给一个数n表示读的次数，就是在第n次读第n-1次给出的字符串。当n等于1的时候读做1，n=2时就直接将其读作11表示1个1，n=3时将11读作2个1，返回21，当n=4时，将21读作1个2和1个1，返回1211。

代码如下，天然的递归：

```c++
class Solution {
public:
    string countAndSay(int n) {
        if(n==1) return "1";
        string tmp = countAndSay(n-1), ret = "";
        int len = tmp.size();
        int count = 1;
        for(int i=0; i<len-1; i++){
            if(tmp[i]==tmp[i+1]) count++;
            else {
                ret += count + '0';
                ret += tmp[i];
                count = 1;
            }
        }
        ret += count + '0';
        ret += tmp[len-1];
        return ret;
    }
};
```

BitBrave, 2019-05-05
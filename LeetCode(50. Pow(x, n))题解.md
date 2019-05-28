# LeetCode(50. Pow(x, n))题解
------
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

    Input: 2.00000, 10
    Output: 1024.00000
Example 2:

    Input: 2.10000, 3
    Output: 9.26100
Example 3:

    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]

## 解题思路

直接使用内置函数

```c++
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x,n)
```

```c++
class Solution {
public:
    double myPow(double x, int n) {
        return pow(x,n);
    }
};
```

通过自己实现pow函数，如果没有超过n的话，每次都将数据结果乘上自己的平方。如果数据过大，就将数据不断开方，再进行相乘。

代码如下：

Runtime: 4 ms, faster than 93.26% of C++ online submissions for Pow(x, n).
Memory Usage: 8.5 MB, less than 60.47% of C++ online submissions for Pow(x, n).

```c++
class Solution {
public:
 
    double myPow(double x, int n) {
        if(n==0) return 1;
        if(n==-pow(2,31)) return pow(x, n);
        int N = abs(n);
        double res = 1;
        
        int i = 1, sign = (x<0 && N%2==1) ? -1:1;
        x = abs(x);

        while(i>=1){
            if(i<=N){
                res *= x;
                N -= i;
                if(i<pow(2,31)/2) {
                    i *= 2;
                    x *= x;
                }
            }
            else {
                i /= 2;
                x = sqrt(x);
            }
        }
        
        if(n<0) res = 1 / res;
        return sign*res;
    }
};
```

BitBrave，2019-05-28.
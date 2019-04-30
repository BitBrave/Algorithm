# LeetCode(29. Divide Two Integers)题解
------
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3
Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2
Note:

    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

## 解题思路
这是一个Medium的题，要求在不使用乘法、除法和求余数的情况下得到两个数相除的整数结果。（其实直接使用除法符号也可以AC，但这违背了题目的原则，还是不要用了）。

### 解法
最简单的方式就是在相同符号的情况下用被除数减除数，直到被除数的绝对值大小小于除数绝对值。减的次数就是除法结果，但是这样会超时，比如当被除数为2^31-1，除数为1的时候，就需要遍历2^31-1次，这是不可取的。

我们不能这么笨地一步步减，就像TCP传输报文的策略一样，只要没有遇到天花板，TCP单位时间内发送的报文是不断递增的，直到出现丢包。所以，我们可以将这种思想用在这道题上，每次不断用被除数减去除数的n倍，然后减法次数记录加上n，下一次被除数减去2n倍除数，减法记录次数加上2n，···，直到被除数不能减去除数为止。

但是这时候，不能直接返回函数，因为此时除数是初始除数的好多倍，所以不能保证被除数此时比初始除数小。比如我们假设被除数=7，除数=3，除数使用每次*2的方式增大。那么一开始7>3，被除数变为4=7-3，除数变为6=3*2，结果记录1，然后被除数4<6，但4>3，此时不能直接返回。因此接下来除数应该变为3，然后再比较，将被除数变为1=4-3，结果记录为2，再返回。

所以，综上，我们应该使用被除数-除数，然后不断增大除数，每次减去之后，除数增大，当不能相减时，除数应该逐步回退到初始大小，然后直到被除数与初始大小的除数都不能相减后，函数才能结束。

这里有一个问题，除数以什么方式增大，最简单的方式是每次*2，然后回退的时候每次/2，但是题目要求不要用*和/号，那么我们就一丁点都不用。这里有个方式增大，设立两个变量：fore=1，back=0，然后每次增大的时候，fore=fore+back，back则变为上一次的fore，这样（fore，back）就每次为（1，0）（1，1）（2，1）（3，2）（5，3）（8，5）···。然后回退的时候，fore=back，back=fore-back。因为fore-back恰好是上一次迭代的back，所以可以不断回退。这就完全不需要使用*和/了。

PS：这个题的数使用int记录值，要特别注意越界的问题，int的取值范围是[-2^31, 2^31)。

代码如下，其实也可以不用每次都减，可以先不断增大除数直到不能减的前一个即最大的可以减的除数，然后减去之后再逐步减小，保证每次被除数减去除数的时候，除数总是被除数可以减去的最大倍数的除数，但是我这样写就可以达到最快的速度，所以就不改了（4ms）：

```c++
class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend==-pow(2,31) && divisor==-1) return pow(2,31)-1;
        if(dividend==-pow(2,31) && divisor==1) return -pow(2,31);
        
        bool s = ((dividend<0 && divisor<0)||(dividend>0 && divisor>0)) ? true:false;
        if(dividend!=-pow(2,31))
            dividend = dividend>0 ? -dividend:dividend;
        if(divisor!=-pow(2,31))        
            divisor = divisor>0 ? -divisor:divisor;
        
        int res = 0;
        int temp;
        int fore = 1, back = 0;
        int fore_div = divisor, back_div = 0;
        
        while(!(fore_div+back_div < dividend && back <= 0)){
            if(fore_div+back_div >= dividend){
                res += fore + back;
                dividend -= fore_div + back_div;
                
                if(-pow(2,31)-fore_div > fore_div+back_div) continue;
                temp = fore;
                fore = fore + back;
                back = temp;
                
                temp = fore_div;
                fore_div = fore_div + back_div;
                back_div = temp;
            }
            else{
                temp = fore;
                fore = back;
                back = temp - back;
                
                temp = fore_div;
                fore_div = back_div;
                back_div = temp - back_div;
            }
        }
        
        if(s) return res;
        return -res;
    }
};
```

BitBrave, 2019-04-30
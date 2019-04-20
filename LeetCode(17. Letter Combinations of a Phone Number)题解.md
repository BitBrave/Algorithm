# LeetCode(17. Letter Combinations of a Phone Number)题解

------

## 题意理解

这是一个Medium的题目，比较简单，但是我也花了一些时间才理解怎么做，特意记录下来。题目要求是给出几个数字，然后就想拼音九键一样，每个数字对应几个字母，现在输入几个数字，再输出对应的数字代表的字母的组合。比如假如2="abc",3="de",那么2代表了三个字母，3代表了两个字母。组合就有"ad","ae","bd","be","cd","ce"六种组合。就是一个乘法操作。

**但是我一开始做的时候觉得很简单，很快就写出来了。但是如何遍历所有的字母的组合再将其存到vecto\<string\>内让我卡壳了很久。**一开始想的直接for循环就可以了，每个数字来一个对应字母的for循环，但是真的写的时候发觉数字的个数决定了for循环的数目，而数字的个数是不确定的。所以这个困扰了我一会儿，最后想到可以用递归去做，但是也没有再深入细想了。

另一个思路就是，每检测到一个数字，就在结果vector里面记录下这个字符。每个数字到来就意味着当前结果数组内的vector量多上了几倍，这样不断迭代下去，也可以做到，并且只需要两个for循环。举个例子：输入的数据是234,2='abc',3='def',4='gh'，那么一开始检测到2，就在结果数组内存入[a,b,c]，然后检测到3，就在结果数组每个元素后面轮流加上字符，形成新的更大的，首先加入d形成[ad,bd,cd],然后加入e，成为[ad,bd,cd, **ae,be,ce**]，然后加入f，形成[ad,bd,cd,ad,bd,cd,**af,bf,cf**],依次类推，检测到4时加入gh，将结果数组扩大2倍。

代码如下：

```c++
class Solution {
public:
    vector<char> numToletter(char ch){
        vector<char> le;
        switch(ch){
            case '1': break;
            case '2': le.push_back('a'); le.push_back('b'); le.push_back('c'); break;
            case '3': le.push_back('d'); le.push_back('e'); le.push_back('f'); break;
            case '4': le.push_back('g'); le.push_back('h'); le.push_back('i'); break;
            case '5': le.push_back('j'); le.push_back('k'); le.push_back('l'); break;
            case '6': le.push_back('m'); le.push_back('n'); le.push_back('o'); break;
            case '7': le.push_back('p'); le.push_back('q'); le.push_back('r');  le.push_back('s'); break;
            case '8': le.push_back('t'); le.push_back('u'); le.push_back('v'); break;
            case '9': le.push_back('w'); le.push_back('x'); le.push_back('y'); le.push_back('z'); break;
        }
        return le;
    }
    
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        vector< vector<char>> R;
        int len = digits.size();
        string st;

        if(len == 0) return res;
        for(int i = 0; i < len; i++) R.push_back(numToletter(digits[i]));

        string ss; 

        for(int j = 0; j < R[0].size(); j++) {
            ss = "";
            ss.push_back(R[0][j]);
            res.push_back(ss);
        }
        
        for(int i = 1; i < len; i++){
            vector<string> t_res = res;
            
            for(int j = 0; j < R[i].size(); j++){
                if(j == 0){
                    for(int k = 0; k < t_res.size(); k++) res[k] += R[i][j];
                    continue;
                };
                
                for(int k = 0; k < t_res.size(); k++){
                    res.push_back(t_res[k] + R[i][j]);
                }
            }
        } 
        return res;
    }
};
```
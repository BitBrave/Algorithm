# LeetCode(68. Text Justification)题解
------
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

    Input:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    Output:
    [
    "This    is    an",
    "example  of text",
    "justification.  "
    ]
Example 2:

    Input:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    Output:
    [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be",
                because the last line must be left-justified instead of fully-justified.
                Note that the second line is also left-justified becase it contains only one word.
Example 3:

    Input:
    words = ["Science","is","what","we","understand","well","enough","to","explain",
            "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    Output:
    [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
    ]

## 解题思路
Hard, 给一句话组成的字符串，按照给定的长度K进行分行，每一行的字符数量为K，不足的就在每个单词之间插入空格，最后形成左对齐和右对齐的情况，最后一行不足只在最后插入空格，除此之外每一行的空格尽量均匀，不能均匀就多的在左边。

这题最主要就是有点繁琐，使用贪心策略，每行放置尽可能多的单词。就相word排版里的双侧对齐一样。

代码如下：

Runtime: 4 ms, faster than 87.96% of C++ online submissions for Text Justification.
Memory Usage: 9.4 MB, less than 5.12% of C++ online submissions for Text Justification.

```c++
class Solution {
public:
    string Justify(vector<string>& words, int sta, int end, int width, int maxWidth){
        if(sta == end){
            return words[sta] + string(maxWidth - width, ' ');
        }
        int space = end - sta;
        int restlen = maxWidth - width;
        int q = restlen / space, r = restlen % space;
        //cout<<space<<restlen<<q<<r<<endl;
        string tmp = words[sta++];
        while(sta<=end){
            tmp += string(1 + q + (r--<=0 ? 0:1), ' ') + words[sta++];
        }
        //cout<<tmp<<" "<<tmp.size()<<endl;
        return tmp;
    }
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int len = words.size();
        
        int sta = 0, end = 0, width = words[0].size();
        for(int i=1; i<len; i++){
            if(width+1+words[i].size() <= maxWidth){
                end = i;
                width += 1 + words[i].size();
            }
            else{
                res.push_back(Justify(words, sta, end, width, maxWidth));
                sta = i;
                end = i;
                width = words[i].size();
            }
        }
        string tmp = words[sta++];
        while(sta<=end){
            tmp += ' ' + words[sta++];
        }
        tmp += string(maxWidth - tmp.size(), ' ');
        //cout<<tmp<<"+"<<tmp.size()<<endl;
        res.push_back(tmp);
        return res;
    }
};
```

一个稍微精简一点的：

Runtime: 4 ms, faster than 87.96% of C++ online submissions for Text Justification.
Memory Usage: 9.4 MB, less than 5.49% of C++ online submissions for Text Justification.

```c++
class Solution {
public:
    string Justify(vector<string>& words, int sta, int end, int width, int maxWidth){
        if(sta == end) return words[sta] + string(maxWidth - width, ' ');
        
        int q = (maxWidth - width) / (end - sta), r = (maxWidth - width) % (end - sta);
        string tmp = words[sta++];
        while(sta<=end) tmp += string(1 + q + (r--<=0 ? 0:1), ' ') + words[sta++];
        return tmp;
    }
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int len = words.size();
        
        int sta = 0, end = 0, width = words[0].size();
        for(int i=1; i<len; i++){
            if(width+1+words[i].size() <= maxWidth) width += 1 + words[i].size();
            else{
                res.push_back(Justify(words, sta, end, width, maxWidth));
                sta = i;
                width = words[i].size();
            }
            end = i;
        }
        string tmp = words[sta++];
        while(sta<=end) tmp += ' ' + words[sta++];
        res.push_back(tmp + string(maxWidth - tmp.size(), ' '));
        return res;
    }
};
```

BitBrave, 2019-06-06
# LeetCode(127. Word Ladder)题解
------
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    Output: 5

    Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
Example 2:

    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    Output: 0

    Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

## 解题思路
给一个开始单词和结尾单词，以及一个单词列表。每次使用列表内与开始单词相差一个字符的单词与开始单词替换，最终变成结尾单词，返回最短的转换次数。有条件如下：转换不成返回0、所有单词一样长、所有单词小写字母、列表内单词不重复、开始和结尾单词不重复且不相同。

这就是一个简单的最短路径问题。可以看成是单词为一个节点，相差一个字符的单词之间为有一条边。所以找最短路径可以使用BFS。可以使用队列的办法。首先开始单词入队列，然后弹出，选择一个相差一个的单词，入队列并在数组中删除这个单词，进入下一轮。注意在这个过程中看这个单词是否与结尾单词相等，相等就返回值。否则一直往下，如果到最后数组空了或者队列空了也没找到，就返回0.

代码如下：

Runtime: 1224 ms, faster than 20.86% of C++ online submissions for Word Ladder.
Memory Usage: 11.3 MB, less than 96.72% of C++ online submissions for Word Ladder.

```c++
class Solution {
public:
    bool adjacent(string a, string b, int wl){
        int c = 0;
        while(--wl >= 0){
            c += a[wl] == b[wl] ? 0 : 1;
        }
        return c == 1;
    }
    bool inExist(string endWord, vector<string>& wordList, int len){
        while(--len >= 0){
            if(endWord == wordList[len]) return true;
        }
        return false;
    }
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        int wl = beginWord.size(), len = wordList.size();
        int res = 1, c = 0;
        if(!inExist(endWord, wordList, len)) return 0;
        queue<string> Q;
        Q.push(beginWord);
        c++;
        while(!Q.empty()){
            int tl = Q.size();
            string t;
            while(tl > 0){
                t = Q.front(); Q.pop();
                for(int i=0; i<len; i++){
                    if(adjacent(t, wordList[i], wl)){
                        if(wordList[i] == endWord) return res + 1;
                        Q.push(wordList[i]);
                        
                        wordList.erase(wordList.begin() + i);
                        i--;
                        len--;
                    }
                }
                tl--;
                
            } 
            res++;
        }
        return 0;
    }
};
```

BitBrave, 2019-07-06
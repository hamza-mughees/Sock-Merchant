# Sock Merchant
Click [here](https://www.hackerrank.com/challenges/sock-merchant/problem) to view the problem on the HackerRank website

[![Run on Repl.it](https://repl.it/badge/github/hamza-mughees/Sock-Merchant)](https://repl.it/github/hamza-mughees/Sock-Merchant)

John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are <img src="/tex/b47d8bea69cdf184074d99633f036765.svg?invert_in_darkmode&sanitize=true" align=middle width=40.00371704999999pt height=21.18721440000001pt/> socks with colors <img src="/tex/e6c31fc6086974fa254fe7c101439809.svg?invert_in_darkmode&sanitize=true" align=middle width=148.9819518pt height=24.65753399999998pt/>. There is one pair of color <img src="/tex/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/> and one of color <img src="/tex/76c5792347bb90ef71cfbace628572cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/>. There are three odd socks left, one of each color. The number of pairs is <img src="/tex/76c5792347bb90ef71cfbace628572cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/>.

**Function Description**

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

- n: the number of socks in the pile
- ar: the colors of each sock

**Input Format**

The first line contains an integer <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, the number of socks represented in <img src="/tex/9978ba2b8a2eb701a65496a8045523e2.svg?invert_in_darkmode&sanitize=true" align=middle width=16.56210929999999pt height=14.15524440000002pt/>.  
The second line contains <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> space-separated integers describing the colors <img src="/tex/6fc9da1442be04032d5171209f031c7b.svg?invert_in_darkmode&sanitize=true" align=middle width=31.35778304999999pt height=24.65753399999998pt/> of the socks in the pile.

**Constraints**

- <img src="/tex/34cc73fd43cb9c3b17b174cbef853d8b.svg?invert_in_darkmode&sanitize=true" align=middle width=86.57897489999999pt height=21.18721440000001pt/>
- <img src="/tex/ad355cf29cf7c848ad9709a586616f2e.svg?invert_in_darkmode&sanitize=true" align=middle width=108.06988169999997pt height=24.65753399999998pt/> where <img src="/tex/47b09516931ac5804a75178523b31909.svg?invert_in_darkmode&sanitize=true" align=middle width=67.58457419999999pt height=21.68300969999999pt/>

**Output Format**

Return the total number of matching pairs of socks that John can sell.

**Sample Input**
```
9
10 20 20 10 10 30 50 10 20
```

**Sample Output**
```
3
```

**Explanation**

![](https://s3.amazonaws.com/hr-challenge-images/25168/1474122392-c7b9097430-sock.png)

John can match three pairs of socks.

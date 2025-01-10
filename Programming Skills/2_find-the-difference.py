# https://leetcode.com/problems/find-the-difference/

from collections import defaultdict

def findTheDifference(s: str, t: str) -> str:
    d = defaultdict(int)
    for i in range(len(s)):
        d[s[i]] += 1
        d[t[i]] += 1  
    d[t[-1]] += 1     
    for i, j in d.items():
        if (j % 2) != 0:
            return i
        
# def findTheDifference(s: str, t: str) -> str:
#     ch = 0
#     for i in s:
#         ch ^= ord(i)
#     for i in t:
#         ch ^= ord(i)
#     return chr(ch)    

# ord() - Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
# chr() - Return the string representing a character whose Unicode code point is the integer i

if __name__ == "__main__":
    res = findTheDifference(s = "abcd", t = "abcde")
    print(res)
    res = findTheDifference(s = "", t = "y")
    print(res)
    res = findTheDifference(s = "a", t = "aa")
    print(res)    
    res = findTheDifference(s = "aaaas", t = "saaaaa")
    print(res)
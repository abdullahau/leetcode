# https://leetcode.com/problems/valid-anagram/
from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_d = defaultdict(int)
    t_d = defaultdict(int)
    for i in range(len(s)):
        s_d[s[i]] += 1
        t_d[t[i]] += 1
        
    return s_d == t_d

# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):return False 
#     for c in set(s):
#         if s.count(c) != t.count(c):
#             return False 
#     return True 

# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     s_d = {}
#     t_d = {}
#     for i in range(len(s)):
#         s_d[s[i]] = s_d.get(s[i], 0) + 1
#         t_d[t[i]] = t_d.get(t[i], 0) + 1
        
#     return s_d == t_d
                
if __name__ == "__main__":
    result = isAnagram(s='anagram', t='nagaram')
    print(result)
    
    result = isAnagram(s='rat', t='car')
    print(result)

    result = isAnagram(s='algorithm', t='logarithm')
    print(result)
    
    result = isAnagram(s='nitin', t='vipin')
    print(result)    
    
    result = isAnagram(s='ccac', t='aaca')
    print(result)
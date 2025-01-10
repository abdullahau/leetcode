# https://leetcode.com/problems/merge-strings-alternately/
from collections import deque

def mergeAlternately(word1: str, word2: str) -> str:
    iterators = deque(map(iter, [word1, word2]))
    res = ""
    while iterators:
        try:
            while True:
                res += next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            iterators.popleft()    
    return res

if __name__ == "__main__":
    res = mergeAlternately(word1 = "abc", word2 = "pqr")
    print(res)
    res = mergeAlternately(word1 = "ab", word2 = "pqrs")
    print(res)
    res = mergeAlternately(word1 = "abcd", word2 = "pq")
    print(res)
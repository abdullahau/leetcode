# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from collections import deque
# def letterCombinations(digits: str) -> list[str]:

# letter_map = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], 
#                 '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']}

letter_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
              '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
def letterCombinations(digit):
    letters = [letter_map[i] for i in digit]
    iterator = deque(map(iter, letters))
    while iterator:
        yield next(iterator[0])
        iterator.rotate(-1)

d = letterCombinations(digit='23')
print(next(d))
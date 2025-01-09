# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from collections import deque

def letterCombinations(digits):
    letter_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}    
    
    n = len(digits)
    
    # Result list to store all combinations
    combinations = []    
    if n==0: return combinations
    
    # Helper function for recursion
    def backtrack(index, current_combination):
        # Base Case (to stop recursion): If the current combination is complete, add it to the result
        if index == n:
            combinations.append("".join(current_combination))
            return
        
        # Get the letters for the current digit
        current_digit = digits[index]
        for letter in letter_map[current_digit]:
            # Add the letter to the current combination
            current_combination.append(letter)
            # Recurse for the next digit
            backtrack(index + 1, current_combination)
            # Backtrack: remove the last added letter
            current_combination.pop() 

    # Start the recursion
    backtrack(0, deque())
    return combinations       

print(letterCombinations(digits='289'))

# def letterCombinations(digits: str):
#     letter_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
#                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'} 

#     n=len(digits)
#     results=[]

#     if n==0:return results

#     def track(path:str,level:int):
#         if level==n:
#             results.append(path)
#             return
#         else:
#             possible_letters = letter_map[digits[level]]
#             for letter in possible_letters:
#                 track(path+letter,level+1)

#     track("",0)
#     return results

# print(letterCombinations(digits='289'))

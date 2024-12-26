# https://leetcode.com/problems/roman-to-integer/

roman_symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# def romanToInt(s: str) -> int:
#     res = 0
#     num_list = []
#     for i in s[::-1]:
#         num_list.append(roman_symbols[i])
#     for i in range(len(num_list)):
#         res += num_list[i]
#         if i > 0 and num_list[i] < num_list[i - 1]:
#             res -= num_list[i] * 2
#     return res

def romanToInt(s: str) -> int:
    result = 0
    for charIdx in range(len(s)-1):
        num = s[charIdx]
        if roman_symbols[num] < roman_symbols[s[charIdx + 1]]:
            result -= roman_symbols[num]
        else:
            result += roman_symbols[num]
    result+=roman_symbols[s[-1]]
    return result

if __name__ == "__main__":
    s_list = ['III', 'LVIII', 'MCMXCIV', 'XC', 'CM', 'CD']
    res = [romanToInt(i) for i in s_list]
    print(res)
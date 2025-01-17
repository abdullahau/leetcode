# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if __name__ == "__main__":
    result = strStr(haystack='sadbutsad', needle="sad")
    print(result)
    
    result = strStr(haystack='leetcode', needle='leeto')
    print(result)
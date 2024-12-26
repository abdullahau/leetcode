# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if str(x)[::-1] != str(x):
        return False
    return True


if __name__ == "__main__":
    x_list = [121, -121, 10, 242, 23432, 23422]
    result = [isPalindrome(x) for x in x_list]
    print(result)
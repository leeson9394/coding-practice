import re


def isAlphaNumeric(c):
    if 'a' <= c <= 'z':
        return True
    if 'A' <= c <= 'Z':
        return True
    if '0' <= c <= '9':
        return True
    return False


def isPalindrome(s):
    s1 = re.sub('[^a-zA-Z0-9]', '', s).lower()
    return s1 == s1[::-1]
    # left = 0
    # right = len(s) - 1
    # while left <= right:
    #     if not isAlphaNumeric(s[left]):
    #         left += 1
    #         continue
    #     if not isAlphaNumeric(s[right]):
    #         right -= 1
    #         continue
    #     if s[left].lower() == s[right].lower():
    #         left += 1
    #         right -= 1
    #     else:
    #         return False
    # return True


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))

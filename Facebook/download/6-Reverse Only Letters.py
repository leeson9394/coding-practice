import re


def reverseOnlyLetters(S):
    s = re.sub('[^a-zA-Z]', '', S)[::-1]
    r = ""
    j = 0
    for i in range(len(S)):
        if re.match('[^a-zA-Z]', S[i]):
            r += S[i]
        else:
            r += s[j]
            j += 1
    return r


if __name__ == '__main__':
    print(reverseOnlyLetters("a-bC-dEf-ghIj"))

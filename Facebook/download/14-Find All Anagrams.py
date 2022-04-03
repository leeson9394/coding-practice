# 438. https://leetcode.com/problems/find-all-anagrams-in-a-string/

def findAnagrams(s, p):
    p_dict = {}
    for c in p:
        if c in p_dict:
            p_dict[c] += 1
        else:
            p_dict[c] = 1

    if len(s) < len(p):
        return []
    s_dict = {}
    for c in s[:len(p)]:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1

    result = []
    if s_dict == p_dict:
        result.append(0)
    for i in range(len(p), len(s)):
        if s_dict[s[i-len(p)]] == 1:
            s_dict.pop(s[i-len(p)])
        else:
            s_dict[s[i-len(p)]] -= 1
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1
        if s_dict == p_dict:
            result.append(i - len(p) + 1)
    return result


if __name__ == '__main__':
    print(findAnagrams("abab", "ab"))

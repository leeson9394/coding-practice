# 1. Strings

str = 'tieba.baidu.com'
# print(str[5:])
# print(str)
# print(str.index('.'))

# for i, c in enumerate(str):
#     # print(i)
#     # print(c)
#     if c == '.':
#         print(str[i+1:])

for char in str:
    print(char)

# 2. dictionarys

dm_cnt = {'baidu.com': 900, 'com': 1600, 'facebook.com': 200, 'weibo.com': 500, 'baidu.com.cn': 200, 'com.cn': 200, 'cn': 200}

# print(dm_cnt.get('com'))

# res = []
# for v,k in dm_cnt.items():
#     res.append((k,v))
# res.sort(reverse=True)
# print(res)

# for x in dm_cnt.keys():
#     print(x)

# for x in dm_cnt.values():
#     print(x)


# 3. Lists

dm = ['aa.xx.com','bb.yy.com','ccc.sss.ddd.com']


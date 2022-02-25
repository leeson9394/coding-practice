# Given a list, counter how many times element occurs.

def counter(l):
    kv={}
    for item in l:
        if item in kv:
            kv[item] += 1
        else:
            kv[item] = 1
    return kv

my_list = [1,2,3,3,2,1,1,0,-1]
res = counter(my_list)
print(res)
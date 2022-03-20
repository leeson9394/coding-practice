# Given list with access count of websites 
# ['900, tieba.baidu.com','200, www.facebook.com','500, www.weibo.com']
# Require output count of sub domain. For example, .com will be 1600 .

from collections import defaultdict

def subdomainVisits(cpdomains):
    domain_counts = defaultdict(int)
    for item in cpdomains:
        count = item.split(',')[0]
        count = int(count)
        domains = item.split(',')[1]
        # while '.' in domains: #  parsing all subdmains for for each domain.(example: www.facebook.com)
        #     domains = domains[domains.index('.') + 1:] # remove the prefix of the string(example: facebook.com)
        #     domain_counts[domains] += count 
        
        
        for index, char in enumerate(domains): # parse but not changing domain string
            if char == '.':
                domain_counts[domains[ index + 1: ]] += count

    
    print(domain_counts)
    res = []
    for k, v in domain_counts.items():
        res.append(str(v) + ' ' + k)
    return res

arr = ['900,tieba.baidu.com','200,www.facebook.com','500,www.weibo.com','200,tieba.baidu.com.cn']
res = subdomainVisits(arr)
print(res)
# url1 = "https://finance.yahoo.com/news"
# url2 = "https://www.yahoo.co.uk/#finance"
# url3 = "https://google.com/"
# url4 = "https://google.com/search?query=groceries"


# Output1: ['finance.yahoo.com', 'yahoo.com']
# Output2: ['www.yahoo.co.uk', 'co.uk']
# Output3: ['google.com', 'google.com']
# Output4: ['google.com', 'google.com']


import re

def url_parse(url):
    res = []
    url_list = url.split("/")
    res.append(url_list[2])
    # print(url_list)

    sub_domain_list = url_list[2].split(".")
    sub_domain = sub_domain_list[-2] + "." + sub_domain_list[-1]
    # print(sub_domain_list)
    res.append(sub_domain)

    return res

url1 = "https://finance.yahoo.com/news"
url2 = "https://www.yahoo.co.uk/#finance"
url3 = "https://google.com/"
url4 = "https://google.com/search?query=groceries"
res = url_parse(url1)
print(res)
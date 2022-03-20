# """
#
# For this next exercise, we'd like to use Bash scripting.
#
# We have a log file that's currently stored on the web at this address:  https://karat-production-base-public.s3-us-west-2.amazonaws.com/content/q082/referrers.txt
#
# The log file is in a flat format where each line contains a URL and nothing else.
#
# Write a script or one-liner to download that log file and print out each domain found and the number of times it appeared in the file, in descending order by count.
#
# Sample output:
#
# 200  google.com
#  95  m.facebook.com
#  30  harvard.edu
#  15  slashdot.org
#  10  facebook.com
#
# """

# Python3 use urllib.request library

# import urllib.request

# filedata = urllib.request.urlopen('https://karat-production-base-public.s3-us-west-2.amazonaws.com/content/q082/referrers.txt')
# data= filedata.readlines()
# res = []
# for url in data:
#     url_list = str(url).split("/")
#     res.append(url_list[2])
# print(res)

import urllib.request

filedata = urllib.request.urlopen('http://karat-production-base-public.s3-us-west-2.amazonaws.com/content/q082/referrers.txt')
data= filedata.readlines()
res = []
for url in data:
    url_list = url.split("/")
    res.append(url_list[2])
    print(url_list)
# print(res)

d = {}

for domain in res:
    if domain in d:
        d[domain] += 1
    else:
        d[domain] = 1

# print(d)

result = sorted(d.items(), key = lambda x: -x[1])
print(result)
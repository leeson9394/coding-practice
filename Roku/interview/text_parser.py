# This is an output of a Cisco router, you need to write a function to return neighobr IP and its corresponding Up/Down time,
# and sort based on the one which has highest uptime

# """
# Router_1# show ip bgp summary
# For address family: IPv4 Unicast
# BGP router identifier 10.0.96.2, local AS number 2
# BGP using 1768 total bytes of memory
# BGP activity 12/0 prefixes, 14/0 paths, scan interval 60 secs
# Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down     State/PfxRcd
# 10.0.0.3        4            3       6       9        8    0    0  00:01:04      3
# 10.0.2.4        4            2       5       8        8    0    0  00:01:15      0
# 10.0.3.5        4            4       6       7        8    0    0  00:01:14      3
# 10.0.96.254     4            1       0       0        1    0    0  never       Idle 
# """

import csv

def parser(filename):
    file = csv.Dictreader(filename)
    for row in file:
        row["Neighbor"]
    
    key_value ={}
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            item_list = line.split("    ")
            neighbor = item_list[0]
            updown_time = item_list[8]
            key_value[neighbor] = updown_time
            
    return key_value
    
#     {ip: xxx, updowntime:xxx}
    
    
# cron job
# import threading

# filename = request(xx.com/router)

# res = parser(filename)


# virutalenv python version
# pip install 

# dockerfile

# alpine

# docker exec ... id sh

# docker-compose
#     volume
#     env
#     image
    
    
# kubernetes
#     svc
#     deployments
#     hpa
    
# hook send-email, slack

# dns, geo-rediction

# load balancer, level 4 vs 7, bad nodes - health check
    

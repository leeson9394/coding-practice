# Enter your code here. Read input from STDIN. Print output to STDOUT

# t=raw_input().split(" ")
# t=map(int,t)
# n=t[len(t)-1]

# i=0
# for i in range(n-2):
#     t[i+2]=t[i]+t[i+1]*t[i+1]
#     t.append(t[i+2])
    
# print t[n]

def fibbonacci(n):
    if n <= 1:
        res = n
    else:
        res = fibbonacci(n-1) + fibbonacci(n-2)
    return res

n=10
for i in range(0,n):
    print(fibbonacci(i))
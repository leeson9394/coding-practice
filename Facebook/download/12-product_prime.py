# print all possible products from a list of primes: product of two numbers, product of three number, etc.

# import numpy as np

# def productPrime(nums):
#     if not nums:
#         return []
#     res = productPrime(nums[1:])
#     return [nums[0]] + res + [i * nums[0] for i in res]

def productPrime(nums):
    res = []
    if not nums:
        return res
    dfs(res, 1, nums, 0)
    return res

def dfs(res, product, nums, start):
    if product != 1:
        res.append(product)
    for i in range(start, len(nums)):
        product *= nums[i]
        dfs(res, product, nums, i + 1)
        product //= nums[i]


if __name__ == '__main__':
    print(productPrime([2,7,11]))


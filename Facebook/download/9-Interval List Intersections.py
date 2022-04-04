# 986. https://leetcode.com/problems/interval-list-intersections/


# def intervalIntersection(A, B):
#     a_i, b_i = 0, 0
#     result = []
#     while a_i < len(A) and b_i < len(B):
#         max_start = max(A[a_i][0], B[b_i][0])
#         min_end = min(A[a_i][1], B[b_i][1])
#         if max_start <= min_end:
#             result.append([max_start, min_end])
#         if A[a_i][1] < B[b_i][1]:
#             a_i = a_i + 1
#         else:
#             b_i = b_i + 1
#     return result


def intervalIntersection(A, B):
    res = []
    for i in range(len(A)):
        for j in range(len(B)):
            max_start = max(A[i][0], B[j][0])
            min_end = min(A[i][1], B[j][1])
            if max_start <= min_end:
                res.append([max_start, min_end])
    return res

if __name__ == '__main__':
    a = [[0, 2], [5, 10], [13, 23], [24, 25]]
    b = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(intervalIntersection(a, b))

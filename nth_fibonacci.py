
def getNthFib(n):
    memo = [0]*(n + 1)
    return computeFib(n, memo)


def computeFib(n, memo):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif memo[n] > 0:
        return memo[n]

    memo[n] = computeFib(n - 1, memo) + computeFib(n - 2, memo)

    return memo[n]

result = getNthFib(6)
print(result)


# basic solution (O(2^n)):
# def getNthFib(n):
#     if n <= 1:
#         return 0
#     elif n == 2:
#         return 1

#     return getNthFib(n - 1) + getNthFib(n - 2)
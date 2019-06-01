# listOfFib = [0, 1]

def getNthFib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    return getNthFib(n - 1) + getNthFib(n - 2)

result = getNthFib(6)
print(result)
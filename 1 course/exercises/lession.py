def change(n):
    denominations = [64, 32, 16, 8, 4, 2, 1]
    result = {}

    for denom in denominations:
        if n >= denom:
            count = n // denom
            result[denom] = count
            n -= count * denom

    return result

n = int(input())

print(change(n))

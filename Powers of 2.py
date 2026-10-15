base = int(input("Enter num"))
exp = int(input("Enter exponent"))

result = 1
for i in range(1, exp + 1):
    result = result * base
    print(result)
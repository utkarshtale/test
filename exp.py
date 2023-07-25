# 10
# 12-14
# 16-18-20
# 22-24-26-28

a = 10
for i in range(1, 5):
    suffix = ''
    for j in range(1, i + 1):
        print(suffix + str(a), end='')
        suffix = '-'
        a += 2
    print()


# 0 - 24


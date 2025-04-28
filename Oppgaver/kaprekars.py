input = 5491
res = list(map(int, str(input)))
min = sorted(res)
max = sorted(res,reverse=True)

print(min, max)
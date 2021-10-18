import math

l = [1,2,3,4,5,6,7]
s = {2,3,4,5}
d = {1:"one", 2:"two"}

# print([x for x in d])

res = [x for x in range(20)]
# print(res)
# print(list(range(20)))

# res = []
# for x in range(20):
#     res.append(x)

[math.sin(x**3) for x in range(20)]

[x for x in range(20) if x != 5 if x !=10]

[f"{x}-{y}" for x in range(10) for y in range(10)]

# for x in range(10):
#     for y in range(10):
#         res.append(f"{x}-{y}")

l = [[1,2,3],[4,5,6],[7,8,9]]

# for x in l:
#     for y in x:
#         res.append(f"{x}-{y}")

[y for x in l for y in x]

{str(x):x*x for x in range(10)}

print({str(k):v for k,v in d.items() if k == 2})
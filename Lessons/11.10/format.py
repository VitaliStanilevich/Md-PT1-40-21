c = "cat"
d = "dog"
k = "kangooroo"

res = "a cat, a dog, and a kangooroo"

test = "a " + c + ", a " + d + ", and a " + k

"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog, and a "
"a cat, a dog, and a kangooroo"

pattern = "a {}, a {}, and a {}"
pattern.format(c, d, k)
"a {1}, a {2}, and a {0}".format(c, d, k)
"a {name3}, a {name1}, and a {name2}".format(name1 = c, name2 = d, name3 = k)

test = f"a {c}, a {d}, and a {k}"

print(test)
print(res == test)

print(f"{3*6-12}")
x1 = "my first string"
x2 = "my second string"

xx = f"{x1} {x2}"
print(xx)

# print("%s %d" % (42, "42"))
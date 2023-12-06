
s = set()
f = open("input.txt", "r")
lines = f.readlines()
for line in lines:
    for c in line:
        s.add(c)

print(s)

# \$/\%-=\*\+#\@\&
#tupple
n = input("Input n:\n")
n = int(n)
t = ()

line = input()
line_elements = line.split(" ")

for a in range(n):
    b = line_elements[a]
    b = int(b)
    t += (b,) #elements inserted in tupple

print(hash(t))
print(hash(line_elements)) #!New
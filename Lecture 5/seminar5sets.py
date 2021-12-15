n = input("Insert # of plants and after heights:")
n = int(n)
height = input().split(" ")
for a in range(n):
        height[a] = int(height[a])
line_set = set(height)

print(sum(line_set)/len(line_set))
n = int(input("Number: "))
flock = []
for i in range(n + 1):
    flock.append("⬛" * i)
print(*flock)

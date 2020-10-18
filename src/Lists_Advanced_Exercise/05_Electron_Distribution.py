n = int(input())

i = 1
shells = []

while n > 0:
    shell = 2 * (i**2)
    if n > shell:
        n -= shell
        shells.append(shell)
    else:
        shells.append(n)
        break
    i += 1

print(shells)

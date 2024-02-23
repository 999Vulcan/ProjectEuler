############## Your Original
def rep_div_old(n, rem, digs):
    if (rem//10)%n in digs:
        return len(digs) - digs.index((rem//10)%n)
    elif n>rem:
        digs.append(rem//10)
        return rep_div(n, rem*10, digs)
    elif rem%n==0:
        return 0
    else:
        digs.append(rem//10)
        return rep_div(n, (rem%n)*10, digs)

############## A Bit Simpler
def rep_div1(n, rem, digs):
    if (rem//10)%n in digs:
        return len(digs) - digs.index((rem//10)%n)
    if rem%n > 0:
        return rep_div(n, (rem%n)*10, digs+[rem//10])
    return 0

############## Simpler Yet
def rep_div2(n, rem, digs):
    if rem%n in digs:
        return len(digs) - digs.index(rem%n)
    if rem%n > 0:
        return rep_div(n, rem*10%n, digs+[rem])
    return 0

############## Simplest
def rep_div(n, rem, digs):
    if rem in digs:
        return len(digs) - digs.index(rem)
    if rem > 0:
        return rep_div(n, rem*10%n, digs+[rem%n])
    return 0

m = 1000
high = 0
num = 0
for i in range(2, m):
    rep = rep_div(i, 1, [])
    if rep > high: high, num = rep, i
print(num)

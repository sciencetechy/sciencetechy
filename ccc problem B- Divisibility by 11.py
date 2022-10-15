

length = 0
x = int(input("what num?"))
l = x
c = 1
u = 0
r = x

while c > 0:
    
    length += 1

    u = l // 10
    l = l // 10

    if u == 0:
        c -= 1



for i in range(length+2, 0, -1):

    val = x%10

    if val == 0:
        x = x // 10

    else:
        x = x // 10
        x -= val

    print(x)

    if x == 11:
        print(r, "is divisible by 11")
        break

    elif x < 21:
        print(r, "is not divisible by 11")
        break

    elif x < 11:
        break

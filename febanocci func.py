def febanocci(n):
    if n<=1:
        return n
    else:
        return (febanocci(n-1)+febanocci(n-2))
num=int(input())
if num<=0:
            print("invalid")
else:
    print("febanocci series:")
for i in range(num):
        print(febanocci(i))

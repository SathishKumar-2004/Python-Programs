terms = int(input("How many terms? "))
n1=0
n2=1
i=0
if terms <= 0:
    print("Please enter a positive integer")
elif terms == 1:
    print("Fibonacci sequence upto",terms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
while i<terms:
    print(n1)
    n3= n1 + n2
    n1 = n2
    n2 = n3
    i+=1

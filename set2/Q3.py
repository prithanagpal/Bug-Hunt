
n = int(input("Enter a number :"))

a = 0
b = 1
list1 = [0,1]
list2 = []
for i in range(n):
    c=a+b
    a=b
    b=c
    list1.append(c)

print(list1)

for j in list1:
    k = j*j
    list2.append(k)

print(list2)

print("Odd numbers ")
for m in list1:
  if m % 2 != 0:
    print(m)

print("Even numbers ")
for m in list1:
  if m % 2 == 0:
    print(m)

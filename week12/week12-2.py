a = [0]*100
print(a)
a[0] = 1
a[1] = 1
print(a)
for i in range(2,100):
  a[i] = a[i-1] + a[i-2]
print(a)
a=list(map(int,input().split()))


ans = a[0]
for x in a:
  if x>ans:
    ans = x
print('最大值是:', ans)

for x in a:
  print(x)
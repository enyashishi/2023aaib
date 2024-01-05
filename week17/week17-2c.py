a =int(input())
hh = a//60//60
mm = a//60%60
ss = a%60
# print(hh,mm,ss, end='')
print( f'{hh:02}:{mm:02}:{ss:02}', end='')
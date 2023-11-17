a=int(input())

if a<=2000:
	ans= 100
else: #more than 2000
	ans=100
	more = a-2000 
	ans +=more//500 * 5
	if more%500: ans += 5
	
print(ans)
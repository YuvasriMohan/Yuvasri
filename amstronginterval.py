num1=int(input())
num2=int(input())
for i in range (num1+1,num2):
	order=len(str(i))
	sum=0
	temp=i
	while temp>0:
		dig=temp%10
		sum+=dig**order
		temp//=10
	if i==sum:
		print(i)

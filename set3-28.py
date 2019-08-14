number=int(input())
mylist=[]
for i in range(number):
		mylist.append(int(input()))
for index,value in enumerate(mylist):
	print(value,index)

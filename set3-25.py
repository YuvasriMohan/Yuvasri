import statistics
n=int(input())
mylist=[]
for i in range(n):
	mylist.append(int(input()))
print(statistics.median(mylist))

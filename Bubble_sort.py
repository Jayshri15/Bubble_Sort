a=[60,80,70,30,50,10]
i=0
attempt=0
while i<len(a):
	j=0
	while j<len(a):
		if a[i]<a[j]:
			attempt=a[j]
			a[j]=a[i]
			a[i]=attempt
		j=j+1
	i=i+1
print(a)

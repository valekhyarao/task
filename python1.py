#!/usr/bin/python
sum=0;
for i in range(1,36):
	if i%5==0 and i%7!=0:
		sum=int(sum)+int(i)
print(sum)		

		

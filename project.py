import collections
import math
def freq_count(b):
	count=collections.Counter(b)
	return count
def ecludian(data):
	sum=0
	for i in data:
		sum=sum+data.get(i)**2
	value=math.sqrt(sum)
	return value
def dot_product(data1,data2):
	product=0
	for i in data1:
		if i in data2:
			product=(product)+data1.get(i)*data2.get(i)
	return product
a1=open('hello.txt','r+')
b1=a1.read().split(' ')
a2=open('hai.txt','r+')
b2=a2.read().split(' ')
c1=freq_count(b1)
c2=freq_count(b2)
d1=ecludian(c1)
d2=ecludian(c2)
e=dot_product(c1,c2)
plager=(e/(d1*d2))*100
print('uniqueness is ',100-plager,'%')






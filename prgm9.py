n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
hcf=1
for i in range(1,n1+1):
	if(n1%i==0 and n2%i==0):
		hcf=i
lcm=int((n1*n2)/hcf)
print("LCM of n1,n2 is:",lcm)

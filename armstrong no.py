num=int(input("enter a no:"))
original=num
sum=0
# variable to store sum

while num>0:
    digit =num%10
    sum=sum+digit**3
    num= num//10
if original==sum:
    print(original,"is an armstrong no")
else:
    print(original,"is not an armstrong no")
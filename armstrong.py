n=int(input("how many digits are there is your number num:"))
num=input()
num1="".join(num)
sum1=0

for i in  num1:
    integer=int(i)
    sum1=sum1+integer**n
    sum2=str(sum1)
print(sum2)


if sum2==num:
    print("armstrong number")
else:
    print("not an armstrong number")


def perfect_number(num):
    sum=0
    for i in range(1,(num//2+1)):
        if num % i ==0:
            sum+=i
    return sum==num
num=int(input("Enter the number:"))
if perfect_number(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

                   
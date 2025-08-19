#     3. WAP to check if the number is divisible by 3 and the last digit is 4.

num = int(input("enter a number : "))
if(num%3==0 and num%10==4):
    print("yes divisible by 3 and last digit is 4 ")
else:
    print("NO!!! not divisible by 3 and last digit is 4") 

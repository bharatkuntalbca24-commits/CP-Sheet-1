# WAP to check if the number is divisible by 7 or if the last digit is 5.

num = int(input("Enter a number: "))

if num % 7 == 0 and num % 10 == 5:
    print(f"{num} is divisible by 7 and ends with 5")
else:
    print(f"{num} number is not divisible by 7 ")
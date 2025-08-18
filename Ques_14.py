# Write a program to input three numbers(A, B & C) from the user and print the
# minimum element among A, B & C.


A = float(input("Enter first number (A): "))
B = float(input("Enter second number (B): "))

if A < B:
    print("Minimum:", A)
elif B < A:
    print("minimum:", B)
else:
    print("Both are equal")

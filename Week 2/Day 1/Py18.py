# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.

print ("Please, provide a number of your choice.")
num = int(input())

if num%2 == 0:
    print ("This is an even number.")
else:
    print ("This is an odd number")
#Exercise1

print("Exercise1")

num1 = int ( input("Enter first number") )
num2 = int ( input("Enter second number") )

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum: ",sum)
print("Difference: ",difference)
print("Product: ",product)
print("Quotient: ",quotient)


#Exercise2

print("Exercise2")

A = int(input("Enter first number"))
B = int(input("Enter sencond number"))
C = int(input("Enter third number"))

if A > B and A > C:
  print("The larngest number is: ", A)
elif B > A and B > C:
  print("The larngest number is: ", B)
elif C > A and C > B:
  print("The larngest number is: ", C)
elif A == B == C:
  print("All number are equal: ", A or B or C)
elif A == B:
  print("The larngest two numbers are: ", A or B)
elif A == C:
  print("The larngest two numbers are: ", A or C)
elif B == C:
  print("The larngest two numbers are: ", B or C)
else:
  print("All number are egaul.")

  
#Exercise3

print("Exercise3")

for n in range (1,100):
    m = n + 1
    if m % 3 == 0 and m % 5 == 0:
        print("FizzBuzz")
    elif m % 3 == 0:
        print("Fizz")
    elif m % 5 == 0:
        print("Buzz")
    else:
        print(m)


#Exercise4

print("Exercise4")

n = int(input("Enter the number: "))
f = 1
while n >= 1:
  f *= n
  n -= 1
print("Factorial is: ", f)


#Exercise5

print("Exercise5")

def is_palindrome(n):
    if n == n[::-1]:
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")   
n = input("Enter a string: ")    
is_palindrome(n)


# Bonus exercise

print("Bonus exercise")

def check_password_strength(pw):
    if len(pw) < 8:
        print("Password strength: Weak") 
    else:
        if (
            any(c.isupper()for c in pw)
        and any(c.islower()for c in pw) 
        and any(c.isdigit()for c in pw)
        and any (c in '!@#$%^&*()'for c in pw)
    ):
             print("Password strength: Strong")
        else:
             print("Password strength: Moderate")
    
pw = input("Enter a password to check its strength: ")
check_password_strength(pw)
n=int(input("enter any number:"))
if n%3==0 and n%5==0:
    print("Fizzbuzz")
elif n%5==0:
    print("buzz")
elif n%3==0:
    print("fizz")
else:
    print("given no is not divisible by both")
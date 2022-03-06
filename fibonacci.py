# Programme for Fibonacci series

number = int(input("How many Fibonacci numbers do you want? "))
i1 = 0
i2 = 1
counter = 0
while counter < number:
    print(i1)
    i = i1 + i2
    i1 = i2
    i2 = i
    counter = counter + 1

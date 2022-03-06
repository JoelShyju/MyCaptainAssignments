# Programme for printing all positive numbers from the input list

numbers_list = []
positives_list = []
n = 0
number = int(input("How many elements in your list? "))
for i in range(number):
    element = int(input(f"Enter element {i+1} : "))
    numbers_list.append(element)
print("Your list is ", numbers_list)
while n < len(numbers_list):
    if numbers_list[n] > 0:
        positives_list.append(numbers_list[n])
    n = n + 1
print("The positive elements are ", positives_list)

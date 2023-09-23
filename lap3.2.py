numbers = []
for i in range(10):
    while True:
        try:
            value = float(input(f"Enter value {i + 1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    numbers.append(value)

max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print("The largest number in the list is:" ,max_value)

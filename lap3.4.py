num = int(input("Enter a number: "))
print("Multiplication table for", num),
for i in range(1, 11):
    result = num * i
    print(num,"X", i, "=",result)

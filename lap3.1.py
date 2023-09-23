employee_salaries = {}
while True:
    name = input("Enter the name of the employee (or 'no' to exit): ")
    if name.lower() == 'no':
        break  
    salary = float(input("Enter the salary of {} : ".format(name)))
    employee_salaries[name] = salary

print("Employee salaries:")
for name, salary in employee_salaries.items():
    print("{}: ${:.2f}".format(name, salary))

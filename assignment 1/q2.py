def calculate_gross_salary(basic_salary):
    if basic_salary <= 10000:
        hra_percentage = 20
        da_percentage = 80
    elif basic_salary <= 20000:
        hra_percentage = 25
        da_percentage = 90
    else:
        hra_percentage = 30
        da_percentage = 95

    hra = (hra_percentage / 100) * basic_salary
    da = (da_percentage / 100) * basic_salary

    gross_salary = basic_salary + hra + da
    return gross_salary

basic_salary = float(input("Enter the basic salary of the employee: "))

gross_salary = calculate_gross_salary(basic_salary)
print(f"The gross salary is: {gross_salary}")

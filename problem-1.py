# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC(Annual Salary before deductions) - HRA(House Rent Allowance)- 10%, DA(Dearness Allowance)- 5%, PF(Provident Fund)- 3% and taxes deduction as below:
#     Salary(Lakhs) : Tax(%)
#     Below 5 : 0%
#     5-10 : 10%
#     10-20 : 20%
#     above 20 : 30%

salary = float(input("Enter your salary in lakhs: "))

hra = salary * 0.1
da = salary * 0.05
pf = salary * 0.03

if salary < 5:
    tax_rate = 0
elif salary <= 10:
    tax_rate = 0.1
elif salary <= 20: 
    tax_rate = 0.2
else:
    tax_rate = 0.3

tax = salary * tax_rate

annual_salary = salary - hra - da - pf - tax
print(f"Annual Salary {annual_salary:.2f} lakhs")

monthly_salary = annual_salary / 12
print(f"Monthly Salary {monthly_salary:.2f} lakhs")
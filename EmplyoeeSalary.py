
def calculate_annual_salary(hourly_wage, hours_per_week):
  weeks_per_year = 52
  return (hourly_wage * hours_per_week * weeks_per_year)


def apply_raise(salary, percentage):
  percentage = percentage / 100
  return salary * (1 + percentage / 100)


def format_salary(salary):
  return "${:,.2f}".format(salary)



hourly_wage = float(input("What is your hourly wage? "))
hours_per_week = float(input("How many hours do you work per week? "))

initial_salary = calculate_annual_salary(hourly_wage, hours_per_week)
print(f"Initial Annual Salary: {format_salary(initial_salary)}")

raise_percentage = float(input("What is the raise percentage to apply to the salary? "))
new_salary = apply_raise(initial_salary, raise_percentage)
print(f"New Annual Salary: {raise_percentage} % raise: {format_salary(new_salary)}")


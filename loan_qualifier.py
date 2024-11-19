MIN_SALARY = 30000
YEARS_ON_JOB = 2

salary = float(input("Enter your current salary: "))
years_at_job = int(input("Enter number of years at current job: "))

if salary >= MIN_SALARY and YEARS_ON_JOB >= 2:
    print("You qualify for the loan.")
else:
    print("You must have a salary of at least", MIN_SALARY, "and worked at your job for", YEARS_ON_JOB, "to qualify for the loan.")
    
 
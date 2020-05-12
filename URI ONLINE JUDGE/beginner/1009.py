NAME = str(input())
SALARY = float(input())
SALES_TOTAL = float(input())
SALARY_BONUS = SALES_TOTAL * 0.15
TOTAL_SALARY = SALARY + SALARY_BONUS
print("TOTAL = R$ %.2f" %TOTAL_SALARY)
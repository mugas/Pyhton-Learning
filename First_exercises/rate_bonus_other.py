hours = input(" Enter hours")
rate = input(" Enter rate")
try:
    fr = float(rate)
    fh = float(hours)
except:
    print("Error, print a numeric input")
    quit()

if fh > 40:
    bonus = fr * 2
    new_salary = bonus * fh
    print("Overtime")
    print(bonus)
    print(new_salary)

else:
    print("regular")
    salary = fr * fh
    print(salary)

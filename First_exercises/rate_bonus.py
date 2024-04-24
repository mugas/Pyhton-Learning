hours = input(" Enter hours")
rate = input(" Enter rate")
fr = float(rate)
fh = float(hours)
salary = fr*fh

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

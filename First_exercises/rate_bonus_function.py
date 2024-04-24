hours = input(" Enter hours")
rate = input(" Enter rate")
fr = float(rate)
fh = float(hours)


def salary(hours, rate):
    # print("in salary", hours, rate)
    if hours > 40:
        bonus = rate * 2
        salary = bonus * hours
        print("Overtime")
    else:
        print("regular")
        salary = hours * rate
    # print("salary", salary)

    return salary


new_salary = salary(fh, fr)
print("new_salary", new_salary)

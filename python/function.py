def employee_detail(arg):
    youngest_age = arg[0]['age']
    name = ""
    for item in arg:
        if item['age'] <= youngest_age:
            youngest_age = item['age']
            name = item['name']
    print(f"Youngest employee details is {name} {youngest_age}")

def character_check(arg):
    checker = {'upper': 0, 'lower': 0};
    for char in arg:
        if char.isupper():
            checker["upper"] += 1
        elif char.islower():
            checker['lower'] += 1
        else:
            pass
    print(f"Uppercase is {checker['upper']}, Lowercase is {checker['lower']}")

def is_even(arg):
    even_numbers = []
    for num in arg:
        if num % 2 == 0:
            even_numbers.append(num)
    print(f"Even numbers {even_numbers}")


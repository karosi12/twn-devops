from datetime import datetime

bday = input("Enter date of birthday in this format DD/MM/YYYY\n")

birthday_date = datetime.strptime(bday, '%d/%m/%Y').date()
today = datetime.today()

difference_one = datetime(today.year, birthday_date.month, birthday_date.day)
difference_two = datetime(today.year + 1, birthday_date.month, birthday_date.day)

print(f"{today}")
print(f"{difference_one}")
print(f"{difference_two}")

days_till_birthday = 0
if difference_one > today:
    # birthday this year
    days_till_birthday = difference_one - today
else:
    # birthday next year
    days_till_birthday = difference_two - today   

print(f"{days_till_birthday.days} days till your birthday")

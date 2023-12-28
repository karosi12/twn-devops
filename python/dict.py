employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

for key in employee.copy():
    employee["job"] = "Software Engineer"
    if(key == 'age'):
        employee.pop(key)
        continue
    print(f"{key} {employee[key]}")

dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}

new_dict = { **dict_one, **dict_two}
sum_value = 0

for _, value in new_dict.items():
    sum_value += value

print(f"Sum: {sum_value}")
print(f"Maximum value is {max(new_dict.values())}, Minimum value is {min(new_dict.values())}")

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

for item in employees:
    print(f"My name is {item['name']}. My professional job is {item['job']}, I lived {item['address']['city']}.")

print(employees[1]['address']['country'])
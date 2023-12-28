from function import is_even, employee_detail, character_check

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

employee_detail(employees)
character_check("The Quick Brown Fox Jumps Over The Lazy Dog")
is_even([2,3,4,6,8,10,9,11,12])

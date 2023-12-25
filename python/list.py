my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
result = []

user_input = input("Enter a valid number\n")

try:
    val = int(user_input)
    for item in my_list:
        if item >= val:
            result.append(item)
    print(result)
    
except ValueError:
    print("Invalid input")
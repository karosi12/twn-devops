cal_count = 0
user_input = ""

try:
    while user_input != 'exit':
        user_input = input("Enter two valid input numbers\n")
        two_values = user_input.split(" ")
        first_value = int(two_values[0])
        second_value = int(two_values[1])
        plus = first_value + second_value
        minus = first_value - second_value
        multiply = first_value * second_value
        divide = first_value / second_value

        print(f"{plus} {minus} {multiply} {divide}")
        cal_count +=1
except ValueError:
    print("Invalid input")

print(f"{cal_count}")
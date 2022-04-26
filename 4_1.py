

# def get_number():
#     return 5

# def set_number(num):
#     number = num
#     print("From set_number, num is: ", str(num))
#     return number


# num = get_number()
# set_number(6)
# print("End of program. Num is: ", str(num))

# def add_number(num1, num2):
#     print("num1: ", str(num1))
#     print("num2: ", str(num2))
#     val = num1 + num2
#     print("from add_number, val is: ", str(val))
#     return val


# output = add_number(5, 2) # 7

# print("Output of {} and {} is {}.".format(str(2), str(5), output))

# def get_firstname(full_name):  # Lucas Phan
#     space = full_name.index(" ")
#     first_name = full_name[:space]
#     return first_name

# # my_name = get_firstname("Lucas Phan")
# # print("Hello, my name is " + my_name + ".")

# names = [
#     "Lucas Phan",
#     "Joe Biden",
#     "Mike Tyson",
#     "Tom Brady",
#     "Coby Bryant"
# ]

# for name in names:
#     my_name = get_firstname(name)
#     if my_name == "Tom":
#         print(my_name + " plays football!")
#     elif my_name == "Coby":
#         print(my_name + " plays basketball!")
#     elif my_name == "Mike":
#         print(my_name + " is into boxing!")
#     else:
#         print(my_name + " is not not into sports!")

# def pay(wage, hours):
#     amount = 0
#     if hours <= 40:
#         print("Here!")
#         amount = wage * hours
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#     return amount

# wage = eval(input("Enter the hourly wage: "))
# hours = eval(input("Enter the numbers of hours worked: "))

# result = pay(wage, hours)
# print("Earnings: ${0:,.2f}".format(result))

# def is_vowel_word(word):
#     word = word.upper()
#     vowels = ("A", "E", "I", "O", "U")
#     for vowel in vowels:
#         # if vowel not in word:
#         #     return False
#         # return True
#         # return False if vowel not in word else True
#          vowel in word
# word = input("Enter a word: ")

# if is_vowel_word(word):
#     print(word, "contains vowel.")
# else:
#     print(word, "does not contain vowel")

# PI = 3.141529
# def main():
#     y = 2
#     print(str(y) + ": function main")
#     trivial()
#     print(str(y) + ": function main")


# def trivial():
#     x = 3
#     print(str(x) + ": function trivial")
#     print(PI)
# main()
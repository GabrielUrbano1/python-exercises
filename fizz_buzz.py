


# for i in range(1, 100):
#     if i % 5 == 0  and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

empty_list = []
for i in range(1, 100):
        if i % 5 == 0  and i % 3 == 0:
            empty_list.append("FizzBuzz")
            # print()
        elif i % 5 == 0:
            empty_list.append("Buzz")
            # print("Buzz")
        elif i % 3 == 0:
            empty_list.append("Fizz")
            # print("Fizz")
        else:
            empty_list.append(i)

print(empty_list)
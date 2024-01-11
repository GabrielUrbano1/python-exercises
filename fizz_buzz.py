


# # for i in range(1, 100):
# #     if i % 5 == 0  and i % 3 == 0:
# #         print("FizzBuzz")
# #     elif i % 5 == 0:
# #         print("Buzz")
# #     elif i % 3 == 0:
# #         print("Fizz")
# #     else:
# #         print(i)

# empty_list = []
# for i in range(1, 10000000):
#         if i % 5 == 0  and i % 3 == 0:
#             empty_list.append("FizzBuzz")
#             # print()
#         elif i % 5 == 0:
#             empty_list.append("Buzz")
#             # print("Buzz")
#         elif i % 3 == 0:
#             empty_list.append("Fizz")
#             # print("Fizz")
#         else:
#             empty_list.append(i)

# print(empty_list)


# Create a sample 2D list
my_2d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Specify the indices of the element you want to update
row_index = 1  # Row index (0-based)
column_index = 2  # Column index (0-based)
print(my_2d_list)
# Update the element at the specified indices
new_value = 42
my_2d_list[row_index][column_index] = new_value

# Print the updated 2D list
for row in my_2d_list:
    print(row)
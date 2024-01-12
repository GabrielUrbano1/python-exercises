# moving zeros leetcode 282
import random

# Generate a list of 10 random numbers between 0 and 25 (inclusive)
random_list = [random.randint(0, 10) for _ in range(25)]

# print(random_list)


def move_zeros(nums):
    if not nums:
        return
    right  = 0
    left = 0

    while right < len(nums):
        if nums[right] != 0:

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return random_list


move_zeros(random_list)
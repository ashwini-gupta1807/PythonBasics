# def max(list):
#     max=0
#     for i in range(len(list)):
#         if(list[i]> max):
#             max = list[i]
#     return max

# list = [18, 9, 45, 89,112, 10, 234, 3453]
# list.sort()
# print(list[len(list)-3])

# find third max element in a list
def thirdmax(nums):
    first = second = third = float('-inf')

    for num in nums:
        # Skip duplicates
        if num == first or num == second or num == third:
            continue

        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    # If third largest doesn't exist, return the maximum
    return third if third != float('-inf') else first


nums = [2, 2, 3, 1]
print(thirdmax(nums))  # Output: 1


# Given an array of integers and a target, return a pair of indices where the corresponding values in the array add up to the target.

# Input: [5, 1, 3, 8, 4, 4], 8 
# Output: [0, 2]

# Input is a list and a number, output is a list of two numbers

# empty list > []
# no pairs > return [-1, -1]

# print(sum_targets([], target))

# Use target as number to subtract from
# Loop through list, and check each number
# If the number is less than target, we want to subtract this number from target, store remainder
# continue looping through list until remainder is found, then we have the pair
# If no remainder is found, keep looping


# dict_nums = {
#     0: 5,
#     1: 1,
#     2: 3,
#     3: 8,
#     4: 4,
#     5: 4
# }

# dict_nums[index] = value # number

# dict_nums.itervalues() loops through values
# dict_nums[key] = value
# assign variable remainder to 0 in setup
# after subtracting value, assign remainder as remaining value

def sum_targets(lst, target):

    sum_indices = []
    remainder = 0
    dict_nums = {}

    # Input: [5, 1, 3, 8, 4, 4], 8 
    for i in range(0, len(lst)):
        # Sets up dictionary
        dict_nums[i] = lst[i] # Add index: value pairs to dictionary as key/value pair
        i += 1

        # Loop through 
    for i in range(0, len(lst)):        
        # Sets remainder, and checks values of dict
        remainder = target - dict_nums[i] 
        print("remainder: ", remainder)
        if remainder in dict_nums.values():
            print("Remainder exists in dict_nums.values()")
            remainder_at_index = list(dict_nums.keys())[list(dict_nums.values()).index(remainder)]
            print("Remainder index: ", remainder_at_index)
            sum_indices.append(remainder_at_index)
            sum_indices.append(i)
            return "Sum indices: " + str(sorted(sum_indices))
            # return sum_indices
        else:
            print("No match!")
            return [-1, -1]

print(sum_targets([0, 1, 3, 4], 8))

# print("Test stuff below")

# mydict = {'george':16,'amber':19}



# dict_nums = {
#     0: 5,
#     1: 1,
#     2: 3,
#     3: 8,
#     4: 4,
#     5: 4
# }
# remainder = 3


# # print(list(mydict.keys())[list(mydict.values()).index(16)])

# # print(list(dict_nums.keys())[list(dict_nums.values()).index(remainder)])

# remainder = 3

# for number in dict_nums.values():
#     print("Dict nums values: ", dict_nums.values())
#     if number == remainder:
#         print("dict_nums keys: ", dict_nums.keys())

# print(type(dict_nums.values()))
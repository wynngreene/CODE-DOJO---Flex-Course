print("Connected")
# 1 DONE
# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def count_down(num):
    for x in range(0, num+1, 1):
        print(x)

count_down(5)


# 2 DONE
# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(num_first, num_second):
    print(num_first)
    # print(num_second)
    return num_second

print_and_return(1,2)


# 3 DONE
# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(array):
    sum = 0
    for x in range(0,len(array),1):
        sum = array[x] + sum
        print(sum)
    return sum

first_plus_length([1,2,3,4])


# 4 DONE
# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(array, num_greater):
    new_array = []
    for x in range(0,len(array),1):
        if num_greater <= array[x]:
            new_array.append(array[x])
            print(x)
            print(new_array)

values_greater_than_second([5,2,3,2,1,4],3)


# 5 DONE
# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(num_size, num_value):
    
    new_array = []
    for x in range(0,num_size, 1):
        new_array.append(num_value)
        print(new_array)
    return new_array
        
length_and_value(6,2)
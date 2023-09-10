print("Connected")

# x = [0,1,2,3,4]

# print(x)

# larva = [
#     {"id": 1, "name":"Caterpie", "typeElement":{"bug":"none"}}
# ]

# class Worm:
#     def __init__(self) -> None:
#         pass
    
#     print(__init__)

# def say_hi(name):
#     print("Hi, " + name +"!")

# say_hi("Jade")
# say_hi("Aziza")

# def full_name(first_name, last_name):
#     # your code here!
#     full_name.first_name = first_name
#     full_name.last_name = last_name
#     return first_name + " " + last_name

# name1 = full_name("Eddie", "Aikau")
# print(name1) # should print Eddie Aikau

# def be_cheerful(name="Mr.Popsicle", repeat=2): # default parameters
#     print(f"Hello {name}\n"* repeat)

# be_cheerful("Mike")
# be_cheerful()

# set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
	
# be_cheerful()# output: good morning (repeated on 2 lines)
# be_cheerful("tim")# output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")# output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)# output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)# output: good morning michael (repeated on 5 lines)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")# output: good morning kb (repeated on 3 lines)

def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
>>>[2,4,10,16]


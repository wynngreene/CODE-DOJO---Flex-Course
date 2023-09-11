# print("connected")

#01. CODE
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#01. Update Values in Dictionaries and Lists
x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students[0]["last_name"])

sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"][0])

z[0]["y"] = 30
print(z[0]["y"])


#02. CODE
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#02.Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for x in range(0,len(students),1):
        print("first_name - " + students[x]["first_name"] +",","last_name - " + students[x]["last_name"])

iterateDictionary(students)


#03. CODE
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#03.Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    if key_name == "first_name":
        for x in range(0,len(students),1):
            print(students[x]["first_name"])
    if key_name == "last_name":
        for x in range(0,len(students),1):
                print(students[x]["last_name"])

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)


#04. CODE
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#04.Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    num_Loc = len(dojo["locations"])
    print("-------------")
    print(str(num_Loc) + " LOCATIONS")
    for x in range(0,num_Loc,1):
        print(dojo["locations"][x])

    print("-------------")

    num_Instr = len(dojo["instructors"])
    print(str(num_Instr) + " INSTRUCTORS")
    for x in range(0,num_Instr,1):
        print(dojo["instructors"][x])

printInfo(dojo)
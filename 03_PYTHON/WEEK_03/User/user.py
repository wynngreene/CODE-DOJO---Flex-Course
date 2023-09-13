print("connected")

class User:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dual = True

    def first_method(self, my_stuff):
        new_Stuff = self.z + my_stuff
        return new_Stuff

new_User = User(4, 5, 6)
old_User = User(6, 7, 8)

print(old_User.z)

print(new_User.first_method(10))
print(old_User.first_method(10))
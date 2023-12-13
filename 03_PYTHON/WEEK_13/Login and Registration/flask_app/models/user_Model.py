from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash

class User:
#---START---DONE
    DB = "login_reg"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#---SAVE---DONE
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at )
                VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(),  NOW() );"""
        save_result = connectToMySQL(cls.DB).query_db(query, data)
        return save_result

#---GET_BY_EMAIL---DONE
    @classmethod
    def get_by_email(cls, data):    
        query = "SELECT * FROM users WHERE email = %(email)s;"
        email_results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(email_results[0])

#---VALIDATE_EMAIL---DONE
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        valid_email_results = connectToMySQL(User.DB).query_db(query, user)
        if len(valid_email_results) >= 1:
            flash("Email already taken")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid Email!!!")
            is_valid = False
        return is_valid

#---VALIDATE_EMAIL---DONE
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        valid_email_results = connectToMySQL(User.DB).query_db(query, user)
        if len(valid_email_results) >= 1:
            flash("Email already taken")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid Email!!!")
            is_valid = False
        return is_valid

#---VALIDATE_LOGIN---DONE
    @staticmethod
    def validate_login(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        valid_login_results = connectToMySQL(User.DB).query_db(query, user)
        
        return is_valid


# #---GET_ONE_USER---
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM cookie_orders"
#         get_all_results = connectToMySQL(cls.DB).query_db(query)
#         users = []
#         for row in get_all_results:
#             users.append( cls[row])
#         return users


# #---GET_ONE---
#     @classmethod
#     def get_one(cls, order_id):
#         query = """
#                 SELECT * FROM users
#                 WHERE id = %(id)s
#                 """
#         order_dictionary = connectToMySQL(cls.DB).query_db(query, {"id": order_id})
#         order = Cookie_order(order_dictionary[0])
#         return order

# #---EDIT---
#     @classmethod
#     def edit(cls, data):
#         query = """
#                 UPDATE cookie_orders
#                 SET full_name = %(full_name)s,
#                 cookie_type = %(cookie_type)s,
#                 number_boxes = %(number_boxes)s,
#                 updated_at = NOW()
#                 WHERE id = %(id)s;
#                 """
#         result = connectToMySQL(cls.DB).query_db(query, data)
#         return result
    


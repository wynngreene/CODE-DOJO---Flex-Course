from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
#---START---DONE
    DB = "recipe_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#---Crud|CREATE (SAVE)---
    @classmethod
    def save(cls, data):
        pass
        # query = """
        #         INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at )
        #         VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(),  NOW() );
        #         """
        # save_result = connectToMySQL(cls.DB).query_db(query, data)
        # return save_result

#---cRud|READ (GET_ONE_USER)---
    @classmethod
    def get_by_id(cls):
        query = "SELECT * FROM users"
        get_all_results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for row in get_all_results:
            users.append( cls[row])
        return users
        

#---cRud|READ (GET_ALL_USER)---
    @classmethod
    def get_all(cls):
        pass
    
#---crUd|UPDATE (GET_ALL_USER)---
    @classmethod
    def update(cls):
        pass
        
#---cruD|DELETE (GET_ALL_USER)---
    @classmethod
    def delete(cls):
        pass
    

#---VALIDATE_EMAIL---DONE
    @staticmethod
    def validate_register(user):
        pass
        # is_valid = True
        # query = "SELECT * FROM users WHERE email = %(email)s;"
        # valid_email_results = connectToMySQL(User.DB).query_db(query, user)
        # if len(valid_email_results) >= 1:
        #     flash("Email already taken.","register")
        #     is_valid = False
        # if not EMAIL_REGEX.match(user["email"]):
        #     flash("Invalid Email!!!", "register")
        #     is_valid = False
        # if len(user["first_name"]) < 3:
        #     flash("First name must be at least 3 characters.")
        #     is_valid = False
        # if len(user["last_name"]) < 3:
        #     flash("Last name must be at least 3 characters.")
        #     is_valid = False
        # if len(user["password"]) < 8:
        #     flash("Last name must be at least 8 characters.")
        #     is_valid = False
        # if user["password"] != user["confirm"]:
        #     flash("Password does not match.", "register")
        #     is_valid = False
        # return is_valid

#---VALIDATE_LOGIN---DONE
    @staticmethod
    def validate_login(user):
        pass
        # is_valid = True
        # query = "SELECT * FROM users WHERE email = %(email)s;"
        # valid_login_results = connectToMySQL(User.DB).query_db(query, user)
        # return is_valid
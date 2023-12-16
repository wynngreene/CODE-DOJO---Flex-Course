from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Recipe:
#---START---DONE
    DB = "recipe_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_30 = data["under_30"]
        self.user_id = data["user_id"]

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

#---cRud|READ (GET_ALL_USER)---
    @classmethod
    def get_all(cls):
        pass
        # query = "SELECT * FROM users"
        # get_all_results = connectToMySQL(cls.DB).query_db(query)
        # users = []
        # for row in get_all_results:
        #     users.append( cls[row])
        # return users
    
#---crUd|UPDATE (GET_ALL_USER)---
    @classmethod
    def update(cls):
        pass
        
#---cruD|DELETE (GET_ALL_USER)---
    @classmethod
    def delete(cls):
        pass
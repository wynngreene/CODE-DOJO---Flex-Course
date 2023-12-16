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
        query = """
                INSERT INTO recipes ( name, description, instructions, date_made, under_30, user_id )
                VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s,  %(user_id)s );
                """
        save_result = connectToMySQL(cls.DB).query_db(query, data)
        return save_result

#---cRud|READ (GET_ALL_USER)---
    @classmethod
    def get_all(cls):
        pass
        query = "SELECT * FROM recipes"
        get_all_results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for row in get_all_results:
            users.append( cls[row])
        return users
    
#---crUd|UPDATE (GET_ALL_USER)---
    @classmethod
    def update(cls):
        pass
        
#---cruD|DELETE (GET_ALL_USER)---
    @classmethod
    def delete(cls):
        pass
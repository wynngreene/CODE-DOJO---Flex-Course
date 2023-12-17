from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Recipe:
#---START---DONE
    DB = "recipe_schema"

    def __init__(self, recipe):
        self.id = recipe["id"]
        self.name = recipe["name"]
        self.description = recipe["description"]
        self.instructions = recipe["instructions"]
        self.date_made = recipe["date_made"]
        self.under_30 = recipe["under_30"]
        self.created_at = recipe["created_at"]
        self.updated_at = recipe["updated_at"]
        self.user = None

#---Crud|CREATE (SAVE)---
    @classmethod
    def save(cls, recipes_data):
        query = """
                INSERT INTO recipes ( name, description, instructions, date_made, under_30, user_id, created_at, updated_at )
                VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s,  %(user_id)s, NOW(), NOW() );
                """
        save_result = connectToMySQL(cls.DB).query_db(query, recipes_data)
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
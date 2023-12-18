from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user_Model


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

#---cRud|READ (GET_ONE_RECIPE)---
    @classmethod
    def get_one_recipe_id(cls, recipe_id):
        pass
        query = """SELECT * FROM recipes
        JOIN users on recipes.user_id = users.id
        WHERE recipes.id = %(id)s"""

        data = {
            "id":recipe_id
        }

        get_one_results = connectToMySQL(cls.DB).query_db(query, data)
        recipe_dict = get_one_results[0]

        recipe_obj = Recipe(recipe_dict)

        user_obj = user_Model.User({
            "id" : recipe_dict["users.id"],
            "first_name" : recipe_dict["first_name"],
            "last_name" : recipe_dict["last_name"],
            "email" : recipe_dict["email"],
            "password" : recipe_dict["password"],
            "created_at" : recipe_dict["users.created_at"],
            "updated_at" : recipe_dict["users.updated_at"]
        })

        recipe_obj.user = user_obj

        return recipe_obj

#---Crud|CREATE (SAVE)---
    @classmethod
    def save(cls, recipes_data):
        query = """
                INSERT INTO recipes ( name, description, instructions, date_made, under_30, created_at, updated_at, user_id)
                VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, NOW(), NOW(), %(user_id)s );
                """
        save_result = connectToMySQL(cls.DB).query_db(query, recipes_data)
        return save_result

#---cRud|READ (GET_ALL_USER)---
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM recipes
        JOIN users on recipes.user_id = users.id;"""

        results = connectToMySQL(cls.DB).query_db(query)

        recipes = []

        for recipe_dict in results:
            recipe_obj = Recipe(recipe_dict)
            user_obj = user_Model.User({
                "id" : recipe_dict["users.id"],
                "first_name" : recipe_dict["first_name"],
                "last_name" : recipe_dict["last_name"],
                "email" : recipe_dict["email"],
                "password" : recipe_dict["password"],
                "created_at" : recipe_dict["users.created_at"],
                "updated_at" : recipe_dict["users.updated_at"]
            })
            # Associate user with Recipe
            recipe_obj.user = user_obj
            # Append to List
            recipes.append(recipe_obj)
        # Return the list of Recipes
        return recipes
    

    
#---crUd|UPDATE (UPDATE Recipes)---
    @classmethod
    def update(cls):
        pass
        
#---cruD|DELETE (DELETE Recipes)---
    @classmethod
    def delete_by_recipe_id(cls, recipe_id):
        query = """DELETE FROM recipes
        WHERE id = %(id)s;"""
        data = {
            "id": recipe_id
        }
        results = connectToMySQL(cls.DB).query_db(query, data)
        return
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return result
    
    @classmethod
    def delete_by_id(cls, data):
        query = "DELETE "

        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"

        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return cls(result[0])
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []

        for d in results:
            dojos.append(cls(d))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES ( %(name)s );"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return result
    
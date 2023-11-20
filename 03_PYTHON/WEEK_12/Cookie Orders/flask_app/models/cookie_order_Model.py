from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie_order:
    DB = "cookie_orders_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.full_name = data["full_name"]
        self.cookie_type = data["cookie_type"]
        self.number_boxes = data["number_boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO cookie_orders ( full_name, cookie_type, number_boxes, created_at, updated_at )
                VALUES ( %(full_name)s, %(cookie_type)s, %(number_boxes)s, NOW(),  NOW() );"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def edit(cls, data):
        query = """
                UPDATE cookie_orders
                SET full_name = %(full_name)s,
                cookie_type = %(cookie_type)s,
                number_boxes = %(number_boxes)s,
                updated_at = NOW(),
                WHERE id = %(id)s;
                """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
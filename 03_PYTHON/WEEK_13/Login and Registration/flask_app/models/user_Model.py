# from flask_app.config.mysqlconnection import connectToMySQL
# from flask import flash

# class User:
#     DB = "database_schema"
#     def __init__(self, data):
#         self.id = data["id"]
#         self.full_name = data["full_name"]
#         self.cookie_type = data["cookie_type"]
#         self.number_boxes = data["number_boxes"]
#         self.created_at = data["created_at"]
#         self.updated_at = data["updated_at"]
        
#     @classmethod
#     def get_one(cls, order_id):
#         query = """
#                 SELECT * FROM cookie_orders
#                 WHERE id = %(id)s
#                 """
#         order_dictionary = connectToMySQL(cls.DB).query_db(query, {"id": order_id})
#         order = Cookie_order(order_dictionary[0])
#         return order

#     @classmethod
#     def get_all(cls):
#         all_orders_list = []
#         query = "SELECT * FROM cookie_orders"
#         all_orders_data = connectToMySQL(cls.DB).query_db(query)
        
#         for order in all_orders_data:
#             new_order_object = Cookie_order(order)
#             all_orders_list.append(new_order_object)
#         return all_orders_list
    
#     @classmethod
#     def save(cls, data):
#         query = """
#                 INSERT INTO cookie_orders ( full_name, cookie_type, number_boxes, created_at, updated_at )
#                 VALUES ( %(full_name)s, %(cookie_type)s, %(number_boxes)s, NOW(),  NOW() );"""
#         result = connectToMySQL(cls.DB).query_db(query, data)
#         return result
    

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
    
#     @staticmethod
#     def validate_order(data):
#         is_valid = True
#         # Check if each field is blank
#         if len(data["full_name"]) == 0:
#             flash("Name required!")
#             is_valid = False
#         if len(data["cookie_type"]) == 0:
#             flash("Cookie type required!")
#             is_valid = False
#         if len(data["number_boxes"]) == 0:
#             flash("Number of box(es) required!")
#             is_valid = False    
#         elif int(data["number_boxes"]) <= 0:
#             flash("Number of box(es) must be a valid positive!")
#             is_valid = False

#         return is_valid


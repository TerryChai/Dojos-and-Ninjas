from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        dojos = []
        for u in results:
            dojos.append(cls(u))
        print(dojos)
        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        # this comes back as the new row id #
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod
    def get_one_dojo_all_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"

        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        if result:
            dojo_obj = cls(result[0])
            dojo_obj.ninja= []
            for data in result:
                ninja_data ={
                    "id": data['ninjas.id'],
                    "first_name": data['first_name'],
                    "last_name": data['last_name'],
                    "age": data['age'],
                    "created_at": data['ninjas.created_at'],
                    "updated_at": data['ninjas.updated_at'],
                    "dojo_id": data['dojo_id']
                }
                dojo_obj.ninja.append(ninja.Ninja(ninja_data))
            return dojo_obj

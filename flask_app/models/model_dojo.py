from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_ninja import Ninja


DATABASE = 'dojos_and_ninjas_db'

class Dojo:
    def __init__(self, data: dict) -> None:
        self.id         = data['id']
        self.name       = data['name']
        self.created_at = data['updated_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls) -> list['Dojo']:
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row in results:
            all_dojos.append(cls(row))
        return all_dojos

    @classmethod
    def get_dojo(cls, id: str) -> 'Dojo':
        data = { 'id': int(id) }
        query = 'SELECT * FROM dojos \
            WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    """ @classmethod
    def get_dojos_ninjas(cls, id: str):
        data = { 'id': int(id) }
        query = 'SELECT ninjas.* \
            FROM dojos \
            JOIN ninjas ON dojos.id = ninjas.dojo_id \
            WHERE dojos.id = %(id)s;'
        ninjas_results = connectToMySQL(DATABASE).query_db(query, data)
        print(ninjas_results)
        all_ninjas_in_dojo = []
        for row in ninjas_results:
            all_ninjas_in_dojo.append(cls(row))
        return all_ninjas_in_dojo """

    @classmethod
    def get_dojo_with_ninjas_by_dojo_id(cls, dojo_id) -> 'Dojo':
        data = { 'dojo_id': int(dojo_id) }
        query = 'SELECT * FROM dojos \
            LEFT JOIN ninjas on dojos.id = ninjas.dojo_id \
            WHERE dojos.id = %(dojo_id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo_instance = cls(results[0])
        all_ninjas_in_dojo = [];
        for row in results:
            if row['first_name'] == None:
                break
            ninjas_data = {
                **row,
                'id': row['ninjas.id'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            all_ninjas_in_dojo.append(Ninja(ninjas_data))
        dojo_instance.ninjas = all_ninjas_in_dojo
        return dojo_instance


    @classmethod
    def create_dojo(cls, data: list[dict]) -> int:
        query = 'INSERT INTO dojos (name) \
            VALUES(%(name)s);'
        new_dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return new_dojo_id

    @classmethod
    def update_dojo(cls, data: list[dict]) -> None:
        query = 'UPDATE dojos \
            SET name = %(name)s \
            WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return None
    
    @classmethod
    def delete_dojo(cls, id: str) -> None:
        data = { 'id': int(id) }
        query = 'DELETE FROM dojos \
            WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return None
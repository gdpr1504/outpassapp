from flask_restful import Resource, reqparse
from db import query
from flask_jwt_extended import create_access_token, jwt_required

class details(Resource):
    def get(self):
    	parser = reqparse.RequestParser()

        parser.add_argument('id', type = int, required = True, help = 'id cannot be left blank')

        data = parser.parse_args()
        try:
            return query(f"""SELECT * FROM tracker WHERE id = '{data['id']}'""",return_json=False),200
        except:
            return {"message":"id doesn't exist"},500

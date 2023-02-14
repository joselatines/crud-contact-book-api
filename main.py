from flask import Flask, request
from uuid import uuid4
from flask_restful import Resource, Api, reqparse
from database.main import query_db, tables

app = Flask(__name__)
api = Api(app)


class BaseResource(Resource):
    @staticmethod
    def handle_exception(e):
        return {
            "message": "Error while retrieving the contact",
            "error": str(e),
            "status": 500,
        }, 500


class ContactsList(BaseResource):
    def get(self):
        try:
            contacts = query_db(f"SELECT * FROM {tables['contacts']}")
            if contacts:
                return {"message": "Success", "data": contacts, "status": 200}
            else:
                return {"message": "No contacts found", "status": 200}

        except Exception as e:
            return self.handle_exception(e)

    def post(self):
        try:
            data = request.get_json()
            name = data.get("name")
            email = data.get("email")
            id = str(uuid4())

            if name and email and id:
                query_db(
                    f"INSERT INTO {tables['contacts']} (name, email, id) VALUES (?, ?, ?)",
                    [name, email, id],
                    commit=True,
                )

                return {"message": "Contact created successfully", "status": 201}, 201
            else:
                return {"message": "All fields are required", "status": 400}, 400

        except Exception as e:
            return self.handle_exception(e)


class ContactResource(BaseResource):
    def get(self, contact_id):
        try:
            contact = query_db(
                f"SELECT * FROM {tables['contacts']} WHERE id = ?",
                (contact_id,),
                one=True,
            )

            if contact:
                contact_json = {
                    "id": contact[0],
                    "name": contact[1],
                    "email": contact[2],
                }
                return {
                    "message": "Contact found successfully",
                    "data": contact_json,
                    "status": 200,
                }, 200
            else:
                return {"message": "Contact not found", "status": 404}, 404

        except Exception as e:
            return self.handle_exception(e)

    def put(self, contact_id):
        try:
            contact = query_db(
                f"SELECT * FROM {tables['contacts']} WHERE id = ?",
                (contact_id,),
                one=True,
            )

            if contact:
                # create a RequestParser object to parse incoming request data
                parser = reqparse.RequestParser()
                parser.add_argument("name", type=str, help="Name of the contact")
                parser.add_argument("email", type=str, help="Email of the contact")
                # parse the incoming request data and extract the expected arguments
                args = parser.parse_args()

                if args["name"] and args["email"]:
                    query_db(
                        f"UPDATE {tables['contacts']} SET name = ?, email = ? WHERE id = ?",
                        (args["name"], args["email"], contact_id),
                        commit=True,
                    )

                    return {
                        "message": "Contact updated successfully",
                        "status": 200,
                    }, 200
                else:
                    return {"message": "Fields cannot be empty", "status": 400}, 400
            else:
                return {"message": "Contact not found", "status": 404}, 404

        except Exception as e:
            return self.handle_exception(e)

    def delete(self, contact_id):
        try:
            contact = query_db(
                f"SELECT * FROM {tables['contacts']} WHERE id = ?",
                (contact_id,),
                one=True,
            )

            if contact:
                query_db(
                    f"DELETE FROM {tables['contacts']} WHERE id = ?",
                    (contact_id,),
                    commit=True,
                )
                return {"message": "Contact deleted successfully", "status": 200}, 200

            else:
                return {"message": "Contact not found", "status": 404}, 404

        except Exception as e:
            return self.handle_exception(e)


api.add_resource(ContactResource, "/contacts/<string:contact_id>")
api.add_resource(ContactsList, "/contacts")

if __name__ == "__main__":
    app.run(debug=True)

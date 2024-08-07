from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
import json
from marshmallow import Schema, fields, validate, ValidationError
import os

app = Flask(__name__)
api = Api(app)
CORS(app)
DEFAULT_JSON_PATH = "sample_input_data.json"
data_store = {}


class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    language = fields.Str(required=True, validate=validate.Length(min=1))
    bio = fields.Str(required=True)
    version = fields.Float(required=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)


def convert_names_to_uppercase(data):
    for user in data:
        user["name"] = user["name"].upper()
    return data


class LoadData(Resource):
    def get(self):
        global data_store

        file_path = request.args.get(
            "file", default=DEFAULT_JSON_PATH, type=str
        )

        if not os.path.isfile(file_path):
            return jsonify({"error": "File not found"}), 404

        if not file_path.endswith(".json"):
            return jsonify(
                {"error": "Invalid file type, please use a JSON file"}, 400
            )
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            data = convert_names_to_uppercase(data)
            validated_data = users_schema.load(data)
            data_store = {user["name"]: user for user in validated_data}
            return jsonify({"message": "Data loaded successfully"}, 200)

        except json.JSONDecodeError:
            return jsonify({"message": "Invalid JSON format"}, 400)
        except ValidationError as err:
            return jsonify({"message": err.messages}, 400)
        except Exception as e:
            return jsonify({"message": str(e)}, 500)


class FetchUsers(Resource):
    def get(self):
        global data_store
        if not data_store:
            return jsonify({"error": "Please load the data before fetching!!!"}, 404)
        uname = request.args.get("name", default=None, type=str)
        if uname:
            uname = uname.upper()
            user = data_store.get(uname)
            if user:
                return jsonify(user)
            else:
                return jsonify({"error": "User not found"}, 404)
        else:
            return jsonify(list(data_store.values()))


api.add_resource(LoadData, "/fetch-data/")
api.add_resource(FetchUsers, "/get-processed-data/")

if __name__ == "__main__":
    app.run(debug=True)

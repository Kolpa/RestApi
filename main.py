from flask import Flask

from flask_restful import fields, marshal_with
from flask_restful import reqparse
from flask_restful import Resource, Api

from data import TodoDB


app = Flask(__name__)
api = Api(app)
db = TodoDB()

resource_fields = {
    'tid':   fields.Integer,
    'name':    fields.String,
    'description': fields.String,
    'time': fields.Float
}

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('description')


class TodoRes(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        return db.getTodo(todo_id)

    @marshal_with(resource_fields)
    def put(self, todo_id):
        dt = parser.parse_args(strict=True)

        if db.getTodo(todo_id) is None:
            return {'status': 'Not Found'}, 404

        return db.editTodo(todo_id, dt['name'], dt['description']), 202

    def delete(self, todo_id):
        if db.getTodo(todo_id) is None:
            return {'status': 'Not Found'}, 404

        db.deleteTodo(todo_id)
        return {'status': 'Deleted'}, 200


class TodosRes(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return db.getTodos()

    @marshal_with(resource_fields)
    def post(self):
        dt = parser.parse_args(strict=True)
        return db.addTodo(dt['name'], dt['description']), 201

api.add_resource(TodosRes, '/todo')
api.add_resource(TodoRes, '/todo/<int:todo_id>')


class TeapotRes(Resource):
    def get(self):
        return "I'm a Teapot", 314

api.add_resource(TeapotRes, '/teapot')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from create_database  import db,Employees

app = Flask(__name__)
# applies CORS headers to all routes, enabling resources to be accessed
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Employees(Resource):

    # read
    def get(self, employee_id=None):
        if employee_id:
            user =Employees.query.get(employee_id)
            if not user:
                return {'error': 'User not found'}, 404
            return {'user': user.to_dict()}, 200
        else:
            users = Employees.query.all()
            return {'users': [user.to_dict() for user in users]}, 200

    # create
    def post(self):
        data = request.get_json()
        employee_id=data.get('employee_id')
        start_date=data.get('start_date')
        end_date= data.get('end_date')
        leave_type=data.get('leave_type')
        reason=data.get('reason')
        if not employee_id:
            return {'error': 'Not found'},404
        new_user = Employees(empoyee_id=employee_id,start_date=start_date,end_date=end_date,leave_type=leave_type,reason=reason)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User added successfully'}, 201
    
    
api.add_resource(Employees,'/api/v1/leave-requests/{employee_id}')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employees(db.Model):
    __tablename__ = 'Employees'
    id = db.Column(db.Integer, primary_key=True)
    employee_id=db.Column(db.Integer)
    start_date=db.Column(db.String(50), unique=True, nullable=False)
    end_date=db.Column(db.String(50), unique=True, nullable=False)
    leave_type= db.Column(db.String(100), unique=True, nullable=False)
    reason=db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
          'employee_id':self.employee_id,
          'start_date':self.start_date,
          'end_date':self.end_date,
          'leave_type':self.leave_type,
          'reason':self.reason
        }
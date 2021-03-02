from extensions import db
from flask import Blueprint
from flask_restful import Resource
import pandas as pd

timetable_api = Blueprint('timetable_api', __name__)


class TimeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon = db.Column(db.String(100), nullable=False)
    tue = db.Column(db.String(100), nullable=False)
    wed = db.Column(db.String(100), nullable=False)
    thu = db.Column(db.String(100), nullable=False)
    fri = db.Column(db.String(100), nullable=False)
    sat = db.Column(db.String(100), nullable=False)


class News(Resource):
    @timetable_api.route("/timetable/<int:member_id>", methods=['GET'])
    def get(member_id):
        data = pd.read_excel("time_table.xlsx")
        table = data[data['ID'] == member_id]
        if table['ID'].empty:
            return {'message': "Time Table doesn't exist...."}
        else:
            return {'mon': table.iloc[0]['Monday'], 'tue': table.iloc[0]['Tuesday'], 'wed': table.iloc[0]['Wednesday'],
                    'thu': table.iloc[0]['Thursday'], 'fri': table.iloc[0]['Friday'], 'sat': table.iloc[0]['Saturday']}

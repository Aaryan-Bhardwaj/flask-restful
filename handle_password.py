from extensions import db
from flask import Blueprint, abort, make_response, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with

password_api = Blueprint('password_api', __name__)


class PasswordModel(db.Model):
    __bind_key__ = 'passworddb'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    


news_put_args = reqparse.RequestParser()
news_put_args.add_argument("password", type=str, help="Date missing", required=True)

news_update_args = reqparse.RequestParser()
news_update_args.add_argument("password", type=str, help="Date missing")

resource_fields = {
    'id': fields.Integer,
    'password': fields.String,
}


class Password(Resource):
    @password_api.route("/pass/<int:member_id>", methods=['GET'])
    @marshal_with(resource_fields)
    def get(member_id):
        result = PasswordModel.query.filter_by(id=member_id).first()
        if not result:
            abort(make_response(jsonify(message="Password no exist.."), 404))
        return result
    
    @password_api.route("/pass/<int:member_id>", methods=['PUT'])
    @marshal_with(resource_fields)
    def put(member_id):
        args = news_put_args.parse_args()
        result = PasswordModel.query.filter_by(id=member_id).first()
        if result:
            if args['password']:
                result.password = args['password']
        else:
            result = PasswordModel(id=member_id, password=args['password'])
            db.session.add(result)
        
        db.session.commit()
        return result, 201

#     @password_api.route("/pass/<int:member_id>", methods=['PUT'])
#     @marshal_with(resource_fields)
#     def put(member_id):
#         args = news_put_args.parse_args()
#         passw = PasswordModel(id=member_id, password=args['password'])
#         db.session.add(passw)
#         db.session.commit()
#         return passw, 201

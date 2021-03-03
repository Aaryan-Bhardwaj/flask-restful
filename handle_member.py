from extensions import db
from flask import Blueprint, abort, make_response, jsonify
from flask_restful import Resource, reqparse, fields, marshal_with

member_api = Blueprint('member_api', __name__)


class MemberModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	contact = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.String(1), nullable=False)
	trainer = db.Column(db.String(100), nullable=False)
	membership = db.Column(db.String(100), nullable=False)
	balance = db.Column(db.Integer, nullable=False)
	status = db.Column(db.String(15), nullable=False)
	start_date = db.Column(db.String(8), nullable=False)


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of guy missing", required=True)
video_put_args.add_argument("contact", type=int, help="Age of guy missing", required=True)
video_put_args.add_argument("gender", type=str, help="Weight of guy missing", required=True)
video_put_args.add_argument("trainer", type=str, help="Height of guy missing", required=True)
video_put_args.add_argument("membership", type=str, help="Height of guy missing", required=True)
video_put_args.add_argument("balance", type=int, help="Height of guy missing", required=True)
video_put_args.add_argument("status", type=str, help="Height of guy missing", required=True)
video_put_args.add_argument("start_date", type=str, help="Height of guy missing", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of guy missing")
video_update_args.add_argument("contact", type=int, help="Age of guy missing")
video_update_args.add_argument("gender", type=str, help="Weight of guy missing")
video_update_args.add_argument("trainer", type=str, help="Height of guy missing")
video_update_args.add_argument("membership", type=str, help="Height of guy missing")
video_update_args.add_argument("balance", type=int, help="Height of guy missing")
video_update_args.add_argument("status", type=str, help="Height of guy missing")
video_update_args.add_argument("start_date", type=str, help="Height of guy missing")


resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'contact': fields.Integer,
	'gender': fields.String,
	'trainer': fields.String,
	'membership': fields.String,
	'balance': fields.Integer,
	'status': fields.String,
	'start_date': fields.String,
}


class Member(Resource):
	@member_api.route("/member/<int:member_id>", methods=['GET'])
	@marshal_with(resource_fields)			# serializes return object. see result is in db format.
	def get(member_id):				# video_id = request argument
		result = MemberModel.query.filter_by(id=member_id).first()
		if not result:
			abort(make_response(jsonify(message="Member with ID not found"), 404))
		return result

	@member_api.route("/member/<int:member_id>", methods=['PUT'])
	@marshal_with(resource_fields)
	def put(member_id):
		args = video_put_args.parse_args()     # all request arguments from video_put_args
		result = MemberModel.query.filter_by(id=member_id).first()
		if result:
			abort(make_response(jsonify(message="Member with ID taken"), 409))
		member = MemberModel(id=member_id, name=args['name'], contact=args['contact'], gender=args['gender'], trainer=args['trainer'], membership=args['membership'], balance=args['balance'], status=args['status'], start_date=args['start_date'], )
		db.session.add(member)
		db.session.commit()
		return member, 201

	@member_api.route("/member/<int:member_id>", methods=['PATCH'])
	@marshal_with(resource_fields)
	def patch(member_id):
		args = video_update_args.parse_args()
		result = MemberModel.query.filter_by(id=member_id).first()    # request to db
		if not result:
			abort(404, message="Videos with ID not found, can't update.")

		if args['name']:
			result.name = args['name']
		if args['contact']:
			result.contact = args['contact']
		if args['gender']:
			result.gender = args['gender']
		if args['trainer']:
			result.trainer = args['trainer']
		if args['membership']:
			result.membership = args['membership']
		if args['balance']:
			result.balance = args['balance']
		if args['status']:
			result.status = args['status']
		if args['start_date']:
			result.start_date = args['start_date']

		db.session.commit()
		return result, 200

	@member_api.route("/member/<int:member_id>", methods=['DELETE'])
	@marshal_with(resource_fields)
	def delete(member_id):
		result = MemberModel.query.filter_by(id=member_id).first()
		if not result:
			abort(make_response(jsonify(message="Member with ID not found"), 404))
		MemberModel.query.filter_by(id=member_id).delete()
		db.session.commit()
		return result, 204

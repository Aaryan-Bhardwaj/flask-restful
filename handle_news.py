from extensions import db
from flask import Blueprint, abort, make_response, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with

news_api = Blueprint('news_api', __name__)


class NewsModel(db.Model):
    __bind_key__ = 'newsdb'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(8), nullable=False)
    text = db.Column(db.String(1000), nullable=False)


news_put_args = reqparse.RequestParser()
news_put_args.add_argument("date", type=str, help="Date missing", required=True)
news_put_args.add_argument("text", type=str, help="Body missing", required=True)

news_update_args = reqparse.RequestParser()
news_update_args.add_argument("date", type=str, help="Date missing")
news_update_args.add_argument("text", type=str, help="Body missing")

resource_fields = {
    'id': fields.Integer,
    'date': fields.String,
    'text': fields.String,
}


class News(Resource):
    @marshal_with(resource_fields)
    def serialize(data):
        return data

    @news_api.route("/news", methods=['GET'])
    # @marshal_with(resource_fields)
    def get():
        result = NewsModel.query.order_by(-NewsModel.id).limit(5).all()
        if not result:
            abort(make_response(jsonify(message="No News..."), 404))
        print(result)
        return {'1': News.serialize(data=result[0]), '2': News.serialize(data=result[1]), '3': News.serialize(data=result[2]),
                '4': News.serialize(data=result[3]), '5': News.serialize(data=result[4])}

    @news_api.route("/news", methods=['PUT'])
    @marshal_with(resource_fields)
    def put():
        args = news_put_args.parse_args()
        news = NewsModel(date=args['date'], text=args['text'])
        db.session.add(news)
        db.session.commit()
        return news, 201

    @news_api.route("/news/<int:news_id>", methods=['DELETE'])
    @marshal_with(resource_fields)
    def delete(news_id):
        result = NewsModel.query.filter_by(id=news_id).first()
        if not result:
            abort(make_response(jsonify(message="No News with that ID..."), 404))
        NewsModel.query.filter_by(id=news_id).delete()
        db.session.commit()
        return result, 204



from flask import Flask
from handle_member import member_api
from handle_news import news_api
from handle_timetable import timetable_api
from config import config


def create_app():
	app = Flask(__name__)
	app.config.from_object(config)
	register_extensions(app)
	app.register_blueprint(member_api)
	app.register_blueprint(news_api)
	app.register_blueprint(timetable_api)
	if __name__ == "__main__":
		app.run(debug=True)
	return app


def register_extensions(app):
	from extensions import db  # db store to variable
	db.init_app(app)
	with app.app_context():
		db.create_all()


app1 = create_app()

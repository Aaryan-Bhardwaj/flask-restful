from flask import Flask
from handle_member import member_api
from handle_news import news_api
from handle_timetable import timetable_api
from handle_password import password_api
from config import config


def create_app():
	app = Flask(__name__)
	app.config.from_object(config)
	register_extensions(app)
	app.register_blueprint(member_api)
	app.register_blueprint(news_api)
	app.register_blueprint(timetable_api)
	app.register_blueprint(password_api)
	if __name__ == "__main__":
		app.run(debug=True)
	return app


def register_extensions(app):
	from extensions import db  # db store to variable
	db.init_app(app)
	with app.app_context():
# 		db.drop_all()
		db.create_all(bind='passworddb')


app = create_app()

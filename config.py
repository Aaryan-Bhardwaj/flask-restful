class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///members.db'
    SQLALCHEMY_BINDS = {'newsdb': 'sqlite:///news.db', 'passworddb': 'sqlite:///password.db'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config

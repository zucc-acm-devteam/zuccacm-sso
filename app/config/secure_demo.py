# 定义数据库信息
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@ip:port/acmsso?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 定义flask信息
SECRET_KEY = 'secretkey'
SESSION_COOKIE_NAME = 'sso-session'
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True

# 定义redis信息
REDIS_URL = 'redis://127.0.0.1:6379'

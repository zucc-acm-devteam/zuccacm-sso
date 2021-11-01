from flask_cors import CORS
from flask_login import LoginManager
from flask_redis import FlaskRedis

from app.models.base import db
from .app import Flask

cors = CORS(supports_credentials=True)
login_manager = LoginManager()
redis = FlaskRedis(decode_responses=True)


def register_blueprints(flask_app):
    from app.api.v1 import create_blueprint_v1
    flask_app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(flask_app):
    # 注册sqlalchemy

    db.init_app(flask_app)

    # 初始化数据库
    from app.models import user
    with flask_app.app_context():
        db.create_all()

    # 注册cors
    cors.init_app(flask_app)

    # 注册用户管理器
    login_manager.init_app(flask_app)

    # 注册redis
    redis.init_app(flask_app)


def create_app():
    from datetime import datetime

    from app.libs.global_varible import g

    g.run_start_time = datetime.now().strftime("%a %b %d %Y %H:%M:%S")

    flask_app = Flask(__name__)

    # 导入配置
    flask_app.config.from_object('app.config.secure')

    register_blueprints(flask_app)
    register_plugin(flask_app)

    return flask_app
